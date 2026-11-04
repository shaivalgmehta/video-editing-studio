# Level 2: podcast work (any client)

This level turns finished long-form podcast episodes into short pieces: Reels/Shorts, episode teasers and Reel covers. It also covers the editorial side of carousels, LinkedIn posts, newsletters and quote graphics.
The level-1 rules in the root `CLAUDE.md` still apply: verbatim captions, no invented numbers, literal b-roll, licence log, check plus snapshots, one render at a time, levelling and naming.
Generic how-to lives in the level-1 skills `video-edit-core` (cutting, audio, captions, HyperFrames), `video-qa-delivery` (check, snapshots, levelling, naming, archive) and `stock-sourcing` (footage, logos, music, licences). Reference those skills here; don't repeat them.

## Skills at this level

| Skill | Use when |
|---|---|
| `podcast-repurposing` | First, on every podcast job. It holds the CD's editorial rules and checklists. Use it to pick moments, write hooks and scripts, and plan the posting spread, and again at QC. |
| `podcast-reel` | Making 9:16 Reels/Shorts from an episode: from picking the clips through to the shared build brief, per-reel agents, central renders and posting order. |
| `podcast-teaser` | Making the pre-release episode teaser (usually 16:9, about 60 s) in the style of a reference video. |
| `podcast-cover` | Making the cover image for each Reel or Short, plus the platform-crop checks. |

Level 3 (`podcasts/<client>/`) supplies each show's brand, approved pilot templates, reusable outro, show-frame crop map and standing CD decisions. Example: Retail Razor's L3 has its warm-brown look, red accent, Montserrat and Caveat, the R2 pilot and a 3 s outro. **Before building, read the client's L3 `CLAUDE.md` and skills. If the client has none yet, build a pilot, get it approved, then write the L3 skill.**

## Episode folder

```
podcasts/<client>/episodes/<SxEyy_guest-slug>/
  input/     the finished episode mp4, show-notes transcript, cover art, media kit (read-only)
  work/
    episode/   ep_words.json (whole-episode word timings), teaser EDL + checkpoints, episode-level scripts
    reels/     BRIEF.md (shared build brief), r1..rN/ (EDL.md, NOTES.md, words.json, build scripts, tmp/, snaps/)
    covers/    cover generator + cutout scripts, frames/, review sheets
    hyperframes/  r1..rN/, teaser/, covers/   (one HyperFrames project per deliverable)
  output/final/{reels,teaser,covers}/   current versions only
  output/archive/                        superseded versions
```
Name deliverables `<SHOW>_<SxEyy>_<deliverable>_<aspect>_v<N>.mp4`, for example `TRRS_S6E15_R3_9x16_v2.mp4` or `TRRS_S6E15_teaser_16x9_v7.mp4`. Covers are `<SHOW>_<SxEyy>_R<n>_cover.png`.

## Always-on podcast rules
1. **Quotes are verbatim to the audio.** Script, captions and on-screen quotes must match what is actually said. Show notes and auto-transcripts mishear words and mislabel speakers, so check each line by ear and against the video. If a key word is unclear, cut its sentence and raise it as an open question. Never patch or re-synthesise.
2. **A guest's statistic is the guest's claim.** Leave it in their spoken words and captions. If it goes on a card, attribute it to them ("<Guest>: over half of …"). Never restate it as an established fact. Never add numbers they didn't say, and keep illustrative charts and meters free of figures.
3. **Keep the host's point of view.** Keep the host's question or set-up where it frames the clip. Caption the host's clear lines. Name both host and guest. The asset should make the **host** worth following, not only the guest.
4. **Each clip gives a different reason to care.** One idea per clip, which a viewer can sum up in one sentence. No two near-identical cuts, no rewritten sensational titles, and the payoff lands inside the clip.
5. **Locate lines in the whole-episode word timings, not in show-notes timestamps.** Show-notes timestamps drift by a few seconds; in S6E15 they ran about 4 s early. Transcribe the episode once to `work/episode/ep_words.json`, check that it shares the mp4's timebase, then search it for each line.
6. **Represent the guest fairly.** No misleading drama. Never show the guest's (or the client's) own customers or partners as negative examples. List them in the episode brief.
7. **Propose before building.** Send the CD picks, scripts, beat sheets and open questions as short plain lists. Build after approval. Every deliverable has a `NOTES.md` that lists its open questions.
8. **Plan the release spread:** pre-release (teaser plus one reel), launch day (the strongest reel), then the rest spread over +2 to +14 days.

## Typical inputs and traps
- The client often supplies only the **finished episode**, with a branded frame, logo boxes and burned-in captions. Map those boxes in pixel coordinates once per show (put the map in L3) and crop every shot inside the clean window.
- Show-music licences are often unknown. Use licensed stock music (see `stock-sourcing`) and ask the client before using the show theme.
- No AI video generation is assumed to be available. B-roll is licensed footage, real logos, or UIs rebuilt in HTML.
