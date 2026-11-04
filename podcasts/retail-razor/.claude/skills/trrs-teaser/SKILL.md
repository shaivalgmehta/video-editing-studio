---
name: trrs-teaser
description: Build The Retail Razor Show 16:9 episode teaser (~60 s, "reveal the promise, protect the payoff") from templates/teaser, following the approved S6E15 teaser v5 recipe (Anatomy-of-a-Dream grammar in the TRRS warm brand). Use when the CD asks for a TRRS teaser, trailer or promo for an episode.
---

# TRRS teaser (16:9)

The teaser rules ("Reveal the promise. Protect the payoff.", beat selection, what to withhold) are in the L2 skill
`podcast-teaser`. This skill is the TRRS recipe. Read `trrs-style` and `podcasts/retail-razor/CLAUDE.md` first.

**Approved reference: S6E15 teaser v5** (`episodes/S6E15_leslie-ann-hall/output/final/teaser/TRRS_S6E15_teaser_16x9_v5.mp4`).
The project `episodes/S6E15_leslie-ann-hall/work/hyperframes/teaser` was left at its v7 state. Notes and files show that
**v6 and v7 changed only the music**, and both were **unapproved explorations**:
- v6: a "mystery" bed from Mixkit 548 with hits re-tuned to C#, built with `duck_v6.sh`
- v7: Mixkit 550 "Falling Inversus" stems arranged to the reference's music grammar, with a gentle duck (ratio 1.5),
  built with `duck_v7.sh`, `music4_work/REFERENCE_MUSIC.md` and the `*_v7.wav` files

Don't treat them as part of the recipe. File history can't prove nothing visual changed after v5 (there is no git, and
`captions.html` was modified later on 10-30), so compare snapshots against the v5 mp4 before reusing a beat.

Supporting S6E15 files:
- `work/episode/CHECKPOINT_1.md` (beat sheet)
- `work/episode/EDL.md` (crops and segments)
- `work/episode/build_captions.py`
- `work/episode/duck.sh` (the v5 duck)

Style reference: `_shared/references/Anatomy of a dream.mp4`.

## Recipe (v5)
- **Format:** 1920x1080, 30 fps, about 60 s.
  - The A-roll is ONE pre-cut file with crops baked in from the finished episode (lanczos + light unsharp).
  - Black in the title gap (3 s) and the end gap.
  - Crops must stay inside the clean window of the source frame. S6E15: x 80–1835, y 185–990, avoiding the logo and
    "Recorded live" boxes.
  - Crop types (S6E15 values, re-measure every episode): WIDE [230,185,1440,810], guest MED [870,185,960,540],
    guest CU [1060,185,736,414], host MED [110,185,960,540], host CU [250,185,736,414].
- **Structure:**
  | Beat | Time | What |
  |---|---|---|
  | HOOK | 0–4.9 | cold open on the guest's boldest line, guest CU |
  | HOST | 4.9–9.5 | the host's framing question (MED → WIDE reveal) |
  | TITLE | 9.5–12.5 | the client's **video cover used exactly as supplied**, slammed in on the music drop with a slow push |
  | BODY | 12.5–~53 | 5–7 one-line verbatim beats (≈4–9 s each), each with a graphic that EXPLAINS the line |
  | CUT-OFF | ~53–55.5 | a line that stops mid-sentence so the payoff stays hidden (S6E15: "So the number one thing that we encourage is…") |
  | END CARD | ~55.8–60 | see below |
- **Graphics** (text on the side away from the speaker, over a brown side scrim):
  - kinetic type: peach tracked lead-in label, red bar, then a HUGE Montserrat 900 key word slammed in on the word
    (scale 1.4→1, blur 16→0, 0.24 s expo.out)
  - handwritten names (Caveat Brush) writing on with a drawn arrow to each person, **both hosts named** when present
  - Caveat Brush "X → Y" write-ons
  - argument graphics, e.g. S6E15's SEO→GEO legacy-vs-indie split, "200 products" counter collapsing to hero products,
    a swelling funnel, a search bar typing the guest's questions, a Reddit "final check" card, platform/client logos
    instead of text
  - search cards name rivals generically ("Competitor"). No invented numbers.
- **Transitions:** whip pans between sections (out 0.16 s power3.in, in 0.3 s power3.out, x ±260, scale 1.3) with a
  0.2 s **B&W flash** frame. Red/cream bar **glitch bursts** (0.24 s) plus `glitch.wav` on the big seams. A slow
  lateral pan drift on every talking stretch, alternating direction.
- **Camera:** eased zooms on the baked crops: creep, then slam in (0.3 s expo.out) on the key word, pull out to reveal,
  and a slow push into the cut-off.
- **Captions:** continuous spoken-word captions (`trrs-style`), never spanning a cut, ending on "…".
- **End card:**
  - logo
  - a three-line question headline with a red "?" (S6E15: "CAN SMALL BRANDS / BEAT THE GIANTS / IN AI SEARCH?")
  - a sub line ("<Guest> reveals what it takes to compete.")
  - the release date in red ("TUESDAY, NOVEMBER 3rd")
  - "Watch on" with Apple Podcasts / Spotify / YouTube / Goodpods
  - the guest cutout on the right
- **Sound (v5):** voice.wav at -16 LUFS. A music bed (S6E15 v5: Mixkit 370 "Sparta", edited to the timeline with
  bar-line splices and a drop at the title) is ducked by `tools/duck.sh`, whose defaults are the v5 settings: volume
  0.62, threshold 0.05, ratio 4, attack 20, release 200. Hits and risers go in a separate **un-ducked** `hits.wav`.
  SFX: whoosh + glitch into the host and title, glitch on seams, type under typing, click on counters.
  - The CD confirmed (2026-11-02) the approved teaser keeps Sparta; the v6/v7 music explorations were not adopted.

## Steps
1. **Beat sheet first** (checkpoint for the CD), as in `CHECKPOINT_1.md`. List:
   - the reference moves you'll borrow
   - the brand mapping
   - the beats table: time, verbatim line, speaker, source time, visual
   - what is withheld on purpose

   Every line must be found in `ep_words.json` (search, don't trust show-notes times).
2. **EDL** (`work/episode/EDL.md`): crops verified on real frames, then the segment table (master in–out, source
   in–out, words, shot). Render `aroll.mp4` (black gaps included) and `voice.wav` at exactly 60.000 s.
3. Copy `templates/teaser` → `work/hyperframes/teaser`. Drop in the media (README lists the files).
4. Captions: `tools/build_captions.py --words ... --cuts "<every segment boundary>" --fix fixes.json --cutoff-end <t>`.
   Put ASR→verbatim fixes in `fixes.json` (S6E15 needed "Iced Media", "Redditors", "in the whole").
5. Scenes: one composition per beat. Copy `hook.html` / `host.html` / `handwrite.html` and give each a unique id
   (file name = composition id = host id). Set `glitch.html` seams, endcard variables, and the camera and
   `SEGS` / `WHIPS` lists in `index.html`. Add one B&W flash `<video>` per whip.
6. Music: cut the bed to the beat map (drop on the title, stops and booms on key words), then
   `sh tools/duck.sh music.wav voice.wav music_ducked.wav 60`. Hits go in `hits.wav`. Check the summed peak; it may
   need a final limiter.
7. QA: `check` (0 errors; the 26 px host role and 22 px platform labels are the accepted v5 warnings), snapshot every
   beat, then a central render and loudness levelling to `output/final/teaser/TRRS_<SxEyy>_teaser_16x9_v<N>.mp4`.

## CD notes that shaped v1→v5
- v2: media-kit system tried, then reverted to the warm look while keeping v2's features:
  - always show the logo with "Cutting through the clutter"
  - both hosts named
  - logos instead of text
  - continuous captions
  - graphics that explain rather than decorate
  - lighter grade
  - more eased zooms
- v3–v5:
  - the supplied video cover used exactly for the title
  - Caveat Brush handwriting
  - whip pans and B&W flashes between sections
  - a single "Legacy brand" row
  - search cards say "Competitor"
