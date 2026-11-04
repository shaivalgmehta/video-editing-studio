# Ad 2C "The one that shows up": QA report and delivery note

Date: 2026-10-23. Editor's report for the creative director. Source `raw/VID20261022174728.mp4` (the guarantee script). Built from the cut you approved at the checkpoint, then graphics, render, finish and QA without stops, per your instruction.

## Deliverables (in `/out`)

| File | Measured |
|---|---|
| `2C_9x16.mp4` | 1080×1920, H.264 High, yuv420p, 30 fps, 10.6 Mbps video, AAC-LC 48 kHz, 25.83 s |
| `2C_4x5.mp4` | 1080×1350, same encode, 9.5 Mbps, crop y=120 (not squashed) |
| `2C.srt` | 29 cues, US spelling, "Delesign" correct |
| `2C_thumb.jpg` | 2.2 s: Shaival mid-word, hook bar on |

Duration 25.83 s: 22.83 s A-roll (settled open, first word 0.99 s, last word ends 22.46 s) + 3.0 s end card. Loudness **-14.0 LUFS, -1.0 dBTP, LRA 3.8**. Music: Mixkit 749, house settings (in at 8 s, -26 dB, ducked 5:1, +6 dB swell on the end card).

Review copies: `work/render/2C_v1_540p.mp4` (phone proxy of the finished file), `work/render/2C_v1_frames.jpg` (18 frames from the render), `work/render/snap2C/` (17 beat snapshots).

## Direction built (as approved)

| Time | Line | On screen |
|---|---|---|
| 0.0–6.8 | "I'm not gonna tell you we're the most creative design team you'll ever hire, but we're the one that shows up for when the work comes in every month." | Shaival full-frame; hook bar **"Not the most creative team."** from frame 1 (no walk-in on this take; he is seated and on the lens from the first frame). **The bar sits below his chin (y=880), not at the top of the band**: he is much closer to the lens on this shoot and at y=300 the bar covered his eyes (caught on the first render, re-rendered) |
| 6.85 | | Shaival shrinks to the picture-in-picture (bottom-right, as 2B); dot-pattern ground |
| 6.99–8.4 | "And you shouldn't decide that based on what I say." | Picture-in-picture on the dot ground, captions only |
| 8.89–13.2 | "You should see the actual designs, how we handle the feedback, and what it's like to work with the team." | **"See for yourself:"** then three check-chips landing on the clauses: Actual designs / How we handle feedback / Work with the team. A proof slot bottom-left shows the real thing under each chip: two portfolio flashes (Ads, Landing pages), the Go request-list recording, the Go team panel (designer + backup) |
| 13.5–16.0 | "That's why Delesign offers a 15-day money-back guarantee." | One card: small "Delesign offers a", then **15-day money-back guarantee** (orange "15-day"). No terms line, per your answer |
| 16.05 | | Back to full-frame |
| 16.34–22.5 | "Not the flashiest, but the one that shows up. So if you're looking at recurring design workload and want to see if there's a fit, book a call today." | Shaival full-frame, captions only |
| 22.83–25.83 | End card | White, logo, **The one that shows up**, orange **Book a call**, sub-line "Let's look at your recurring design workload" |

No B-roll on this ad, by design: the confession is the hook and it lives on his face.

## Cut

- Opens at raw 7.30 s, settled and looking at the lens; first word 0.99 s in (no walk-in on this take).
- 10 segments, 9 cuts; lip-smack at raw 11.11 removed; deliberate 0.45 s beats after "what I say" and after "guarantee"; punch-ins alternate 100/115 %.
- Nothing cut from the script as spoken. He says "shows up **for when** the work comes in" and "**the** actual designs" / "**the** feedback"; kept and captioned as spoken.

## Audio

Studio chain as approved on 2B v2 (DeepFilterNet + post-filter, expander, 280 Hz de-mud, 3.5 kHz presence, 9 kHz air, de-esser, 4:1). Every word survives transcription on the cut (99 words, Parakeet; whisper medium agrees on the text). Same honest ceiling as before: treated room, not a booth.

## Captions

Built from the cut transcript, then **snapped to the measured speech**: on this take Parakeet's word starts ran 0.15–0.43 s ahead of the audio, so each caption group was re-timed onto the -45 dB speech regions of the cut WAV (`_shared/tools/align_words.py`, new). The first caption now appears at 0.99 s, exactly when he starts. 29 groups, 2–4 words, ≤2 lines, 54–66 px, inside the band. Brand name normalized ("Dell Design" → Delesign); "15-day" and "money-back" hyphenated.

## Deviations and things to know

- **"with terms" is not said** on this take (script had it). The card shows the guarantee with no terms line because you said there are none. Logged as a claim you own: "15-day money-back guarantee" is the only offer statement on screen.
- Standing overrides applied and logged: no blurring of names in Go screens (team panel shows designer names), no footnote (no price in this script), hand notes none on this ad, "Illustrative workflow" at 14 px on the Go slot and team panel.
- Active caption word orange on the charcoal pill measures 2.89:1 (WCAG asks 3:1), same as 2A/2B.
- Face time is higher than 2B: full-frame for 0–6.85 s and 16–22.8 s (about 55 %), picture-in-picture for the middle 9 s. The script is a confession and a close, both of which need his face; the proof section is the only place graphics can own the frame.
- Hook bar position is a deviation from the style kit (y=300): on this framing it has to sit low. Worth a word to Shaival for the next shoot: sit back so the face ends above the band's top third, as on 2A/2B.
- The 2.2 s thumbnail has the mic hand large in frame (he holds the mic high on this take).

## QA checklist

- [x] Frame 1: hook bar on, face on the lens. Thumbnail at 2.2 s has face + bar.
- [x] No silence >0.4 s except the 0.99 s open, the two deliberate beats (0.51 s, 0.48 s) and the end-card tail (measured on the voice stem).
- [x] Captions match the audio, US spelling, "Delesign" correct, 29 groups of 2–4 words, re-timed to the measured speech.
- [x] Voice: studio chain, every word intact on transcription.
- [x] Nothing in the top 14 % / bottom 35 %; HyperFrames check: 0 lint errors, 0 runtime, 0 layout.
- [x] Go screens labeled "Illustrative workflow"; not redacted (your standing instruction).
- [ ] $85,000 footnote: not applicable.
- [x] No turnaround / SLA / "unlimited" / results claims. On-screen text: hook bar, "See for yourself:", three chips, "Ads", "Landing pages", "Delesign offers a 15-day money-back guarantee", end card.
- [x] Electric Blue only in the logo.
- [x] Loudness -14.0 LUFS, -1.0 dBTP.
- [ ] Watched muted at phone size: needs your eyes; I checked 17 snapshots and 18 decoded frames.
- [x] End card 3.0 s; last second still (mean frame diff 0.65 over 30 frames, encoder noise only).

## What I'd test next

1. Hook bar copy: "Not the most creative team." vs "Not the flashiest." (his own close line).
2. A 4:5 cut of the guarantee card as a static companion.
3. Thumbnail at 0.3 s (bar + settled face, no mic hand) vs 2.2 s.
