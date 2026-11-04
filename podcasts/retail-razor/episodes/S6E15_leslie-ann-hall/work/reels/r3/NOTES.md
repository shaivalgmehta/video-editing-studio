# TRRS S6E15 reel R3: "AI search is a mirror for your brand" (build notes)

## v2 (2026-11-02): CD fix, "as the foundation that…" was cut off at ~13 s
- **What was wrong:** v1 removed source 429.67–430.56, believing the quieter voiced sound at 429.66–430.12 was Ricardo's "Okay" (the burned episode captions read "that- Okay"). It is actually Leslie's own drawn-out "that". Her "foundation" runs to 429.64, and the dip at 429.38 is the stop inside "-tion". So v1 dropped "that" and jumped from "foundation" straight to "drives". The caption still said "that".
- **Fix:** v1 segments 1 and 2 are merged back into one continuous take (415.370–448.627). Her 0.5 s pause before "drives" is natural and kept. Nothing else in the cut changed: "does not continuity" stays out, and the first quote still ends on "best answer."
- **Re-timed:** aroll, voice, words.json and captions were rebuilt.
  - Every shot, card, camera key, sfx and the header hide windows after reel 14.3 move **+0.900 s**. The outro is now 59.3–62.3, with the shing at 58.97 and the music-out clip at media 68.5.
  - The found card is now 9.3–21.5 (12.2 s). Its beats land on the new word times: "foundation" 13.65 → slab drops (T_FOUND 4.35); "drives" 15.25 → wires and tiles (5.95, click at 15.25); "channels" 18.93 (9.64); "across the entire ecosystem" 19.39 → glow (10.10).
  - Other cards now sit at: mirror 24.6–28.1, crack 31.9–37.033, teams 43.2–54.067, align 55.85–59.3. Their local cues are unchanged because they are relative to each card.
- **Verified:** a fresh small.en pass over reel 9–22.5 reads "…share of answers as the foundation that drives all of their marketing tactics [in] channel across the entire ecosystem because really". That matches words.json.
  - voice.wav: 59.300 s, −16.0 LUFS, −2.3 dBFS.
  - aroll: 1779 frames.
  - `check`: ok true, 0 errors.
- **New duration: 62.3 s** (A-roll 59.3 + outro 3). Snapshots of the changed region are in `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/snaps_v2/`, with the sheet at `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/sheet_v2.jpg`.
- In the v1 shot list below, times after 14.3 s are v1 times; add 0.9 s.

Project: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r3` (copied from trrs_r2 without `.hyperframes/`, `renders/`, `assets/video/`, `assets/broll/` or `voice.wav`; R2's `rank.html` moved out to `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/tmp/rank_r2.html`).
**Not rendered**, as the brief asks. It is ready for the central render queue.

- Final duration **61.4 s**: A-roll 0–58.4, outro 58.4–61.4. 1080x1920, 30 fps.
- A-roll: `assets/video/aroll.mp4` (1752 frames, full 1920x1080, no audio). Voice: `assets/audio/voice.wav` (48 kHz, 24-bit mono, 58.400 s, −16.0 LUFS, −2.3 dBFS peak).
- Words: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/words.json` (132 words, cut-relative, verified against the final voice with a small.en re-transcription). Source-time version: `words_src.json`.
- Scripts: `build_aroll.py` (cut, clean, words), `build_captions.py` (repointed; KEY = mirror, foundation, consistent, same, GEO, LLMs), `mk_teams.py` (teams/align cards from `cues.json`).
- `npx hyperframes@0.8.217 check --json`: **ok: true**, with 0 errors in lint, runtime, layout, motion and audio. The craft warnings are small UI copy inside the mock screens: below the 28 px type floor, and on screen for less than full read time. That copy is texture you glance at, not a line to read; the captions carry the message. The outro's read-time warnings are the same as R2's. Lint has 0 errors. The only warnings are the three caption-track-density ones, which R2 also has. Intended overlaps are marked: `#cam` overflow, and occlusion while the answer rows swap. Contrast warnings are only on small grey UI text inside the mock screens (true to real UIs) and on the peach role line of the name tag (same as R2).

## Spoken script (verbatim, as captioned)
> Instead of thinking of AI search, GEO, LLMs as a channel, we really encourage our clients to think about ranking in AI search and increasing their share of answers as the foundation that drives all of their marketing tactics and channels across the entire ecosystem. Because really, AI search is a mirror for what the world thinks about your brand. And if your overall communication strategy is not consistent, it's going to be harder to come up as the best answer.
> ✂ For large corporations, it can be a lot more challenging to make sure that the organic team, the paid team, the PR team, the team that's merchandising your e-commerce website, the team that's responsible for Amazon PDPs, are all making sure that they're prioritizing the same products and the same messages.

She says "ranking **in** AI search". Three passes (ep_words, medium.en, small.en) all hear "in".

## EDL (full detail in `EDL.md`)
| # | source | reel | content |
|---|---|---|---|
| 1 | 415.370–429.670 | 0.000–14.300 | "Instead of thinking…" → "as the foundation that" |
| 2 | 430.560–448.627 | 14.300–32.367 | "drives all of their…" → "is not consistent," |
| 3 | 450.400–454.167 | 32.367–36.133 | "it's going to be harder to come up as the best answer." |
| 4 | 674.060–676.360 | 36.133–38.433 | "For large corporations," |
| 5 | 676.660–691.393 | 38.433–53.167 | "it can be a lot more challenging…" → "for Amazon PDPs," |
| 6 | 691.620–696.853 | 53.167–58.400 | "are all making sure… the same messages." |

The audio joins are 15 ms equal-power crossfades centred on the video cut. Cuts removed:
- Ricardo's "Okay" (gap at 429.7–430.6)
- "does not continuity," (see Q1)
- a 0.3 s breath (hidden by a punch-in at 38.43)
- a silence after "PDPs"

## Shot list (reel seconds)
| time | shot | what moves on which word |
|---|---|---|
| 0.00–4.70 | Leslie (name tag 0.2–3.6) | Opens on a 1.14→1.03 settle, then a punch-in on "GEO, LLMs" (3.0) |
| 4.70–6.05 | **chan** card | Six channel tiles (Paid, Social, PR, Amazon, Website, Creators). "AI Search" drops in as just one more tile on "channel" (5.23) |
| 6.05–9.30 | Leslie | Punch-in on "encourage" |
| 9.30–20.60 | **found** card | A generic AI-chat answer (no product branding): "Best moisturizer for dry skin?" with four ranked picks and source chips. "Your Brand / Hydra Barrier Cream" climbs from #3 to #1 on "ranking in AI search". The share-of-answers meter fills 18→62% on "share of answers" (11.63). On "foundation" (13.49) the answer card crops to a full-width slab and drops to the base. On "drives" (14.36) red wires rise and the six channel tiles land on top of it in turn, finishing by "channels" (18.04). On "across the entire ecosystem" every tile and the slab light red |
| 20.60–23.70 | Leslie | Slow drift, then a hard punch 1.06→1.26 on "**mirror**" (23.25) |
| 23.70–27.20 | **mirror** card | "What the world thinks": a Reddit-style post (r/SkincareAddiction), a 5★ verified review, a short-video creator post (real Mixkit footage) and a press clipping ("Beauty Weekly: the 10 best moisturizers of 2026") land above a silver mirror line. Their reflection falls onto the AI answer card below. On "your brand" each source pulses and lights its numbered citation [1]–[4] on your #1 answer |
| 27.20–31.00 | Leslie | Punch-in on "communication strategy" |
| 31.00–36.13 | **crack** card | On "not consistent" every source flips to a contradicting story: "is Hydra for *oily* skin now??", 2★ "Not what the ad promised", "#ad NEW Glow Serum 30% off", "Your Brand pivots to anti-aging serums". The citations turn red. The mirror then cracks with a shake and glitch sfx (32.0). On "harder to come up" (33.1) your brand slides from #1 to #4 and greys out, and on "best answer" (35.0) a competitor gets the BEST ANSWER badge |
| 36.13–42.30 | Leslie | Hard cut to her face, a punch at 38.43 (hides the jump cut), and an expo punch on "challenging" |
| 42.30–53.17 | **teams** card | Five team cards, scattered at different angles, each pushing a different product and message in its real UI: Organic = search result "10 Tips to Control Oily Skin" (green gel). Paid = sponsored ad "Glow Serum: 30% off" (purple serum). PR = press release "Your Brand Launches Night Repair Oil". E-commerce = storefront hero "NEW Vitamin C Drops". Amazon = Amazon-style PDP for "Daily Sunscreen SPF 50" with stars, price, "#1 Best Seller" and a yellow Add to Cart button. Each card lights exactly as she names it: organic 42.87, paid 44.27, PR 45.43, merchandising 47.29, Amazon 51.49 |
| 53.17–54.95 | Leslie | Punch-in on "are all making sure that they're" |
| 54.95–58.40 | **align** card | On "same products" (56.13) all five flip to ONE product, Hydra Barrier Cream (red-lid jar), with ONE message, "72-hr hydration for dry skin". The label becomes "One product. One message." On "same messages" (57.3–57.75) the cards straighten into one column, a red spine wires them together and each gets a red check |
| 58.40–61.40 | outro (unchanged) | "AI Search Is a Mirror for Your Brand", shing at 58.07 |

The Retail Razor logo (header) is hidden during every full-screen card. Captions (word-synced, ≤3 words) sit at y 1290 on every shot. All card content stays above y 1250, so nothing collides with them.

## Sound
- Music: "Close Up" bed at 0.2 (media 9.2→, groove lands around the found card) and the outro clip at 0.55 (media 67.6, continuous).
- Whooshes on card cuts in: 4.58, 9.18, 23.58 (whoosh2), 30.88, 33.10 (soft, on the slide), 42.18, 54.83.
- Soft clicks:
  - rank and meter: 10.0, 11.63, 14.45
  - citations: 25.4
  - each team named: 42.87, 44.27, 45.43, 47.29, 51.49
  - align: 56.13, 57.60
- Glitch on the crack at 32.0. Shing at 58.07.

## B-roll and assets (logged in `assets/LICENSES.md`)
- `broll/creator_tt.mp4`: Mixkit 50417, "A woman shows how to use a moisturizing skincare product". The page was checked: Mixkit Stock Video Free License, not Restricted. It is cropped to portrait and used inside the short-video post on the mirror and crack cards.
- Everything else (AI answer, Reddit-style post, review, press clipping, search result, social ad, press release, storefront, Amazon-style PDP, product packshots) is drawn in HTML/CSS. There are no real logos and no Iced Media clients; all brand and product names are invented. "r/SkincareAddiction" is a real public subreddit name.
- Mixkit 50426 (cream on face, Free License) was downloaded but not used (kept in tmp). Mixkit 33201 was rejected (Restricted).

## Contact sheets
- `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/sheet1.jpg`: 0.3–30.0 s. The found frames at 14.0–20.4 in this sheet are from **before** the slab fix (the card was shrunk to 56%). The current look is in sheet2 at 14.6, 17.5 and 20.0.
- `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/sheet2.jpg`: 14.6–60.8 s (found after the fix, crack, face, teams, align, outro).
- Raw frames: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/snaps1/`, `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r3/snaps2/`.

## Open questions for the CD
1. **"does not have continuity"**: on the audio she says "does not continuity" (the "have" is not there; ep_words, medium.en and small.en all agree). Per the rules I cut that clause, so the line is "…is not consistent, it's going to be harder to come up as the best answer." Should we keep it out, or put it back captioned exactly as spoken ("does not continuity")?
2. **Ricardo backchannels I could not remove**:
   - an "I see / Yeah" under "tactics and channels across" (≈18.0–18.6). Whisper even hears "in channel" there; I captioned "and channels", per the show notes.
   - a possible "Yeah" under the end of "paid team" (≈44.9).

   Both overlap her words. Do they sound OK to you?
3. **The end of the first quote**: the cut lands on "best answer." (her sentence actually continues "…for the products brands have the right to win."). There is a 0.12 s gap, so it sounds clean on the waveform, but please listen to the join at 36.13. Alternative: keep "…for the products brands have the right to win." (+2.7 s, 64 s total).
4. The reel opens on "Instead of thinking…". Her real sentence starts "But instead…", and the "but" is cut off at a 20 ms dip. Whisper still "hears" a "But" even when the clip starts well inside "Instead", so please give the first word a listen.
5. **Caption legibility at 36.1–38.4** ("FOR LARGE CORPORATIONS,"): in segment 4 she leans forward, so the caption line sits over the white sofa. It is readable but weaker than elsewhere. A 1.15 punch on that shot would put her darker jacket behind it. Want that?
6. Fictional brand naming: the mock UIs say "Your Brand" and "Hydra Barrier Cream", plus invented competitors (Halden Skin, Brightwell, Mira Botanics) and an invented outlet (Beauty Weekly). Fine, or would you prefer one invented brand name used throughout?
