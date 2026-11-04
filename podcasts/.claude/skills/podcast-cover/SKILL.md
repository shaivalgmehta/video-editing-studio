---
name: podcast-cover
description: Build cover images for podcast Reels and YouTube Shorts. Each is a full 1080x1920 cover that survives the platform crops (Instagram's 3:4 profile grid, the 4:5 feed and Shorts). It uses a guest cutout with a rim glow, a hook headline, a reel-specific prop and the show branding, and must read at about 200 px. Use when the CD asks for reel covers, thumbnails or grid images for an episode's reels.
---

# Podcast reel cover

The worked example is Retail Razor S6E15 (covers c1–c6):
- generator: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/covers/gen.py`
- cutout scripts: `clean.py` and `bake.py` in the same folder
- HyperFrames project: `work/hyperframes/covers`
- output: `output/final/covers/`

The look (colours, fonts, glow colour) comes from the client's L3. Pick the cutout with the `media-use` skill (`remove-background`). Use `video-qa-delivery` for check and snapshots.

## Formats and safe areas
- **Master:** 1080x1920 PNG. This is the full cover shown in the Reels tab and full-screen.
- **Instagram profile grid:** **3:4, a 1080x1440 centre crop (y 240–1680)**. Instagram has used this since early 2025; before that the grid was square.
- **Instagram feed preview:** 4:5, a 1080x1350 centre crop (y 285–1635).
- **Keep the headline, face, logo and guest line inside the 4:5 band (y 285–1635), with 60 px side margins.** That band sits inside both crops. S6E15 previewed only the 4:5 crop; preview the 3:4 crop as well.
- In the full-screen viewer, platform UI covers the bottom (caption, handle) and the right edge (buttons). Keep only atmosphere there, such as the fade and the body.
- **YouTube Shorts:** set a custom thumbnail by uploading this image in the **YouTube mobile app** at upload time, where the account has that option. Otherwise you can only pick a frame from the video. Check what the platform currently offers when you deliver. If only frame picking is available, tell the CD; don't add a cover frame to the reel without approval.
- Platform crop rules change. Re-check the current grid and feed ratios before a new client's first delivery, and note the date you checked.

## Design recipe (one template per episode, so the grid reads as a set)
1. **Guest frame:** pick candidate frames from the reel's A-roll at the guest's word midpoints. Score face sharpness (variance of the Laplacian) and look at contact sheets. Choose open eyes and a live, expressive face that suits the reel's mood. For each reel's cover, use a frame from that reel.
2. **Cutout:**
   - Run `npx hyperframes remove-background` on the chosen frame.
   - Clean the alpha: a slight erode plus blur, keep the largest component, and darken the edge pixels to remove the old backdrop's spill.
   - Crop to the bounding box.
   - **If you fix a cutout by hand, protect it from re-running the clean script.** Note it in the work folder.
3. **Bake:** a gentle grade (a little contrast and warmth), then a **soft accent-colour glow** plus a **thin rim light** around the alpha, saved as a padded PNG. Record the face centre x and the padding so the layout can place the head.
4. **Hook headline:**
   - 2–4 lines of heavy uppercase, auto-fitted to the width (measure with the real font).
   - **One key word in the accent colour, with a glow.**
   - It is a hook (a question, a claim or a contradiction), not a quote. If it uses the speaker's words, keep them verbatim. Never add numbers that weren't said, and never misstate the reel.
   - An optional 1–2 line sub-line underneath.
5. **Reel-specific prop:** one small graphic that echoes the reel's main card. Examples: an upvote badge for a Reddit reel, an "SEO → GEO" chip, a cracked AI-answer card, ticked rule tiles, a funnel with a pool, a validation chip. Place it beside the head; it must not cover the face.
6. **Branding:** show logo plus show name and episode code at the top-left. A guest line ("WITH <GUEST>, <COMPANY>") with an accent dash near the bottom of the safe band. Add a fade at the bottom so the text sits on a dark ground.

## Build and review
- Write a generator script (`gen.py`) that writes one HyperFrames composition per cover, 1 s each, into a covers project, configured as a single `COVERS` dict (lines, key words, size caps, prop, face x, sub-line). Run `check`, then snapshot each cover at `n-0.5 s`.
- Make a review sheet with the 4:5 and 3:4 crop lines drawn over each full cover. Also make a **phone-size grid test**: crop each cover to the grid ratio, scale it to **about 200 px wide**, and lay the set out 3 across. The headline key word and the face must read at that size. If not, make the type bigger, cut words or simplify the prop.
- Deliver to `output/final/covers/`:
  - `<SHOW>_<SxEyy>_R<n>_cover.png` (1080x1920)
  - `<SHOW>_<SxEyy>_R<n>_cover_grid.jpg` (the grid-crop preview, 3:4)
  - `contact_sheet.jpg`

## Checklist
- [ ] Face and headline are inside the 4:5 band and clear of the UI zones.
- [ ] The key word and face read at about 200 px wide.
- [ ] Headline is truthful to the reel, any quote is verbatim, and there are no invented numbers.
- [ ] Prop matches the reel's idea and doesn't cover the face.
- [ ] The set is consistent across the episode (same template, varied headline, prop and expression).
- [ ] Cutout edges are clean, with no backdrop fragments around the hair.
