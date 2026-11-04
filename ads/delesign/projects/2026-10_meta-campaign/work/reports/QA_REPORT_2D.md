# Ad 2D "Some things just stick": QA report and delivery note

Date: 2026-10-24 (v2). Editor's report for the creative director. Source `raw/VID20261022175328.mp4` (the brands / phone-number script).

## v2 (your notes on v1)

- **First line kept in full**: "I still remember the first phone number I ever done." The trimmed version is gone; everything after it moves 0.63 s later.
- **v3: the caption on that line reads "learnt" (your note), while the audio still says "done"**: no re-synthesis, per your standing rule. This is the one place the captions and the SRT do not match the audio; logged here. Note "learnt" is UK spelling against the house US-spelling rule; say the word and I'll make it "learned".
- **"The last round of feedback" screen** is now your `Feedback after.jpg` brief, framed on the magnified "Project Description: You know the drill by now." callout, with a clean orange outline landing on it on "feedback" and a slow push. The window shows the lower half of the brief so the callout sits clear of the picture-in-picture.
- **Guidelines beat** now shows the brand guidelines image (`brand_guidelines_example.png`, the only brand-guidelines image in the assets), top part in a 950×520 window with a slow push; the Brands list stays for the "several client brands" beat later.

## Deliverables (in `/out`)

| File | Measured |
|---|---|
| `2D_9x16.mp4` | 1080×1920, H.264 High, yuv420p, 30 fps, 10.9 Mbps video, AAC-LC 48 kHz, 41.0 s |
| `2D_4x5.mp4` | 1080×1350, same encode, crop y=120 (not squashed) |
| `2D.srt` | 42 cues, US spelling, "Delesign" not spoken in this script |
| `2D_thumb.jpg` | 1.0 s: head just up from the mic, eyes on the lens, hook bar on (1.2 s had his eyes still down) |

Duration 41.0 s: 37.97 s A-roll (head comes up at 0.6 s, first word 1.79 s, last word ends 37.5 s) + 3.0 s end card. Loudness **-14.0 LUFS, -1.0 dBTP, LRA 1.9**. Music: Mixkit 749, house settings (in at 8 s, -26 dB, ducked 5:1, +6 dB swell on the end card).

Review copies: `work/render/2D_v2_540p.mp4` (phone proxy of the finished file), `work/render/2D_v2_frames.jpg` (frames from the render), `work/render/snap2D_v2/`, `snap2D_v2b/` (v2 beat snapshots; v1 sets alongside).

## Direction built (as approved)

| Time | Line | On screen |
|---|---|---|
| 0.0–1.8 | (head down at the mic, comes up) | Hook bar **"Some things just stick."** from frame 1, below the chin (see deviations) |
| 1.79–4.0 | "I still remember the first phone number I ever done." | Shaival, then at 2.3 s the orange rotary phone B-roll, finger on the dial (slow push) |
| 4.4–5.4 | "Some things just stick." | Second phone clip (red rotary, finger dialing), slow pull; 0.45 s beat |
| 5.8–8.2 | "And that's what I want your clients' brands to feel like for us." | Shaival full-frame |
| 8.23 | | Shaival shrinks to the picture-in-picture (bottom-right); dot-pattern ground |
| 8.6–10.9 | "Not just the logo, but what each one liked and rejected." | Card **"Not just the logo"** with two tags landing on his words: **Liked ✓** (deep green), **Rejected ✗** (orange) |
| 11.2–16.9 | "Client one likes simple layouts, client two needs very specific typography, client three has an ad format their team prefers." | Numbered card stack, one per client, landing on "Client one / two / three": **Simple layouts** (three layout blocks), **Specific typography** ("Aa" sample), **Preferred ad format** (three frame outlines) |
| 17.7–20.0 | "The last round of feedback should help with the next brief." | Your "feedback after" brief, framed on the magnified "You know the drill by now." callout; orange outline lands on it on "feedback" |
| 20.1–22.0 | "We keep the guidelines and reference work" | Brand guidelines image, note "guidelines live here" |
| 22.1–24.2 | "close to the requests. So we're not starting" | Go request-list recording full-bleed |
| 24.3–26.1 | "from zero every time a new campaign comes in." | **"Not from zero:"** with three check-chips: Guidelines / Reference work / Last feedback |
| 26.3–29.4 | "And when someone needs to cover an account, that context is right there." | Go team panel (designer + backup), push to the backup on "cover", note "same context" |
| 29.6–31.9 | "And that matters when several client brands are involved." | Go Brands list (three brands), slow push, note "every brand, one place" |
| 32.2–33.6 | "Some things just stick," | Orange phone callback, full-frame |
| 33.6–37.9 | "and your clients' brands should too. Book a call if you need a designer that you can rely on." | Shaival full-frame, captions only |
| 37.97–40.97 | End card | White, logo, **Your clients' brands, remembered**, orange **Book a call**, sub-line "A designer you can rely on" (his words) |

## Cut

- Opens at raw 2.75 s: head down at the mic, comes up at 0.6 s, first word at 1.79 s.
- 15 segments, 14 cuts. Hook sentence kept in full (v2, your call; "I ever done" stays as spoken and captioned). Four false starts of "Book a call to" removed (raw 42.4–48.8 s); the fifth take kept.
- Deliberate 0.45 s beats after "number", after "stick." and after "involved."; 0.3 s + punch-in before "The last round of feedback".

## Audio

Studio chain as approved on 2B v2. Every word survives transcription on the cut (137 words, Parakeet; it heard "tick" for "stick" once on v2, fixed as a token; whisper medium agrees on the text, including "an ad format" and a clean final line). Same honest ceiling: treated room, not a booth.

## Captions

Built from the cut transcript and **snapped to the measured speech** (`_shared/tools/align_words.py`: Parakeet word starts ran 0.1–0.4 s early on this take). 42 groups, 2–4 words, ≤2 lines, 54–66 px, inside the band. Fixes applied to ASR tokens only: "Something's" → "Some things", "Client 1/2/3" → "one/two/three" as spoken, "added format" → "ad format", "clients brands" → "clients' brands".

## B-roll

Two Pexels clips (Pexels License: free for commercial use, no credit), cropped 9:16 around the dial, 30 fps: an orange rotary phone being dialed (used twice: hook and callback) and a red rotary phone being dialed. Sources and crops in `ads/delesign/brand/broll/phone/LICENSES.md`; originals kept in `ads/delesign/brand/broll/phone/dl/`.

## Deviations and things to know

- **Hook bar below the chin (y=880), not at the top of the band**: Shaival sits close to the lens on this shoot and at y=300 the bar covered his eyes. Same on 2C. For the next shoot: sit back as on 2A/2B.
- **"with terms" / terms**: not applicable (no offer in this script).
- Standing overrides applied and logged: no blurring of brand names in the Go Brands list (Delesign, Take The Power Back, ECOFIP.GF) or designer names in the team panel; no footnote (no price); hand-written notes kept to one short phrase per screen (four in total); "Illustrative workflow" at 14 px on every Go screen (the two Brands screens were shortened to 380 px so the label clears the picture-in-picture).
- Active caption word orange on the charcoal pill measures 2.89:1 (WCAG asks 3:1), same as 2A/2B.
- The "feedback after" brief is a real Go project (Project 69362, client link and attachment names visible); not redacted, per your standing instruction. Its text is small at 1x; the beat relies on the magnified callout you built into the image.
- The brand guidelines image is the 714 px stock example from 2A, upscaled 1.33× to fit the 950 px window; a 2x capture of a real client guideline page would be sharper.

## QA checklist

- [x] Frame 1: hook bar on, head down at the mic (motion open: the head comes up at 0.6 s). Thumbnail at 1.0 s has face + bar.
- [x] No silence >0.4 s except the 1.8 s open, the deliberate beats and the end-card tail: measured gaps on the voice stem 0.49 s after "done.", 0.52 s after "stick.", 0.48 s before the callback, 0.59 s after "rely on", then the end card.
- [x] Captions match the audio except one word by your instruction ("learnt" over the spoken "done", UK spelling); otherwise US spelling, 2–4 words, re-timed to the measured speech.
- [x] Voice: studio chain, every word intact on transcription.
- [x] Nothing in the top 14 % / bottom 35 %; HyperFrames check: 0 lint errors, 0 runtime, 0 layout.
- [x] Go screens labeled "Illustrative workflow"; not redacted (your standing instruction).
- [ ] $85,000 footnote: not applicable.
- [x] No turnaround / SLA / "unlimited" / results claims. On-screen text: hook bar, "Not just the logo", "Liked ✓", "Rejected ✗", "Client one/two/three", "Simple layouts", "Specific typography", "Preferred ad format", four hand notes, "Not from zero:" + three chips, end card.
- [x] Electric Blue only in the logo.
- [x] Loudness -14.0 LUFS, -1.0 dBTP.
- [ ] Watched muted at phone size: needs your eyes; I checked 32 snapshots and the decoded frame sheet.
- [x] End card 3.0 s; last second still (mean frame diff 0.52 over 30 frames, encoder noise only).

## What I'd test next

1. Hook bar copy: "Some things just stick." vs "The first number you ever learned."
2. The full first line (v2) vs opening on "Some things just stick." (cut L1 entirely), if the "done" bothers anyone in comments.
3. A version with the three client cards as one full-screen card (no picture-in-picture) for that 6 s stretch.
