# Ads (L2: paid social video ads)

Applies to every client under `ads/`, on top of the root `CLAUDE.md`. Procedure: skill `ad-edit` (`ads/.claude/skills/ad-edit/`). Client brand, CD decisions and templates live in `ads/<client>/`.

## What an ad job delivers

Per ad, in `output/final/`: `<name>_9x16_v<N>.mp4` (1080×1920, master), `<name>_4x5_v<N>.mp4` (1080×1350 crop of the master for Feed), `<name>_v<N>.srt` (verbatim, for upload), `<name>_thumb_v<N>.jpg` (frame with the hook on screen), plus `work/reports/QA_REPORT_<ad>.md`.
H.264 High, 30 fps, AAC 48 kHz, `+faststart`; 12–16 Mbps for 9:16. Loudness per the root rule (−14 LUFS, TP ≤ −1.5 dB).

## Rules for every ad

- **Hook in the first second.** Frame 1 already carries the hook text (it doubles as the thumbnail); open on motion, not on a still face waiting to speak. No logo intro, no slow fade-in.
- **Built for muted viewing.** Burned-in captions on every spoken word, plus on-screen text that carries the argument alone. The SRT is uploaded too.
- **Safe zones.** 9:16 text lives between y≈300 and y≈1248 (top 14% and bottom 35% are app UI). The 4:5 is a crop of the 9:16, so key text also sits inside its 1350px window (1080×1350 crop at y=120 → keep within y 120–1470).
- **One idea, one CTA.** End card ≥3 s, dead still for the last second, CTA wording matches the button the media buyer will use.
- **Length** 20–60 s; cut air hard (gaps 0.15–0.25 s), keep one deliberate beat at the turn.
- **Ad-policy cautions (Meta):** no claims the client can't prove (results, turnaround/SLA, "unlimited", guarantees without the client's sign-off), no invented numbers or testimonials, no fake UI (play buttons, notifications, system dialogs), no before/after implying personal attributes, no "you" statements about personal characteristics, licensed music and stock only (log in `assets/LICENSES.md`). Screens shown as product demos get an "Illustrative" label unless they're real captures. Flag anything borderline to the CD rather than deciding.
- Speakers' words are never patched or re-synthesised (root rule); a flubbed sentence is cut or flagged as a pickup.
- Propose A/B variants (hook line, music, with/without a scene) in the QA report rather than building them unasked.
