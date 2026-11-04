# TRRS S6E15 Instagram carousels: notes

## v3 (2026-11-03, current; awaiting CD review)
CD round 2 on v2 applied as written; v2 is in `output/archive/carousels_v2/`. Slide copy now lives in `v3_slides.py`
(exec'd by `gen2.py`; v2 generator kept as `gen2_v2.py`). C1 8 slides (old 6+7 merged into one 2x2 sources slide, rule
slides carry no quotes), C2 7 slides (the "one product for everyone" myth removed; cover "5 BELIEFS"), C3 answers
rewritten to answer the questions, with no text on photos (question row → answer → photo). ≥ 60 px text–image gap,
visuals at ~90% of their slot.
- New verbatim fragments verified in ep_words.json: "those vibes are more important than ever",
  "wildly important" (from "So Reddit is wildly important"). Quote audit: 0 failures. check: 0 errors.
- Headlines kept ≥ 90 px; the long CD lines therefore run to 3–4 lines (C1-5, C2-3/4/6, C3-2/3/4/6), which leaves the
  C2-6 journey visual and the C3 photos smaller than in v2. Open question: shorter wording, or smaller type allowed?

## v2 (2026-11-03, superseded)
CD note on v1: "too text heavy — more imagery than text; remove header, footer and counters." v1 is in
`output/archive/carousels_v1/`.

Rebuild (from the episode folder):
1. `python work/carousels/make_cardsnap.py`: scratch copies of the reel projects without header/captions/tags/outro/audio,
   then `npx --yes hyperframes@0.8.217 snapshot --at …` in each (card times listed in `build_visuals.py`).
2. `python work/carousels/build_visuals.py`: reel-card crops and b-roll stills → `assets/img/v/` (myth sides greyed).
3. `python work/carousels/cut_stills.py`: C3 Ricardo/Leslie cutouts from the episode (no backdrop lettering, no frame boxes).
4. `python work/carousels/gen2.py` → `npx --yes hyperframes@0.8.217 check` (0 errors; `line_unread`, `film_silent` expected)
   → `python work/carousels/export.py snap` → `export.py deliver` → `python work/carousels/audit_quotes.py` (`failures: 0`).
(`gen.py` is the v1 generator, kept for reference.)

Layout rules applied: one dominant visual per slide, headline ≤ 6 words at ≥ 90 px, ≤ 1 support line, ≤ ~18 words;
no header, footer or counters; logo on cover and close only; attribution by Caveat "— Leslie" signature or her photo.

### Quotes shortened in v2 (all still verbatim, "…" marks the cut)
- C1-2 "AI search is a mirror for what the world thinks about your brand." → headline AI SEARCH IS A MIRROR + “…for what the world thinks about your brand.”
- C1-6 Reddit line → “depending on the day” only; YouTube unquoted.
- C2-3 "GEO is looking at fresh, new, and dynamic content" → “FRESH, NEW, AND DYNAMIC…”
- C2-4 → “A HANDFUL OF HERO PRODUCTS” (verbatim fragment).
- C2-5 / C3-3 → “BOTTOM FUNNEL BLOAT” (from "We call it bottom funnel bloat").
- C2-6 the long "the days of this product works for all hair types…" quote dropped; reality is the unquoted paraphrase REAL PEOPLE, REAL RESULTS (from "real results from real people").
- C3-4 → “But is this the best product for me?” only ("Is it worth the price?" dropped).
- C3-5 → “…over half of Redditors do what they call a final check…” (full sentence kept in the caption, attributed).
- C3-6 Leslie's verbatim fragments dropped from the slide; Ricardo's “That's an important distinction.” kept.

### Open questions for the CD
1. Some reused reel cards carry the reels' invented UI prices/ratings ($32.00, 4.4, 48.2K…) as small texture (C1-4, C1-5, C2-7). They were in the approved reels; crop them out if you want zero numbers on the carousels.
2. C2-5 shows funnel artwork on both sides (grey ad-spend bar vs the bloated pool). Alternative myth visual: R5's promo lock-screen (but it carries "40% OFF").
3. C1-2 and C1-8 both use the R3 AI-answer card (mirror vs cracked). Swap C1-8 for another visual if it reads as a repeat.
4. Hashtags unchanged from v1; replace if the show has standing tags.

## v1 (2026-11-02, archived)
Text-led slides with header/footer/counters; see `output/archive/carousels_v1/`.
