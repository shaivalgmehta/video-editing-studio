# TRRS S6E15 reel R1: "The Reddit final check" (not rendered)

Project: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/hyperframes/r1` (copied from the R2 pilot). Work files: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r1/`.
**v4 duration 34.37 s** = 31.37 s A-roll + 3.0 s outro (outro.html unchanged). (v2/v3: 33.67 s.) v1 (rendered as out/TRRS_S6E15_R1_9x16_v1.mp4) was 33.17 s.

## v4 change (CD: ending still abrupt)
- Keeps her whole faint final /s/ (to source 1090.845, 10 ms crossfade, no Ricardo voicing), then 1.19 s of clean room tone on a held listening shot of Leslie (picture to source 1091.063 + 28-frame hold, camera drift continuing). "CONFIDENCE." holds to 30.97; music bed continuous; outro at 31.37 (was 30.67). Details and verification in EDL.md (v4).

## v3 change (CD: v2 still ends abruptly), superseded by v4
Audio tail per the coordinator's spec: source runs on to 1090.93 before the room-tone crossfade. See EDL.md (v3) for the verification and a caveat: the added 80 ms is most likely the breathy onset of Ricardo's "Oh", not her /s/.

## v2 change (CD: "the last line gets cut off too quickly, complete it")
- "confidence." now has a ~0.57 s natural decay before the outro (was 0.07 s plus a 30 ms fade). The source can't run on: Ricardo's "Oh, okay" starts 80 ms after the word. So the voice crossfades (40 ms) into 0.5 s of room tone from the same recording, fading out, and the picture holds on Leslie for 15 more frames.
- Shifted +0.5 s: outro 30.667, shing 30.337, music-out 30.667 (media 39.867), voice/music/aroll/header/captions ends 30.667, root 33.667. The last caption "confidence." holds to 30.40. The final camera drift is stretched to the new end.
- Voice still -16.0 LUFS / -2.3 dBTP. words.json rebuilt (0 silent words). 1080x1920, 30 fps. Not rendered (queued centrally).

## Script (verbatim to the audio)
RICARDO: How important has Reddit become in all of this now?
LESLIE: On the Reddit thing specifically, we know that over half of Redditors do what they call a final check on Reddit before they make a purchase.
RICARDO: Oh, interesting.
LESLIE: And by the way, guilty, right? Before I book a hotel, before I buy a new running shoe—
RICARDO: Checking Reddit.
LESLIE: I do wanna go to Reddit and get that extra stamp of approval. So that's super important. And Reddit is the number one most trusted source to build consumer confidence.

The question is Ricardo's (checked on video and against the show's burned-in captions; the show-notes transcript mislabels it). The mp4 has "to build" (the brief's script dropped "to").

## EDL
See `EDL.md`. Three segments: A 981.39-984.62 (Ricardo's question), B 1062.93-1074.26, C 1075.23-1090.83. Two internal cuts, both in silences, 15 ms crossfades. The B→C cut removes her false start "So that's a s- and,". Voice -16.0 LUFS / -2.3 dBTP.

## Shot list (reel time)
| time | shot | words |
|---|---|---|
| 0.00-3.23 | Ricardo cam (new crop), name tag "Ricardo Belmar / Host, The Retail Razor Show", punch-in on "Reddit" | "How important has Reddit become in all of this now?" |
| 3.23-7.05 | Leslie cam, name tag, punch-in on "specifically" | "On the Reddit thing specifically, we know that over" |
| 7.05-10.30 | B-roll: hand scrolling the Reddit thread on a phone (Mixkit green screen + composited thread), slow push | "half of Redditors do what they call a" |
| 10.30-13.92 | FULL-SCREEN Reddit thread (r/RunningShoeGeeks "Final check before I buy: are these daily trainers actually worth $160?"), slow scroll from title through post photo | "final check on Reddit before they make a purchase." |
| 13.92-14.57 | Ricardo cam | "Oh, interesting." |
| 14.57-16.52 | Leslie cam, punch-in on "guilty" | "And by the way, guilty, right?" |
| 16.52-17.70 | B-roll: boutique hotel room (Mixkit 4046) | "Before I book a hotel," |
| 17.70-19.52 | B-roll: runner tying her running shoes, slow push (Mixkit 4851) | "before I buy a new running shoe—" |
| 19.52-20.08 | Ricardo cam | "Checking Reddit." |
| 20.08-23.52 | FULL-SCREEN Reddit thread: flick-scroll to top comment "Bought them after reading this sub — zero regrets…" (highlighted on "go to Reddit"); on "stamp of approval" the comment's upvote fills orange, 486→487, a big orange upvote badge stamps down with a ring burst and "+1" | "I do wanna go to Reddit and get that extra stamp of approval." |
| 23.52-30.67 | Leslie cam (faces back for the payoff), punch-ins on "important", "number one", "trusted" | "So that's super important. And Reddit is the number one most trusted source to build consumer confidence." |
| 30.67-33.67 | Outro (unchanged), shing at 30.34 | |

Logo hidden over 7.05-13.92, 16.52-19.52, 20.08-23.52. Captions: R2 style, key words red: Reddit, Redditors, final, check, guilty, stamp, approval, trusted. Ricardo's two clear lines are captioned; his murmurs under her words are not.
SFX: whoosh at 6.9, 10.15, 16.37, 19.93; click + soft impact on the stamp (22.36); shing 29.84. Music "Close Up" 0.2, outro 0.55 (continuous, media 39.37 at the outro).

## B-roll sources and licences (all logged in `assets/LICENSES.md`)
- Reddit thread: real capture was tried first and blocked (`hyperframes capture` → "Prove your humanity"; reddit JSON 403). So it is a faithful rebuild of Reddit's current mobile app thread view, dark mode, Reddit Sans (OFL), orange upvote states, snoo-style avatars, invented generic usernames (tempo_tuesday, milesbeforecoffee, negative_split_, couch2marathon, heel_striker_88), no real names. Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r1/build_reddit.py` → `compositions/reddit.html` + `assets/reddit/thread.html`.
- Phone shot: Mixkit 100059 "A young woman relaxing on the couch with mobile phone" (green screen, `videoFree`). Screen tracked per frame, thread warped in, thumb kept in front (`podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r1/build_phone.py` → `assets/broll/phone_reddit.mp4`).
- Hotel: Mixkit 4046 "White luxury boutique hotel room" (`videoFree`).
- Running shoe: Mixkit 4851 "Girl running during sunset ties her shoelaces" (`videoFree`); a still from it is the photo in the Reddit post.
- Rejected as Restricted License: 13168, 15059, 15060, 14766, 11612, 47879, 35369, 34278, 35386, 36736.

No stat card was added, so no attribution label was needed. The "over half of Redditors" number appears only in her spoken words and captions.

## QA
- `npx hyperframes@0.8.217 check --json`: lint, runtime, layout, motion, contrast and audio are all OK. The remaining warnings are (a) a dense timeline track (the captions file, same as R2), (b) "line unread" reading-time warnings on the Reddit UI body text (illustration under her words, not meant to be read in full), and (c) the unchanged outro. The app chrome over the scrolled thread and the punch-in overflow are marked as intended.
- voice.wav re-transcribed (whisper small.en): matches the script word for word. Whisper mishears Ricardo's "has / this now" as "is / the sound". words.json timings agree within ~0.2 s, and no caption word sits in silence.
- Snapshots: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r1/snaps1/` (every shot; contact sheet `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/reels/r1/sheet1.jpg`), fixes in `snaps2/` (`sheet2.jpg`) and `snaps3/` (`sheet3.jpg`). Fixed after the first pass: the hidden Reddit scene had an opaque background that blanked 14-20 s; the stamp ring showed early; the stamp sat on the captions; the post title was half under the nav on "final check"; the shoe push was too tight.

## Open questions for the CD
1. Reddit UI is rebuilt, not captured (Reddit blocks automated capture). OK as is? If a real thread is wanted, a manual phone screen-recording of a public thread could be dropped in. Real usernames would then show.
2. Dark-mode Reddit was picked because it sits better against the warm brown look. Light mode is a one-line CSS swap.
3. Hotel and shoe shots are footage, about 1.2 s and 1.8 s. Alternative: show r/travel / product-page UI instead.
4. Ricardo's crop is tighter on the left, to clear the burned-in title box and captions. His framing is head-and-torso, a little looser than Leslie's.
5. Ricardo's short "Oh" / "Yeah" murmurs overlap her words at about 12.4, 15.0, 18.4 and 21.5 s. They can't be removed and aren't captioned.
