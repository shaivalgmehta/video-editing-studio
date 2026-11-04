---
name: trrs-carousel
description: Make The Retail Razor Show Instagram/LinkedIn carousels (1080x1350 PNG slides + PDF + captions) for an episode in the TRRS warm-brown look - image-first playbook, myth-vs-reality and host Q&A formats built from the episode's reel cards, b-roll and speaker cutouts in one HyperFrames project, exported as stills. Use when the CD asks for TRRS carousels, swipe posts, LinkedIn document posts or slide posts from an episode.
---

# TRRS carousels

Editorial rules (cover promises an outcome, one insight per slide, save/share close) are in the L2 skill
`podcast-repurposing` §3; verbatim/attribution rules in `podcasts/CLAUDE.md`; tokens in `trrs-style`. This skill fixes the
TRRS recipe from S6E15 (`episodes/S6E15_leslie-ann-hall/work/carousels/`). v1 was rejected as text-heavy; v2 (2026-11-03)
follows the CD rules below and awaits review.

## CD rules (S6E15 review, apply without re-asking)
1. **Image first.** Each content slide = ONE dominant visual (≥ ~60% of the slide) + a headline of ≤ 6 words at
   ≥ 90 px + at most one support line (≤ 12 words). About 18 words per content slide at most. The point must be clear
   from image + headline at 360 px wide.
2. **No header, footer or slide counters.** IG shows the dots. `rr_logo.png` appears only on the cover and the close.
3. Attribution lives in the visual: a Caveat "— Leslie" signature after a quote, or the speaker's photo/cutout.
4. **Visuals are literal and real, in the reels' style**: reuse the episode's reel cards and b-roll (clean snapshots),
   real platform logos big, rebuilt UIs with invented names. Myth sides greyed (baked in PIL), reality sides vivid.
5. **Photo crops never show backdrop lettering or the burned-in show frame.** Use background-removed cutouts of the
   speaker on the brand ground (`cut_stills.py`), on-slide scale ≤ ~1.6x the source.
6. Long quotes are trimmed to the strongest verbatim fragment with "…"; the caption carries the full line.
7. **Text flows as a sentence across slides.** Read the headlines in order: they must form one sequence (C1 S6E15:
   HOW TO WIN IN AI SEARCH → AI SEARCH IS A MIRROR → PICK YOUR HERO PRODUCTS → USE ONE MESSAGE FOR EVERY TEAM →
   CREATE CONTENT HUMANS AND MACHINES CAN UNDERSTAND → 4 SOURCES AI FREQUENTLY CITES → "IT'S CHANGING EVERY DAY.").
   Playbook rule slides carry no guest quote; myth-vs-reality LESLIE SAYS lines are short plain paraphrases.
8. **Q&A answers must answer the question** in plain words ("YES. …", "NO. …", "MAKE …"); the support line carries the
   evidence (a verbatim fragment). Never answer with a slogan the question didn't ask for.
9. **≥ 60 px between text and images**, visuals at about 90% of their slot. No text on photos: C3 runs question row →
   answer text → guest photo below.
10. **Combine where it reads better.** All sources on one slide (2x2 tiles), not split over two.

## Formats
| Format | Slide recipe |
|---|---|
| **Playbook** (C1) | cover (cutout + headline + small logo + SWIPE →) → premise → RULE n pill + headline + reel card per rule → big real logos for "where AI looks" → caveat → close |
| **Myth vs reality** (C2) | cover with a count equal to the myth slides → per myth: EVERYONE SAYS + struck one-liner over a greyed visual, red ↓, LESLIE SAYS + headline over a vivid visual → close "Which one surprised you?" |
| **Host Q&A** (C3) | cover with host + guest cutouts ("Ricardo asked. / Leslie answered." in Caveat) → per Q: host cutout at the moment he asks + cream speech bubble, then a red LESLIE ANSWERED pill + the answer headline + evidence line, then (≥ 60 px below) the guest cutout at her answer → close |
Close: logo, headline CTA (save / comment / listen), guest cutout, FULL EPISODE + title + the four platform icons
(Apple Podcasts, Spotify, YouTube, Goodpods).

## Tokens and components (CSS in `gen2.py`)
Ground, cream `#fbeee6`, red `#ff4a55`/`#e3262b`, peach `#f2b48c`, glow as `trrs-style`. Montserrat 900 headlines,
each line auto-fitted (PIL) and flagged if under 90 px; Montserrat 700 support 44 px; Caveat 700 for signatures/tags.
Margins 80 px. Content column flex: headline → visual slot (runs under the support line, which sits on a dark band) →
support. Labels 28–32 px tracked. Nothing under 28 px.

## Accuracy (hard)
Everything in “ ” verbatim: run `audit_quotes.py` on the generated slides (`failures: 0`); whitelist a whisper mishear
only if verified by ear before (cite where). Paraphrases unquoted and never stronger than the speaker. Guest stats
attributed in slide and caption. No invented numbers; reused reel UI may carry the reels' invented prices/ratings as
texture, so flag them to the CD. Never show the guest's clients as the negative example.

## Build + export
1. `make_cardsnap.py`: scratch copies of the reel projects without header/captions/tags/outro/audio (junctions to
   assets), then `npx --yes hyperframes@0.8.217 snapshot --at <card times> --no-end` in each, one at a time.
2. `build_visuals.py`: crop/fit/feather the cards and b-roll stills into `assets/img/v/` (grey myth versions).
3. `cut_stills.py`: speaker cutouts at the question/answer moments (`remove-background` + grade/glow).
4. `gen2.py` (helpers + export; the slide copy and v3 layout CSS live in `v3_slides.py`) → `index.html` + `compositions/<c>s<n>.html` (slide k at k-1…k s) + `slides.json`.
5. `npx --yes hyperframes@0.8.217 check` → 0 errors (`line_unread`, `film_silent` expected for stills).
6. `export.py snap` then `export.py deliver`: `TRRS_<SxEyy>_C<n>_slideNN.png`, one PDF per carousel (LinkedIn),
   `TRRS_<SxEyy>_C<n>_contact_sheet.jpg`, 360 px previews in `work/carousels/review/`. Look at every slide full size and
   at 360 px.
7. `output/final/carousels/CAPTIONS.md`: short hook with keywords, the detail the slides dropped, quotes only if verbatim,
   guest stats attributed, host named, "Full episode — link in bio", the four platforms, exactly 2 specific hashtags.
8. `work/carousels/NOTES.md`: quotes shortened, wording changes vs plan, open questions. Log new assets in
   `assets/LICENSES.md`. Superseded versions go to `output/archive/carousels_v<N>/`.
