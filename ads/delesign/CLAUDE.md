# Delesign (L3 client: paid social ads)

Applies on top of `../CLAUDE.md` (ads, L2) and the root `CLAUDE.md` (L1). Procedure: skill `delesign-ad` (`.claude/skills/delesign-ad/`).

## Client

- **Delesign**: a design subscription for agencies. Each agency gets one dedicated designer plus a backup who shadows the account; requests run through Delesign's own platform **Go**, with a daily update process.
- **Audience**: agency owners and ops leads, retargeting (they already visited the site). Placements Meta Reels, Stories, Feed; most watch muted.
- **On camera**: Shaival (Co-CEO), phone, 4K portrait, handheld mic. Calm and wry: a sharp founder talking, not a produced commercial.
- **The user is the CD**, I'm the editor. Reviews come as short notes with 2–4 concrete changes; "complete the next steps" / "make it quick" = run the remaining stages without checkpoints. The CD wants creative proposals from me, with the reason; the CD decides.

## Brand

- Colors: Sunset Orange #FF5532 (highlight, CTA, active caption word), Charcoal #1E293B, Deep Green #33473B, French Lavender #C7B0FF, Off-white #F8FAFC, Electric Blue #334EAC (**logo only**).
- Fonts: Hanken Grotesk (everything, 700/800); Architects Daughter only for short hand-written notes. Files in `brand/brand/fonts/`.
- Logo: `brand/brand/` (web SVGs in `brand/brand/logo_web/`). US spelling; brand always "Delesign".
- Go screens and recordings: `brand/go/` (2x preferred). B-roll with licences: `brand/broll/` (golden_gate, cockpit, phone).

## CD's standing decisions (don't re-ask; log the overrides in every QA report)

- **No source footnote** on the $85,000 salary figure, and **no blurring** of client names, logos or people in Go screens. Both override the brief's legal rules.
- **Face time** only for the hook and the close; the middle is Shaival in a small picture-in-picture, **bottom-right** (CD's call on 2B), graphics owning the frame on a light dot-pattern ground.
- **No hand-drawn circles** on screenshots: clean selection outlines, or play the recording full-bleed. When a capture has a built-in magnified callout (e.g. `Feedback after.jpg`), frame on the callout with a clean orange outline; move the "Illustrative workflow" label bottom-left when the PiP covers bottom-right.
- Real Go screenshots beat mock panels, even at 1x.
- A representative number ("× 6 clients") stays off screen. No turnaround / SLA / "unlimited" / results claims.
- **Unclear word → cut its sentence**; never AI voice or re-synthesis. Exception (2D): when the flub is in the hook line, offer full line vs trimmed and default to the full line as spoken.
- **Open on real motion** (Shaival walking in and sitting down), hook bar on from frame 1.
- Audio: house "studio" chain (DeepFilterNet + EQ/comp), verified word-for-word by transcript; resemble-enhance is rejected (it rewrote words).

## Campaign state (Meta, Oct 2026)

- Ads 2A "The fourth way", 2B "Co-pilot", 2C "The one that shows up" (15-day money-back guarantee, no terms line), 2D "Some things just stick" delivered: `projects/2026-10_meta-campaign/output/final/`, reports in `.../work/reports/`.
- Built in Meta (account act_403278359021461, creds in the root `.env`, not the fb MCP): campaign "Agency Recurring Design | Lead", single SCHEDULE ad set, everything created **paused**. Folder-to-brief video mapping: 2A=2A, 2B=3A, 2C=8B, 2D=6B. Videos use the BOOK_TRAVEL CTA (shows "Book now"; placement-customised videos reject BOOK_NOW).
- Landing pages: video 2A → `/recurring-design-for-agencies`; guarantee page dropped, those ads go to `/dedicated-graphic-designer`. Avoid "unlimited" promises.
- Approved: $85k salary line in 2A; drop "Meet a real Delesign designer" from 2D.

## Folders

`brand/` (logo, fonts, Go screens, B-roll), `templates/ad/` (HyperFrames template, copy per ad), `tools/` (pipeline scripts, all take `--project`), `projects/<YYYY-MM_slug>/` (jobs), `SETUP_FOR_NEW_EDITOR.md` (machine setup).
