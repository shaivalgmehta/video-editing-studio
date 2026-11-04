# TRRS S6E15 reel R4: "200 products" / Leslie's three rules for winning in AI search

Project: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r4` (copied from R2, same style kit). NOT rendered (renders are queued centrally).
**v2 (after CD review of v1): final duration 51.867 s** = 48.867 s A-roll (1466 frames @ 30 fps: 46.867 s speech + 2.0 s held frame / silence under the final card) + 3 s outro (unchanged `outro.html`).

### v2 change: final "all three rules" card
The CD's one fix: step 3 never showed as ticked. Now:
- **45.60-46.10** Leslie "and": punch-in on the cut, 1.06 to 1.18 (shortened final face shot).
- **46.10-48.867** final checklist card (the rules scene, 4th window; logo hidden). It opens on "machines" (46.13).
  - Row 03 fills "Humans AND machines / Understood by both" (title 44px so it clears the tick) (same fill motion as rules 1-2) at 46.25.
  - The tick lands at 46.50, with a click at 46.50.
  - All three ticks and the RULE 3 chip pulse together at 47.05.
  - The card holds, fully built, until 48.867: about 2.4 s after the tick, about 2.3 s after her last word (machines ends ~46.58).
- **48.867-51.867** outro (unchanged). Shing at 48.537. music-out at 48.867 from media 59.448, still a groove bar line, because the bed's media-start moved 10.29 to 10.581.
- Header BROLL list adds [46.10, 48.867]. Captions, header and voice tracks run to 48.867. voice.wav is padded with digital silence to 2,345,600 samples. aroll.mp4 is the v1 file plus a 60-frame held last frame (concat, no re-encode of the speech).
- Shot list below is v1; S15 is now 45.60-46.10 and the new S16 card is 46.10-48.867.


## EDL (full detail in `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r4/EDL.md`)
| # | source in | source out | reel | words |
|---|---|---|---|---|
| 1 | 502.090 | 548.957 | 0.000-46.867 | "Oftentimes brands will come to us..." to "...both humans and machines." |

- One continuous take, no internal cuts (all pauses < 0.4 s). Bracketed clause "to a diverse group of customers across the entire ecosystem" is **kept**: "message" runs straight into "to", so there's no clean cut point.
- Ricardo's "For all of them, yeah." (reel 7.56-8.47) is kept per script and shown as a reaction cut.
- **Ricardo's "Okay" backchannel removed**: at reel 18.50-18.97 (episode 520.6-521.1), in the gap between "hero products" and "you really have". Pitch tracking confirms it's his voice (~95 Hz against her ~220 Hz). It's pulled down 30 dB with 15 ms ramps, so the length doesn't change (pre-mute copy: `tmp/voice_pre_okay_mute.wav`). The grid card is on screen, so no lips are visible.
- voice.wav: -16.1 LUFS, -2.3 dBTP, 48 kHz, 2,249,600 samples (= the video length exactly).
- words.json: 118 words, checked against a fresh faster-whisper medium.en pass on the final voice.wav (118/118 aligned, mean start difference 0.06 s). There are 3 text calls where the transcripts disagree, all decided by the episode's own burned captions:
  - "wanna" (Whisper hears "want to").
  - "and getting": the "and" is a short unstressed syllable at 28.80; Whisper drops it.
  - The show's captions have "that you really", but there is no Leslie "that" in the audio. The sound there is Ricardo's "Okay", so "that" is dropped from the captions.

## Shot list (reel time)
| # | time | shot | notes |
|---|---|---|---|
| S1 | 0.00-3.95 | Leslie (R2 framing) | name tag 0.4-3.6; slow drift, **punch-in on "200"** (3.40) |
| S2 | 3.95-7.55 | GRID card, full screen | 200 beauty-product tiles pop in on "products", with a counter running 0 to 200. Every tile has a small red rank arrow that bobs, and all of them push up on "rank for everything" |
| S3 | 7.55-9.45 | Ricardo reaction (own crop) | "For all of them, yeah" + Leslie's "But the truth is," over him; Ricardo name tag 7.6-9.45 |
| S4 | 9.45-10.95 | Leslie | **punch-in on "deserve"** (10.20) |
| S5 | 10.95-12.05 | GRID | "rank for everything": 195 tiles fall and dim, counter drops 200 to 5, 5 survivors stay lit |
| S6 | 12.05-14.25 | RULES card | "WINNING IN AI SEARCH" + red "RULE 1" chip; it pulses on "number one", with 3 checklist rows (01 lit, 02/03 empty) |
| S7 | 14.25-17.85 | Leslie | drift, **punch-in on "hero"** (17.50) |
| S8 | 17.85-21.60 | GRID | "hero products": the 5 survivors lift into a centred row at 2x with a red glow, label "HERO PRODUCTS" / counter "5"; their arrows climb on "right to rank" |
| S9 | 21.60-24.20 | RULES card | Row 01 fills "Hero products / The right to rank" with a tick, then the counter rolls to RULE 2 on "second" |
| S10 | 24.20-29.90 | Leslie | punch on "holistically", eases back out on "strategy" |
| S11 | 29.90-35.20 | SILOS card | label "SILOED TEAMS", then "TEAMS ON BOARD" from "on board". 4 team silos (BRAND / E-COM / SOCIAL / SEARCH), each with its own message. On "siloed teams" the messages wobble out of sync; on "on board" the walls fade and one red frame takes in all four; on "work together" the columns close ranks; on "same message" the four messages collapse into a single red "One message" bar wired to every team |
| S12 | 35.20-40.20 | Leslie | "to a diverse group of customers across the entire ecosystem", punch on "ecosystem" |
| S13 | 40.20-42.10 | RULES card | Row 02 fills "One message / Siloed teams, together" with a tick, then the counter rolls to RULE 3 on "third"; row 03 lit |
| S14 | 42.10-45.60 | SPLIT, full screen | **Top:** a real shopper's hands scrolling a real Amazon product page on her phone (Mixkit 42136), "HUMAN VIEW" chip. **Bottom:** "CRAWLER VIEW", the same product as schema.org Product JSON-LD in a `<script type="application/ld+json">` block (UV Sanitizer Box, Offer 59.99 to match the $59.99 on the phone, InStock). The JSON-LD types in on "content" and a scan line reads it on "understood", highlighting @type, name, price and availability. The human chip lights on "humans", the crawler chip on "and" |
| S15 | 45.60-46.867 | Leslie | **punch-in on "machines"** (46.10) |
| Outro | 46.867-49.867 | `outro.html` unchanged | shing at 46.537 |

- The logo is hidden over every full-screen card (header BROLL list: 3.95-7.55, 10.95-14.25, 17.85-24.20, 29.90-35.20, 40.20-45.60).
- Caption KEY (red) words: 200, deserve, hero, holistically, siloed, message, humans, machines.
- Sound: music bed "Close Up" at 0.2 from media 10.29, so the outro clip (0.55, media 57.157) starts on a groove bar line. Whooshes on the grid in (3.82), the hero lift (17.75) and the split (41.98). Clicks on "one", "second", "same message" and "third".

## B-roll / assets and licences (all logged in `assets/LICENSES.md`)
- `broll/human_pdp.mp4`: Mixkit 42136 "Woman exploring an online sales page on her cell phone", https://mixkit.co/free-stock-video/woman-exploring-an-online-sales-page-on-her-cell-phone-42136/. **Mixkit Stock Video Free License** (page checked 2026-11-02, not "Restricted"). Vertical 1080x1920 native.
- Everything else is drawn in HTML/SVG: generic bottle/tube/jar/lipstick silhouettes (no brands), the rule checklist, the silos and the JSON-LD panel. Music, sfx and fonts carry over from R2.
- No Iced Media clients appear anywhere.

## Checks
- `npx hyperframes@0.8.217 check --json`: **ok: true**, with 0 errors. What's left is warnings only:
  - "track too dense" in captions.html (inherited from R2's caption builder).
  - #cam/#camR overflow (intended: punch-in crops inside the window).
  - The outro lines' read time (outro.html is unchanged by brief).
  - A WebGL ReadPixels console note.
- On an earlier run, under heavy machine load from other agents' jobs, the check timed out ("no progress for 120 s"). It passed cleanly on the re-run.
- Snapshots looked at for every shot change: `snaps1/` (1.5-10.4 s), `snaps2/` (11.6-31.8 s), `snaps3/` (34.9-48 s + `contact-sheet.jpg`), `snaps4/` (re-check: bigger rank arrows, split fixes), `snaps5/` (silo label, crawler chip).
- Fixes from review:
  - Bigger rank arrows on the tiles.
  - The CRAWLER VIEW chip moved off the caption band.
  - The JSON-LD price and name now match the phone ($59.99, UV sanitizer box).
  - The silo label swaps "Siloed teams" to "Teams on board" on "on board", so it's on screen long enough to read.
- The final 590 px nudge of the crawler chip (to keep it inside action-safe) came after the last snapshot.

## Open questions for the CD
1. **Ricardo's name tag** sits on a 1.9 s reaction shot, his only appearance, so it is up for 1.9 s, not ~3 s. OK, or drop his tag in this reel?
2. **"Okay" removal**: Ricardo's "Okay" (reel ~18.6) was muted in the gap. The episode's burned captions read "that you really", but the audio has no "that" from Leslie, so the captions read "products / you really have". Please listen to 17.8-19.2 s.
3. **Human view footage** shows a real Amazon PDP for a UV phone sanitizer, not a beauty product. The JSON-LD matches that product (same page, as briefed). If you want it beauty-specific, I can swap the top half for a recreated beauty PDP in HTML (that loses the real human).
4. **The bracketed clause is kept** (adds 4.6 s; 49.9 s total). Dropping it isn't clean: "message" runs straight into "to" with no pause.
5. The card labels "WINNING IN AI SEARCH", "SILOED TEAMS" / "TEAMS ON BOARD", "HERO PRODUCTS", "HUMAN VIEW" / "CRAWLER VIEW" are small peach labels in the rank.html style, not headlines. Keep or strip?
6. The silo team names (BRAND / E-COM / SOCIAL / SEARCH) and their example messages ("Clean beauty", "20% off today", "Viral glow hack", "Best serum") are my illustration. Leslie doesn't name the teams.
