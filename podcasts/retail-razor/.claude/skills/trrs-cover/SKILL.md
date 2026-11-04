---
name: trrs-cover
description: Make The Retail Razor Show reel cover stills (1080x1920, grid-safe 4:5 centre) for an episode's reel series from templates/cover - guest cutout with baked red glow, Montserrat 900 hook headline with red key word, one illustrative prop, logo + episode line. Use when the CD asks for TRRS reel covers, thumbnails or cover frames.
---

# TRRS reel covers

Generic cover rules (hook wording, grid crop, legibility at thumbnail size) are in the L2 skill `podcast-cover`.
This skill is the TRRS series look from S6E15 (`episodes/S6E15_leslie-ann-hall/output/final/covers/`,
`contact_sheet.jpg`). **Status:** the S6E15 covers were awaiting the CD's review on 2026-11-02, so treat this as the
current proposal. Update this skill with the CD's notes.

## Look
- **Ground:** the reel ground (`trrs-style`), plus a soft red radial glow behind the guest (left 260, top 760, 1000 px).
- **Header:** `rr_logo.png` at height 96, left 60 / top 318, with "THE RETAIL RAZOR SHOW" over "SxEyy" beside it in
  peach (800, 28 px, .13em).
- **Headline** (from top 448, left 60, column width 960): uppercase Montserrat 900, cream with a warm glow, 2–4 lines,
  each line auto-fitted to its own width cap.
  - The hook is a question or a sharp claim in the guest's terms ("DO YOU CHECK REDDIT BEFORE YOU BUY?",
    "BOTTOM FUNNEL BLOAT").
  - ONE key word is red `#ff4a55` with a red glow.
  - An optional sub line sits under it (700, 44 px).
- **Guest:** a cutout from that reel's own A-roll (expressive hands, mouth mid-word, sharp face). It gets a baked warm
  grade, a soft red glow and a thin red rim, scaled 1.6x, with the face centre at x ≈ 690–700. The body runs off the
  bottom under a dark fade from y 1320.
- **Footer:** a red dash with "WITH <GUEST NAME>, <COMPANY>" in peach tracked caps at top 1556.
- **Prop:** one small illustrative object beside the narrow key line, echoing that reel's card. S6E15 props:
  - Reddit upvote badge
  - SEO→GEO chip
  - cracked AI-answer card
  - three ticked RULE tiles
  - funnel with "SAME CUSTOMERS" pool
  - VALIDATION step chip

  No invented numbers.
- **Safe zones** (drawn by `tools/review.py`):
  - the profile grid shows the 4:5 centre crop y 285–1635, so all headline and face content must sit inside it
  - keep clear of Instagram's top UI (y < 168)
  - keep clear of the right-hand action buttons (x > 950, y 1150–1750)

## Steps
1. Copy `templates/cover` → `episodes/<ep>/work/hyperframes/covers`.
2. Choose one frame per reel. Snapshot candidates from that reel's `aroll.mp4` at the guest's word midpoints, then
   compare sharpness and pose on a contact sheet. The S6E15 helper scripts `work/covers/cands.py` and `pick.py`
   hard-code that episode's crop boxes, so adapt the box or just use `hyperframes snapshot`.
3. Cut out each frame with `npx --yes hyperframes@0.8.217 remove-background`, then run `tools/clean.py in out`.
   Inspect the result; scraps of backdrop near the head (S6E15 R4/R5) are erased by hand, after which you don't re-run
   clean on that file.
4. `python tools/bake.py --project . --cutinfo <work>/covers/cut_info.json 1=... 2=...` writes
   `assets/img/guest_rN_glow.png` and `cut_info.json`.
5. Write `covers.json` (format in the `tools/gen.py` docstring and `tools/covers.sample.json`). Each line is
   `[text, key words, max px, max width]`. A line with max width < 960 leaves room for the prop. Use `"->"` for the red
   arrow. Pick a prop from `PROPS` in gen.py, or add a new one with its CSS.
6. `python tools/gen.py --config covers.json --project . --cutinfo <cut_info.json>`, then
   `npx --yes hyperframes@0.8.217 check`.
7. `npx --yes hyperframes@0.8.217 snapshot --at 0.5,1.5,... --no-end -o <dir>` (cover i sits at i + 0.5 s), then
   `python tools/review.py <dir>` and look at `review.jpg` (safe zones) and `small.png` (phone-grid legibility).
8. Deliver to `output/final/covers/`:
   - `TRRS_<SxEyy>_R<N>_cover.png` (full 1080x1920)
   - `TRRS_<SxEyy>_R<N>_cover_grid.jpg` (the 1080x1350 crop from y 285)
   - `contact_sheet.jpg`
