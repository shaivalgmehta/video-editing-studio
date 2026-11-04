---
name: ad-edit
description: General procedure for editing a paid social video ad (Meta Reels/Stories/Feed, also TikTok/Shorts) from talking-head or UGC footage - hook in the first second, captions for muted viewing, 9:16 master + 4:5 crop, SRT, thumbnail, ad-policy checks and QA. Use for any ad job under ads/; if the client has its own skill (e.g. `<client>-ad`), follow that and use this for the general rules it doesn't cover.
---

# Editing a paid social ad

Client-neutral. L1 skills cover the mechanics: `video-edit-core` (audio cleanup, transcription, cutting, captions, HyperFrames), `video-qa-delivery` (checks, loudness, naming, archive), `stock-sourcing` (licensed B-roll and music). Read the client's `CLAUDE.md` before starting; its standing decisions override this.

## 1. Set up

- Job folder `ads/<client>/projects/<YYYY-MM_slug>/` with `input/ work/ output/final/ output/archive/`; footage and brief into `input/` (read-only).
- Read the brief for: audience (cold vs retargeting), placement, CTA button, landing page, claims that need proof. List open questions to the CD in one short message.
- Copy the client's HyperFrames template (`ads/<client>/templates/`) into `work/hyperframes/<ad>/`, if one exists.

## 2. Audio and words

- Clean the voice (denoise chain that keeps every word; verify by transcript against the raw: no word may change). Never generative "enhance" models that can rewrite speech.
- Word-timed transcript of the clean audio; cross-check with a second ASR. Note flubs, restarts, unclear words → cut the sentence or flag a pickup.

## 3. Cut (A-roll)

- Cut points from a silence map, not from ASR word times. Gaps 0.15–0.25 s, one deliberate ~0.45 s beat at the turn, ≤0.15 s before list items, a pause + punch-in before the reveal/offer.
- Open on motion (walk-in, gesture, B-roll) with the hook text from frame 1. The first spoken word should land inside ~1–2 s.
- Alternate 100% / ~115% punch-ins per segment (anchored to keep the face in the upper safe band), 10 ms audio crossfades, conform to 30 fps. Check every cut frame for blinks.
- Checkpoint: 540p proxy + EDL with the judgment calls listed.

## 4. Graphics (HyperFrames)

- **Hook bar** on frame 1, inside the safe band, not over the eyes (snapshot the hook beats first).
- **Captions**: 2–4 words per group, ≤2 lines, high-contrast pill or shadow, active-word highlight, hard cut between groups, bottom of the pill at ~65% height. Verbatim to the audio; only spelling fixes (brand names, US/UK per brief).
- On-screen text carries the argument muted: list items, the offer, the CTA. Each graphic shows what is being said at that moment.
- Reduce talking-head time in the middle (picture-in-picture or cutaways) if the CD prefers; keep the face for hook and close.
- End card ≥3 s: logo, one headline, one button matching the ad's CTA, optional sub-line; still for the last second.
- Gate: `npx --yes hyperframes@0.8.217 check` at 0 errors, snapshot every beat, look at the frames. Checkpoint: full-res review render.

## 5. Finish

- Music bed low (≈ −26 dB under voice, sidechain-ducked), lift on the end card, fade out. Licensed for paid ads, logged.
- Export the 9:16 master, then the 4:5 as a crop of the same mix (1080×1350, choose the y offset so captions and hook survive; check frames of both).
- SRT from the caption groups (same text, same timing). Thumbnail = a frame with the hook bar and a good face, usually 1–2 s in.
- Measure: integrated loudness and true peak, last-second stillness of the end card, gaps >0.4 s in the voice, caption spelling of the brand.

## 6. Ad-policy pass (before delivery)

Check every on-screen line and spoken claim:
- Provable? (numbers, guarantees, results, turnaround, "unlimited", "best") → needs the client's sign-off in writing, else flag.
- No invented stats, testimonials or logos; no fake UI elements (play buttons, notifications, cursor "click here").
- No personal-attribute targeting language ("Are you overweight?", "your debt"), no sensational before/after.
- Third-party logos/people visible in screenshots → client must confirm permission (or their standing decision covers it).
- Music, stock, fonts licensed for commercial/paid use and logged in `assets/LICENSES.md`.

## 7. Report

`work/reports/QA_REPORT_<ad>.md`: deliverables with measured numbers, brief checklist, every deviation with its reason (including client standing overrides), policy flags, what was measured vs. not perceivable, and 1–3 proposed tests (hook A/B, music A/B, variant without a scene). Send the CD a short list: links, decisions needed, proposals.
