# Ad 2B "Co-pilot": QA report and delivery note

Date: 2026-10-23. Editor's report for the creative director. Built end to end without checkpoints, per your instruction.

## v2 (your notes on the first delivery)

- **Fumble after "Ours is already on your account" removed.** The cut was joining the restart 0.17s too early and carried the tail of the flubbed "reliable". The in-point now sits after it (raw 57.08s); every word still intact on transcription.
- **Picture-in-picture moved to the bottom-right** (x 755–1015, y 680–1142). Caveat: the Reels action rail (like/comment/share) sits on the right edge from roughly 55% down; the window's lowest 90px can sit under the top icon. Nothing with text is there.
- **Text blocks widened to full width (950px) and enlarged**: card stack 50px heads, questions 44–50px, asks 54–64px, everything left-aligned so no element runs around the window. The third "Ask to see" chip no longer wraps the video.
- **Audio: stronger "studio" chain.** DeepFilterNet with its post-filter, firmer expander (shorter tails between words), a 4 dB de-mud cut at 280 Hz, +3 dB presence at 3.5 kHz, +2 dB air above 9 kHz, firmer de-esser, 4:1 compression. Measured against raw: the room tail between phrases is 16.5 dB lower (was 3.4 dB lower on the previous chain), floor 31 dB lower, 7.6 dB brighter. Every word survives transcription. Honest ceiling, unchanged: this is a treated room, not a booth; the reverb inside long vowels is still there. A lav mic on the next shoot is the real fix, and it's cheap.

## Deliverables (in `/out`)

| File | Measured (v2) |
|---|---|
| `2B_9x16.mp4` | 1080×1920, H.264 High 4.1, yuv420p, 30fps, 10.4 Mbps video, AAC-LC 48 kHz, 48.20s |
| `2B_4x5.mp4` | 1080×1350, same encode, crop y=120 (not squashed) |
| `2B.srt` | 52 cues, US spelling, "Delesign" correct |
| `2B_thumb.jpg` | 2.2s: Shaival seated, mid-word, hook bar on |

Duration 48.20s: 45.17s A-roll (walk-in pre-roll, first word 2.06s) + 3.0s end card. Loudness **-14.0 LUFS, -1.0 dBTP, LRA 2.0**. The join after "Ours is already on your account" now measures -39 dB (silence) where the fumble was. End card last second: max pixel change 2/255. Music: Mixkit 749, same settings as 2A.

## Direction I took (creative freedom)

The metaphor is redundancy, so the whole ad is built as "what happens without a backup" → "the four questions" → "here's ours".

| Time | Line | On screen |
|---|---|---|
| 0.0–2.06 | (walk-in) | Shaival enters and sits; hook bar **"Two pilots. Two meals."** on from frame 1 |
| 2.86–8.6 | "…pilot and co-pilot… land the plane." | Cockpit B-roll: a cockpit takeoff (native vertical), then a cockpit window over clouds. Deliberate 0.46s beat after "land the plane." |
| 8.6–11.3 | "Most outsourced design services don't have a co-pilot." | Shaival full-frame (the turn) |
| 11.3 | | Shaival shrinks to the picture-in-picture; dot-pattern ground |
| 11.4–16.7 | "The first job looks fine… work piles up… out on leave… chasing every project." | Three numbered cards stack as he goes: **1 First job → "Looks fine"** (deep green tag), **2 Monthly work → Requests 4 → 13 (illustrative)**, **3 Designer on leave → calendar strip with an OUT OF OFFICE block** and a hand note "who's chasing?" |
| 16.8–27.0 | "So here's what I'd ask any design partner. One… Two… Three… Four…" | One card, **"Ask any design partner:"**, the four questions landing on his "One / Two / Three / Four" |
| 27.0–31.9 | "At Delesign we use a dedicated designer with a backup and a shared way to manage requests." | Go team panel (designer + backup) with the push to the backup on "backup" and the note "your co-pilot"; then the request-list recording full-bleed on "manage requests" |
| 31.9–37.9 | "Don't take my word for it. Ask to see a real request, a real progress update, and how a project gets handed over." | **"Ask to see:"** with three check-chips landing on the words: A real request / A real progress update / A real handover |
| 37.9–40.3 | "Ask every design partner who their co-pilot is." | Cockpit callback B-roll |
| 40.3–45.3 | "Ours is already on your account. If you run an agency and need a reliable design partner, book a call." | Shaival full-frame, captions only (no claim card: his line carries it) |
| 45.3–48.3 | End card | White, logo, **Get a reliable design partner**, orange **Book a call**, sub-line "Ongoing design support for agencies" |

## Cut

- Walk-in pre-roll from raw 3.3s; first word at 2.06s.
- Two restarts removed: "Ask every design partner who uses it." (raw 47.69–49.75) and the first "If you run an agency and need a reliable" (raw 54.93–57.03, cut inside speech 0.17s before the restart).
- Numbers kept as spoken ("One, how do you track priorities?"): the captions carry them and the card rows land on them.
- 19 segments, 18 cuts; A-roll 45.33s.

## Captions

Follow the audio. Two spots where the engines disagreed, resolved by majority: "the pilot and co-pilot **are served**" and "when the designer **is** unavailable" (he says it singular here). The cut transcript dropped "Ours is already on your account" though the audio is intact (measured -16 dB RMS there); those six words were restored from the raw timestamps. Brand name normalized to "Delesign"; "work piles up"; "co-pilot" hyphenated.

## Things to decide or supply

1. **The cockpit clip is a small propeller plane** (checked sunshade, analog panel), not an airliner with two pilots. It reads "cockpit" at a glance but not "airline". If you want the airliner, I need a clip: the free libraries' two-pilot airliner footage is 720p, too soft for 9:16.
2. **A "progress update" Go screen** would let the "Ask to see" beat show the real thing; today it's text chips.
3. Same open items as 2A: 2x Go captures, and the standing overrides (no footnote, no blurring) are applied and logged.

## Speed-ups made for the next ad

- `ads/delesign/tools/new_ad.py <ad> <raw>`: one command does probe, clean audio, Parakeet + whisper transcripts and a draft runs table.
- `ads/delesign/tools/build_cut.py <config.json>`: the cut from a JSON of runs, no script copying.
- `ads/delesign/tools/build_captions.py <words> <project> <duration>` and `finish.py --name --project`: both parametrized.
- Scenes from 2A/2B are a kit now (hook, stack, questions, go screens, asks, end card); a new ad is mostly re-timing and copy.
- Render + finish run as one background job (~10 min on this laptop); everything else is minutes.

## QA checklist

- [x] Frame 1: hook bar on; face enters at ~0.9s (walk-in open, per your standing preference). Thumbnail at 2.2s has face + bar.
- [x] No silence >0.4s except the pre-roll (2.48s, by design), the deliberate beat after "land the plane" (0.46s), one 0.43s breath before "Ask to see", and the end-card tail.
- [x] Captions match the audio, US spelling, "Delesign" correct (52 groups, 2–4 words, ≤2 lines, inside the band).
- [x] Voice: same chain as 2A, every word intact on transcription (one sentence the ASR dropped was restored from the raw timing; audio verified present).
- [x] Nothing in the top 14% / bottom 35%; HyperFrames layout audit 0 errors.
- [x] Go screens labeled "Illustrative workflow"; not redacted (your standing instruction).
- [ ] $85,000 footnote: not applicable (no price in this script).
- [x] No turnaround / SLA / "unlimited" / result claims. On-screen text: hook bar, three card titles, "Looks fine", "Requests 4 → 13 (illustrative)", "OUT OF OFFICE", "who's chasing?", the four questions as he says them, "your co-pilot", "Ask to see: A real request / A real progress update / A real handover", end card.
- [x] Electric Blue only in the logo.
- [x] Loudness -14.0 LUFS, -1.0 dBTP.
- [ ] Watched muted at phone size: needs your eyes; I checked 36 frame grabs.
- [x] End card 3.0s; last second still (encoder noise only).

## Deviations from the brief (2A rules inherited)

Cold open on motion, no blurring, hand-written notes kept to one short phrase per screen, "Illustrative workflow" at 14px, active caption word at 2.89:1 on the pill: all as on 2A, all logged. New: the numbered questions are spoken as "One, Two, Three, Four" and captioned that way.

## What I'd test next

1. Hook bar copy: "Two pilots. Two meals." vs "Who's your co-pilot?"
2. The cockpit clip: prop plane (current) vs an airliner clip if you can license one.
3. A version with the four questions as a full-screen card (no picture-in-picture) for that 10s stretch.
