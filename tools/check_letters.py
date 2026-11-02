"""Independent letters-and-digits check of every version against its SAPL page (regular expressions only, no HTML
parser, none of the builder's code).

    python -X utf8 check_letters.py [part.json ...]

For each version the page is cut at every provision block ('<div class="dptt'); each block runs to the provision's
notes ('<div class="dn"'), which are left out, as are blocks marked "desativado", blocks right after a
'bloco_alteracao' opening (the amending act's own block) and SAPL's "nota-alteracao" links, and amendment notes typed into the text
("(Redação dada pela Emenda ...)"). The blocks' text, reduced to letters
and digits, must equal the version's unit files (changes applied to the version before) reduced the same way, each unit
found at its place in document order.
"""
import hashlib, html, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def ld(s):
    return ''.join(ch for ch in s if ch.isalnum())


def page_text(raw):
    s = raw.decode('utf-8', 'replace')
    s = re.sub(r'(?s)<a class="nota-alteracao"[^>]*>.*?</a>', ' ', s)  # SAPL's "Inclusão feita pelo ..." notes
    out = []
    parts = s.split('<div class="dptt')
    for before, chunk in zip(parts, parts[1:]):
        cls = chunk[:chunk.index('"')]
        if 'desativado' in cls or 'bloco_alteracao' in before[-120:]:
            continue  # superseded provisions; the amending act's own block shown inside the text
        chunk = chunk[chunk.index('>') + 1:]
        j = chunk.find('<div class="dn"')
        out.append(chunk[:j if j >= 0 else len(chunk)])
    t = html.unescape(re.sub(r'<[^>]+>', ' ', ' '.join(out)))
    return re.sub(r'\(\s*(?:Reda[çc][ãa]o\s+dada|Reda[çc][ãa]o\s+alterada|Inclu[íi]d[oa]s?|Acrescid[oa]s?|Acrescentad[oa]s?|Revogad[oa]s?|Alterad[oa]s?|Suprimid[oa]s?|Renumerad[oa]s?|Vide)\b[^()]*?(?:Emenda|Lei|ELO|Resolu|n\.?\s*[º°o])[^()]*\)', ' ', t, flags=re.I)  # the Câmara's typed amendment notes


def main(paths):
    bad = total = 0
    for p in paths:
        c = json.load(open(p, encoding='utf-8'))
        for a in c['acts']:
            units = {}
            for v in a['versions']:
                if 'units' in v:
                    units = dict(v['units'])
                else:
                    for k, u in v['changes'].items():
                        if u is None:
                            units.pop(k, None)
                        else:
                            units[k] = u
                raw = (HERE / '.cache' / 'sapl' / 'raw' / hashlib.sha256(v['source_url'].encode()).hexdigest()).read_bytes()
                assert hashlib.sha256(raw).hexdigest() == v['sha256'], (a['slug'], 'sha256')
                src = ld(page_text(raw))
                rest = {k: ld(re.sub(r'(?m)^#+ ', '', u['text'])) for k, u in units.items()}
                pos = 0
                while rest:
                    hit = None
                    for k, t in rest.items():
                        if t and src.startswith(t, pos) and (hit is None or len(t) > len(rest[hit])):
                            hit = k
                    if hit is None:
                        break
                    pos += len(rest.pop(hit))
                total += 1
                if rest or pos != len(src):
                    bad += 1
                    print(f'MISMATCH {a["slug"]} {v["from"]}: matched {pos}/{len(src)}; next source: '
                          f'{src[pos:pos + 80]!r}; unplaced: {list(rest)[:5]}')
    print(f'{total} versions checked, {bad} mismatches')
    return bad


if __name__ == '__main__':
    sys.exit(1 if main(sys.argv[1:] or sorted(str(p) for p in (HERE / 'corpus.d').glob('*.json'))) else 0)
