# How this repository was made (Volta Redonda)

This file is written by the build on 2026-11-03, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Câmara Municipal de Volta Redonda, SAPL: Texto Articulado of the Lei Orgânica, one view per period of vigência | <https://sapl.voltaredonda.rj.leg.br/norma/5735> | 2026-11-02 | Text: Câmara Municipal de Volta Redonda, SAPL (Sistema de Apoio ao Processo Legislativo), Lei Orgânica do Município de Volta Redonda, sapl.voltaredonda.rj.leg.br. Lei 9.610/1998 art. 8 IV: the texts of laws and other official acts are not protected by copyright. Non-official text: only the Diário Oficial do Município is authoritative. |
| Câmara Municipal de Volta Redonda, SAPL: scanned PDFs of municipal laws, read by OCR | <https://sapl.voltaredonda.rj.leg.br/norma/pesquisar> | 2026-11-03 | Texts: Câmara Municipal de Volta Redonda, SAPL (Sistema de Apoio ao Processo Legislativo), sapl.voltaredonda.rj.leg.br; SAPL: "Conteúdo e dados sob licença Creative Commons 4.0 Atribuir Fonte - Compartilhar Igual". Lei 9.610/1998 art. 8 IV: the texts of laws and other official acts are not protected by copyright. Non-official text: only the official gazette is authoritative. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `lei-organica` | Lei Orgânica do Município de Volta Redonda | 69 | 1990-04-05 to 2021-09-24 |
| `lei-2026-06890` | Lei nº 6.890, de 1 de outubro de 2026 | 1 | 2026-10-01 to 2026-10-01 |
| `lei-2026-06834` | Lei nº 6.834, de 15 de junho de 2026 | 1 | 2026-06-15 to 2026-06-15 |
| `lei-2025-06667` | Lei nº 6.667, de 15 de setembro de 2025 | 1 | 2025-09-15 to 2025-09-15 |
| `lei-2025-06599` | Lei nº 6.599, de 28 de abril de 2025 | 1 | 2025-04-28 to 2025-04-28 |
| `lei-2025-06595` | Lei nº 6.595, de 25 de abril de 2025 | 1 | 2025-04-25 to 2025-04-25 |
| `lei-2025-06550` | Lei nº 6.550, de 19 de fevereiro de 2025 | 1 | 2025-02-19 to 2025-02-19 |

The build made 68 commits:

| Commits | Kind |
| ---: | --- |
| 7 | first version of an act |
| 61 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futuro`: laws not yet in force on 2026-11-03.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 75 laws in the record.
- 136 tags.

## Dates

Each commit is dated at noon (America/Sao_Paulo) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: The Lei Orgânica and its amendments are promulgated by the Mesa da Câmara and take effect as they state; this record dates each version by the first day of vigência SAPL gives it. Municipal laws: Decreto-Lei 4.657/1942 (LINDB) art. 1 gives 45 days unless a law says otherwise; this record takes in only laws whose vigência clause says they take effect on their publication (or signature) and dates each by the publication date SAPL records for it (else by its date). https://sapl.voltaredonda.rj.leg.br/norma/5735

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `a307a83eced888ada8709e648a84841111d7b12a8ce3d1f6913a0c89be32594e` (567670 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `0fad90cf931c453951234ecf904d05ee79f3ec7e`, `check.py` `5d719354ea4c62d240c93d2cae446307d81d9e81`, `on.py` `aff48cf1b68d50c7ba8f399ca32261871c301824`.
- Python 3.14.4; git version 2.53.0.

## Checks

75 versions of 7 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Each version is one SAPL "vigência" view of the Lei Orgânica's Texto Articulado: the text in force from the view's first day, dated by that day and credited to the act SAPL says gave it ("Dada por ..."); the first view (from 5 April 1990) is credited to the Lei Orgânica itself. Where two views start on the same day (two amendments of the same date), both are kept, in SAPL order, as two versions of that day. Each unit that differs from the view before is credited to the act that gave the view.
- When the text SAPL shows as in force now (the norma page, with its "Vigência a partir de" day and "Dada por" act) starts after the last view, it is the last version. Where SAPL starts a period without naming an amending act, the units that changed are left uncredited and committed as publisher commits, not guessed.
- Each provision is one line: its label ("Art. 1º.", "§ 1º", "XV –") followed by its text; table rows are one line each, cells separated by " | ". Notes SAPL keeps under a provision or links into it ("Inclusão feita pelo ..."), provisions it marks as superseded, the amending acts own blocks it shows inside the text and the amendment notes typed into the text ("(Redação dada pela Emenda ...)", "(Incluído pela ...)") are left out.
- One file per Art.; headings stand above the first article under them; the "Ato das Disposições Orgânicas Transitórias", numbered from 1 again, is adt-*. "000-titulo" holds the preamble.
- Each municipal law ("Lei" and "Lei Complementar") is given as enacted, from the PDF the Câmara's SAPL holds for it, credited to the law itself and dated by the publication date SAPL records for it (else by the law's own date). Later amendments by other laws are not worked into earlier laws: each law is its own file set as enacted. Laws are taken newest first, in parts.
- Left out: scans (with or without an OCR layer), PDFs whose heading does not carry the record's number, texts with no article or no closing date line, texts carrying alteration notes, and laws whose vigência clause sets another day than their publication (or that have none, so that the 45 days of the LINDB apply).
- The text runs from the law's heading to its closing date line (signatures after it are left out); lines repeated at the top or bottom of two or more pages (letterheads, footers) and page numbers are left out. Lines are joined into paragraphs: a new paragraph starts at a provision label, a heading line, or after a line ending in ".", ";" or ":". One file per Art.; "000-titulo" holds what comes before the first article.
- 40-ocr-001: 6 municipal laws read by OCR from the scanned PDFs the Câmara's SAPL holds (Alan's decision D8, 2026-11-02: OCR is allowed for official scans whose terms allow reuse, marked as OCR and spot-checked). Reader: Tesseract 5.4.0, language model "por" (tessdata_best), --psm 3, pages rendered at 300 dpi; the city's Lexifina's code rules (heading, articles, closing date line, alteration notes, vigência, dates, furniture and page numbers) apply unchanged. Every file of an OCR'd law starts with a front-matter line "Text-source: OCR (...) of the official scan <url>", and its commit message says the same. Spot-check (instead of the letters check with a second PDF reader, which needs a text layer): for every law in the part, 3 paragraphs drawn at random are cut out of the scan and read again with a different setting (tessdata_fast, --psm 6); a law with any paragraph under 98% character agreement is left out. Also left out: a law with any paragraph holding 3 or more OCR-noise tokens, or with a publication stamp ("PREF. MUN.", "Publicado no DOM") read into its text. Agreement in this part: lowest law 99.44%, mean 99.77%. OCR can misread single characters; for anything that matters, read the scan.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (claude-opus-5-5) wrote Lexifina's code and chose the sources. No model output is used as legal text or dates: every word comes from the SAPL pages.
- Claude Code (claude-opus-5-5) wrote Lexifina's code and chose the sources. No model output is used as legal text or dates: every word comes from the Câmara's SAPL.
- Where a PDF is a scan, its words are read by Tesseract OCR, not by a language model.
