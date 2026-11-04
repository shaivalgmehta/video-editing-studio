# TRRS S6E15 reel R5: "Bottom funnel bloat" (build notes)

- Project: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r5` (copied from R2 without `.hyperframes/`, `renders/` or R2 media). **Not rendered**; renders are queued centrally.
- Final duration: **51.1 s** at 1080x1920, 30 fps. The A-roll runs 0–48.1 s and the outro (unchanged R2 `outro.html`) runs 48.1–51.1 s.
- Edit details: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r5/EDL.md`. Words: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r5/words.json`, built by `build_words.py`. Captions: `build_captions.py 48.1` writes `compositions/captions.html`.
- Contact sheets: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r5/snaps1/sheet_a.jpg` (full pass, 37 frames; funnel beats there are superseded). Fix passes: `snaps2/` (funnel layout), `snaps3/` (TikTok badge), and **`snaps4/sheet_c.jpg` (funnel with no numbers: 21.8, 27, 31, 34.5, 44.5, 47.6 s)**.

## Script as cut (verbatim, as captioned)
RICARDO: "We've spent so much time in recent years focusing on bottom of the funnel and conversion and performance marketing and driving more dollars into performance marketing."
✂ LESLIE: "Ironically, because Iced Media's roots are as a performance media agency, we're a Meta business partner, a TikTok partner, a Google partner, and I can go on and on. But we actually have a word for that. We call it bottom funnel bloat, where we think all the time we're seeing new prospects come to us and there's an outsized share of their spend going to bottom of funnel conversion media, where they're just paying more to get their existing customers to buy more often. And oftentimes that can result in things like being very promotional, doing sales, and really at the expense of looking and prospecting for new customers."

## EDL (summary)
| reel | source | who | note |
|---|---|---|---|
| 0.000–8.667 | 775.760–784.427 | Ricardo | starts on "we've" (drops "And I know I personally feel that"), ends after "marketing." |
| 8.667–48.100 | 813.860–853.293 | Leslie | one continuous take, no internal cuts |
Voice: −16.0 LUFS, −2.3 dBFS peak, 48 kHz, exactly 48.100 s. The hard cut between speakers is at frame 260.

## Shot list
| reel (s) | shot | words |
|---|---|---|
| 0.00–8.67 | RICARDO, own crop [230,156,680,800]. Name tag 0.2–3.6. Drift, punch on "bottom of the funnel" (3.7), ease back on the second "performance marketing" (7.2) | "we've spent … into performance marketing." |
| 8.67–13.25 | LESLIE (R2 crop). Name tag 8.85–12.25. Punch on "performance media agency" (11.65) | "ironically … media agency," |
| 13.25–17.80 | CARD `partners`: white partner badges with the real Meta, TikTok and Google logos slam in on each name (13.59 / 14.71 / 15.65). Three dashed "+" badges queue up on "go on and on" | "we're a Meta business partner … on and on." |
| 17.80–19.85 | LESLIE, punch on "a word for that" (18.9) | "But we actually have a word for that." |
| 19.85–22.03 | CARD `funnel` A: the funnel builds, with NEW CUSTOMERS on top and 6 customer icons. Coins pour into a red pool at the bottom, which bloats on "bloat". BOTTOM / FUNNEL / BLOAT slams below the captions on each word (20.6 / 21.0 / 21.5) | "We call it bottom funnel bloat," |
| 22.03–26.40 | LESLIE, punch on "new prospects" (24.1) | "where we think all the time … come to us and" |
| 26.40–31.75 | CARD `funnel` B: an AD SPEND bar (NEW CUSTOMERS vs CONVERSION MEDIA end labels, **no numbers**) starts even and tips heavily toward conversion media on "outsized share". The pool swells, the top dims, and CONVERSION MEDIA slams into the pool on "conversion media" (30.5) | "there's an outsized share … conversion media," |
| 31.75–36.95 | CARD `funnel` B2: the same 3 customer icons orbit out of and back into the pool (3 laps). Under "COST PER REPEAT ORDER", a red meter fills with an up-arrow riding its end, and the arrow pulses on each lap (**no figures**). "SAME EXISTING CUSTOMERS" appears on "existing" | "where they're just paying more … buy more often." |
| 36.95–39.40 | LESLIE, punch on "result" (38.3) | "And oftentimes that can result in things like" |
| 39.40–42.00 | CARD `sale`: a phone lock screen (9:41, Tue Nov 3) fills with promo pushes from a fictional "Maison & Co." (FLASH SALE 40% OFF, extra 15% off the cart, 30% off ends at midnight …). A red "40% OFF / SALE" banner slams in on "sales" | "being very promotional, doing sales," |
| 42.00–43.80 | LESLIE, punch on "really at the" (42.7) | "and really at the" |
| 43.80–48.10 | CARD `funnel` C: the top refills, then the 6 new-customer icons vanish one by one to dashed outlines (no counter). A red strike goes through the NEW CUSTOMERS label on "new customers" | "expense of looking and prospecting for new customers." |
| 48.10–51.10 | OUTRO (R2, unchanged; shing at 47.77) | — |

The logo header is hidden over every card (BROLL list in `header.html`). Captions stay on over the cards at y 1290. The card layouts keep that band clear.

Sound: voice at 1.0. Music "Close Up" from media 9.2 s at 0.2, so the groove arrives around 9.1 s, just as Leslie comes in. The outro bed is at 0.55 (media 57.3). Whooshes on the card cuts (13.1, 19.7, 26.25, 39.25, 43.65), clicks on the three badge slams and the SALE banner, a low impact on "bloat" (21.5, 0.22), and the shing at 47.77.

## Sources and licences (also in `assets/LICENSES.md`)
- Partner logos come from Wikimedia Commons:
  - `Meta Platforms Inc. logo.svg` (PD, trademarked)
  - `Tiktok logo text.svg` (PD, trademarked)
  - `Tiktok icon.svg` (CC0 path, which the card draws in TikTok's cyan / red / white layers)
  - `Google 2015 logo.svg` (PD, trademarked)
  
  They are saved as PNGs in `assets/img/partners/`, with the SVGs kept alongside. Scripts are in `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r5/logos/`.
- No stock footage. Every card is HTML. The sale UI brand is fictional, not an Iced Media client or any real retailer.
- Music, SFX and fonts are R2's (Mixkit / Pixabay / Google Fonts OFL), already logged.
- Considered but not used: Mixkit 18264 "Man making a transaction on his smartphone with his card" (licence checked: Mixkit Stock Video Free License, `videoFree`). It is a possible cut-in for "to buy more often" (35.3–36.9) if the CD wants one real-footage beat. Rejected because their pages are marked "Mixkit Restricted License": 48216 (SALE letters on a rope), 47923 (writing SALE on a tag), 21325, 23475.

## Open questions for the CD
1. **Ricardo's headroom.** His crop has to start at y=156 to clear the burned-in title box, so the top of his hair touches the window's top line. To get more headroom I'd have to show the title box corner or shrink him. OK as is?
2. **Ricardo backchannels under Leslie.** "Yeah" (~17.0, "go on and on"), "Okay" (~22.0, "bloat, where") and "Right, right" (~31.4, "media, where") overlap her words in the mixed track, so they can't be cut cleanly. They're quiet. The alternative is to drop "where we think" (22.0–23.0), which would also take out the "Okay", but that cut would be a visible jump on Leslie.
3. **"where we think all the time".** Your script elided "we think". I kept it because it's said and there's no clean gap to cut it. It's captioned as said.
4. **Partner badge wording.** The badges read "Meta / Business Partner", "TikTok / Partner", "Google / Partner", which is her wording, on our own white tiles. They are not the platforms' official badge artwork, which we don't have. Fine, or should they be logos only?
5. ~~Numbers on the cards~~: resolved per the coordinator. There are no invented statistics. The spend bar has no percentages, the cost indicator is a non-numeric meter and arrow, and the new-customer counter is gone.
6. ~~Title slam~~: resolved. The BOTTOM FUNNEL BLOAT word slam is back in window A (the coordinator OK'd it), and the spend bar now first appears in window B.

## Check status
`hyperframes@0.8.217 check` (final, after the no-numbers fix): **0 errors**. Runtime, layout, motion, contrast and audio all pass. The remaining warnings are deliberate:
- `timeline_track_too_dense` on captions.html. R2 has the same caption generator.
- `line_unread` on the sale pushes. The pile-up is meant to be skimmed, not read.
- `line_unread` on the outro. That's R2's unchanged outro.
- `text_below_floor`: I raised the 26/27 px labels to 28 px afterwards. The other sub-28 px text is the notification body copy, which is deliberately phone-UI scale.

The first check run hit a timeout under machine load. A rerun after the fixes completed cleanly.
