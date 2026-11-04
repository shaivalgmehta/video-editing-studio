---
name: sharkpreneur-reels
description: "Sharkpreneur podcast reels — style recipe copied from raw/Sharkpreneur Reel #1, project SP1, sourcing that worked"
metadata:
  node_type: memory
  type: project
  originSessionId: 1aa45a35-0192-4b97-baef-c09521bf947b
  modified: 2026-10-27T17:23:13.520Z
---

Started 2026-10-27: Sharkpreneur podcast reels (a separate client from the Delesign ads). The style reference is `podcasts/sharkpreneur/reference/Sharkpreneur Reel #1.mp4`. Reel 1 of Troy Broussard ("Low Stress Options") is HyperFrames project `podcasts/sharkpreneur/episodes/reel-02_low-stress-options/work/hyperframes/SP1`, with its cut in `podcasts/sharkpreneur/episodes/reel-02_low-stress-options/work/reel_lso/`.

**Style recipe, measured from the reference:**
- Background is #07080b with a #2f2e32 dot grid on a 54px pitch. The Zoom webcam sits in a full-width window: the host at y472 by 976px, the guest at y325 by 1270px.
- The hook is the host's question. Red #c30a0a words build above the window and white words below it, synced to speech.
- Captions are Inter 600, about 74px, with -0.06em tracking. They are white with a drop shadow, centred at y≈1512, one to three words per group, with no pill.
- Cutaways are full-bleed B-roll with scanlines, channel split and vignette (HyperFrames media-treatment). Huge red and white words sit behind the subject, using a `remove-background` cutout layered above them.
- A black slate carries a red header ending in "..." with white words appearing as they're spoken. The diagram card has a red title and white pills joined by red arrows, with the last pill in green #429b46.
- The reference outro (27.43 s to end, with its sound) is reused as is. The music bed sits about 18 dB under the voice, the master is about -16 LUFS, and whooshes are sparse.

**Sourcing:** YouTube copies are 480p at best; use yt-dlp for the full stream, since section downloads re-encode at a low bitrate. Pexels and Unsplash block scripts, and Openverse times out. Mixkit stock video works: tag pages list `free-stock-video/<slug>-<id>/` and the files are at `assets.mixkit.co/videos/<id>/<id>-720.mp4`. Higgsfield had only 4 credits.

**Why:** the CD asked to copy the reference reel's styling exactly. **How to apply:** for the next Sharkpreneur reel, copy SP1 and swap the cut, B-roll and words. Related: [[hyperframes-gotchas]], [[asset-sources]].
