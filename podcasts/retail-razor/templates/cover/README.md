# TRRS reel-cover template (1080x1920 stills via HyperFrames)

Generalised from the S6E15 cover series (`episodes/S6E15_leslie-ann-hall/work/covers/*.py`,
`work/hyperframes/covers`, finals `output/final/covers/`). Procedure: skill **trrs-cover**. Tokens: skill **trrs-style**.
`index.html` and `compositions/c*.html` are GENERATED; this template ships a 2-cover sample from `tools/covers.sample.json`.

## Pipeline (per episode)
1. Copy the folder to `episodes/<SxEyy_guest>/work/hyperframes/covers`.
2. Pick one guest frame per reel from that reel's A-roll (sharp face, expressive hands, mouth mid-word, eyes open).
3. Cut out with `npx --yes hyperframes@0.8.217 remove-background` (check `--help` for the output flag) to `rN_cut.png`, then
   `python tools/clean.py <rN_cut.png> <rN_clean.png>`, then hand-erase any backdrop scraps (do not re-run clean.py after that).
4. `python tools/bake.py --project . --cutinfo <work>/cut_info.json 1=<r1_clean.png> 2=...` writes
   `assets/img/guest_rN_glow.png` (red glow + rim) and `cut_info.json`.
5. Write `covers.json` (copy `tools/covers.sample.json`): show, episode, guest line, and per cover the headline lines,
   key words, prop, face_x.
6. `python tools/gen.py --config covers.json --project . --cutinfo <cut_info.json>`.
7. `npx --yes hyperframes@0.8.217 check`, then `npx --yes hyperframes@0.8.217 snapshot --at 0.5,1.5,... --no-end -o <dir>`
   and run `python tools/review.py <dir>` for the safe-zone overlay (`review.jpg`) and phone-grid test (`small.png`).
8. Deliver `TRRS_<SxEyy>_R<N>_cover.png` (+ `_cover_grid.jpg` crop, `contact_sheet.jpg`) to `output/final/covers/`.

## Contents
| Path | What |
|---|---|
| `tools/gen.py` | config-driven generator: layout, auto-fit headline, prop library (`reddit`, `geo`, `crack`, `rules`, `funnel`, `valid`, `none`) |
| `tools/covers.sample.json`, `tools/cut_info.sample.json` | sample inputs for the shipped placeholder covers |
| `tools/clean.py` | cutout cleanup (largest subject, edge erode, despill), paths as args |
| `tools/bake.py` | grade + red glow/rim bake + cut_info, paths as args |
| `tools/review.py` | safe-zone overlay + phone-grid test from a snapshot dir |
| `assets/fonts/Montserrat.ttf`, `assets/img/rr_logo.png` | brand |

Not generalised: the six props are S6E15-specific illustrations (Reddit upvote, SEO->GEO, cracked AI answer, 3 rule
ticks, funnel, validation chip). Add a new entry to `PROPS` (and its CSS) for a new episode's idea. The candidate-frame
helpers (`cands.py`, `pick.py`) were not ported: they hard-code S6E15 crop boxes. Pick frames from snapshots instead.

## Check status
As shipped: the guest images `assets/img/guest_r1_glow.png` / `guest_r2_glow.png` are missing on purpose (episode media),
so `check` reports exactly those two `missing_local_asset` errors. With placeholder images (scratch test, 2026-11-02)
it returns ok: true with 0 errors. The only warnings are `line_unread`, which doesn't apply here because each cover is
a 1 s still slot, and the snapshot at 0.5 s / 1.5 s shows both covers laid out correctly.
