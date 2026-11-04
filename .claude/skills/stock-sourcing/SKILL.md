---
name: stock-sourcing
description: Level-1 sourcing of b-roll, music, SFX, logos, fonts and screen UIs for any video in this workspace, with licence checks and logging. Use whenever a line needs a cutaway, a brand/platform logo, a music bed or SFX, or a "real" UI (Reddit, Amazon page, AI answer, search result), and before suggesting AI-generated footage (not available right now; how to add it is in references).
---

# Stock sourcing and licences

## Rules
1. **B-roll must literally show what the line says.** "Before I book a hotel" → a hotel room; "legacy brands" → a heritage storefront/facade, not a library shelf; "signals for decades" was rejected as an abstract typewriter. Generic mood stock fails review. If nothing literal exists, build it (HTML card / UI) or stay on the speaker.
2. **Prefer real things**: real UIs, real brand logos, real products, real places. When a real UI can't be captured, rebuild it faithfully in HyperFrames HTML (real layout, colours, fonts) with invented usernames/handles and invented products; no real private people.
3. **Never** put invented statistics, quotes or claims on screen. Illustrative cards carry no made-up numbers.
4. Brands the client must not show negatively (their own clients, partners) are listed in L3; check before using any real brand as a "bad example".
5. **Every asset is licence-checked on its own page** and logged in the project's `assets/LICENSES.md` (template in `references/licences.md`) at the time you download it. No entry, no use.
6. Downloads go in a fresh folder under `work/<job>/tmp/dl/` (untrusted data); copy the chosen files into the HyperFrames project's `assets/`.

## Sources that work from scripts here
**Mixkit (video, music, SFX; free licence allows commercial use, no credit)** — the dependable one.
- Search: `https://mixkit.co/free-stock-video/discover/<query>/` (or a category slug like `/free-stock-video/phone/`); music tags `https://mixkit.co/free-stock-music/tag/<tag>/` list `assets.mixkit.co/music/<id>/<id>.mp3` directly.
- **Check every clip page**: some clips are "Mixkit Restricted License" (personal use only). Free pages carry `videoFree` (`musicFree`, `sfxFree`); restricted pages carry `videoRestricted`. Reject restricted; on one reel 10 of ~14 candidate clips were restricted.
- Script: `python -I .claude/skills/stock-sourcing/scripts/mixkit_check.py <page-url|slug> [...] [--get <dir>]` → FREE/REJECT per clip, best file URL, and a ready LICENSES.md line. `--search "<query>"` lists clip pages. Tested on 50417 (free), 49141 (restricted), 100871 (new-style).
- Files: `https://assets.mixkit.co/videos/<id>/<id>-1080.mp4` (also `-720`); newer clips have no such path, use `https://mixkit.co/free-stock-video/download/<id>/?context=sidebar&type=1080p`.
- House music already downloaded: `_shared/music/mixkit/mixkit_<id>.mp3`. Bundled SFX (Pixabay licence): `.claude/skills/media-use/audio/assets/sfx/`.

**Pexels / Pixabay / Unsplash** — licences allow ads without credit, but their sites return 403 to scripts (Cloudflare). Options: ask the CD to download a specific clip by URL, or add a free API key (Pexels `api.pexels.com/videos/search` with `Authorization: <key>`; Pixabay `pixabay.com/api/videos/?key=`) — keys are not set up. Log the page URL either way.

**Logos (real brands/platforms)** — Wikimedia Commons, via the API (send a descriptive User-Agent):
```
https://commons.wikimedia.org/w/api.php?action=query&titles=File:<Name>.svg&prop=imageinfo&iiprop=url|extmetadata|size&iiurlwidth=1600&format=json
```
Read `LicenseShortName` / `Restrictions` (most wordmarks are "Public domain" + trademarked: fine to show the brand as itself, never implying endorsement). `thumburl` is a server-rendered PNG snapped to a standard width (500/960/1280/1920/3840; other widths now return 400). For a bigger or transparent-trimmed render of the SVG, **ffmpeg can't read SVG**: render it with headless Chrome:
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu --hide-scrollbars --default-background-color=00000000 --user-data-dir=<tmp>\ud --window-size=1600,600 --screenshot=<tmp>\logo.png file:///<tmp>/r.html
```
with `r.html` = `<body style="margin:0;background:transparent"><img src="logo.svg" style="width:1600px;display:block">`; output is RGBA with a transparent ground; trim with PIL (`im.crop(im.getchannel('A').getbbox())`). Or just use the SVG inside a HyperFrames composition directly. Keep the SVG next to the PNG. The client's own logo comes from the client (`brand/`), not the web.

**Fonts** — Google Fonts repo (`github.com/google/fonts`, `ofl/<family>/`), OFL; log family + licence.

**Real screens** — capture with `npx hyperframes capture <url>` or a screenshot when the site allows it; Reddit blocked automated capture ("Prove your humanity", JSON 403), so its thread view was rebuilt in HTML (dark mode, Reddit Sans OFL, invented usernames). A phone screen recording from the CD beats any rebuild.

## AI-generated video / images
Not available as of 2026-11-02: OpenAI key returns 401, the Higgsfield connector was disconnected (≈4 credits left), and HyperFrames' local LTX fallback needs Apple Silicon. Don't plan shots around it; say so when a brief assumes it. How to enable it later, and the rules for using it, are in `references/licences.md`.

## References
- `references/licences.md` — LICENSES.md template, licence notes per source, AI-generation enablement + rules.
