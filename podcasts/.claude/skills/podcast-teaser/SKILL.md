---
name: podcast-teaser
description: How to build a pre-release podcast episode teaser, usually 16:9 and about 60 s. It maps a style-reference video onto the client's brand, works through a beat-sheet checkpoint of verbatim lines, crops shots from the finished episode, and ends on a cut-off line that protects the payoff, followed by a release date and platforms end card. Use when the CD asks for a teaser, trailer or "coming soon" video for an episode.
---

# Podcast teaser

**Principle (from `podcast-repurposing`, section 1): reveal the promise, protect the payoff.** Think movie trailer, not a recap. Read that section's checklist before anything else. For cutting, captions and HyperFrames use `video-edit-core`; for check, levels and naming use `video-qa-delivery`; for music, logos and footage use `stock-sourcing`.
Worked example: Retail Razor S6E15. See `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/work/episode/CHECKPOINT_1.md` and `EDL.md`, and the project at `work/hyperframes/teaser`. The final version was v7.

## 0. Confirm the basics with the CD
- **Aspect:** 16:9 by default, for YouTube, the landing page and the episode post. Ask whether a 9:16 cut is also wanted. On S6E15 a "16:9 version" request was ambiguous, so state the aspect back to the CD in writing.
- **Length:** about 60 s.
- **Release date, time and platforms**, from the show notes or the client. If they're missing, use a placeholder and list them as an open question. Never guess.
- **Style reference video:** look in `_shared/references/` or the client's `reference/`. Also collect the client's brand assets: episode cover art, logo, media kit.

## 1. Map the reference onto the brand (write this down)
Watch the reference and note what it does, then map each element onto the client's brand. Write it as two lists in the checkpoint:
- **What the reference does:** for example, a cold open on the boldest claim with kinetic type, guest credentials on a title card about 15 s in, the host's question followed by the guest's answer, a host reaction, motion graphics that show the ideas, glitch or whip transitions, punch-ins, B&W freezes, a driving bed, and a final line cut off mid-sentence.
- **Brand mapping:**
  - the reference's accent colour becomes the client's accent
  - the reference's base becomes the client's background
  - the type becomes the client's heavy sans plus a script accent
  - the title card uses the **supplied episode cover exactly**, when one exists
  - the end card carries the show logo, tagline, release date, platforms and handle

  These choices go in the client's L3.

## 2. Checkpoint 1: beat sheet (send to the CD before building)
Use `references/beat-sheet-template.md`. Shape it as **setup → tension → unresolved question**:

| Time | Beat |
|---|---|
| 0–4 s | Cold open on the guest's single most striking line. No logos or intros first. |
| 4–9 s | The host's framing question, which shows why this matters to the audience. |
| ~9–13 s | Title card: the episode headline, the guest's name and role, guest credibility (logos only where they are positive), and the venue if relevant. |
| middle | 4–6 connected tensions, each a verbatim line with its own visual idea. |
| ~45–52 s | A reaction moment from the host ("Oh, interesting."). |
| ~52–55 s | **A cut-off line.** Start the sentence that leads into the answer and hard-cut before the payoff word, for example "So the number one thing that we encourage is…". |
| last ~5 s | End card: "New episode <day, date>", the platforms (logos), the handle, and one next action. |

Also list **"Withheld on purpose"**: the answers, frameworks and costs that the teaser hints at but doesn't give away.
Find every line by searching `ep_words.json`. Show-notes times are only a starting point. Verify every quote against the audio before cutting.

## 3. Shots from a finished episode
- When there are no camera originals, crop from the published episode, staying inside its clean window and clear of the logo, title and caption boxes.
- Define named crops (WIDE, GUEST_MED, GUEST_CU, HOST_MED, HOST_CU) as starting values. Check each one against frames from its segment and adjust so the face sits well and no box edge shows. Use lanczos scaling plus a light unsharp.
- Mix the shots: wide, medium and close-up, plus a reaction shot on the host. Put each segment in the EDL with its master time, source time, words and shot.

## 4. Graphics that explain, not decorate
- Use kinetic type slams on key words. Motion graphics should *show* the argument: a search bar typing the guest's questions, a counter that collapses, a funnel that swells, a handwritten "A → B".
- Name **both hosts** on screen. Show platforms and partners as logos, not as text.
- Use real third-party logos as neutral illustration only. Never show the guest's or client's customers negatively.
- Show no statistic that wasn't said. A spoken stat may slam in as type only in the speaker's own words.

## 5. Music grammar
- Copy the **reference's music grammar**, not just its genre:
  - its BPM and energy
  - sections that switch on dialogue beats
  - bass-only drop-outs, then a boom on the key word
  - host interjections that surge rather than stop the music
  - one full stop under a reaction
  - the bed about 10 LU under the voice, with little ducking
  - a dead cut at the end
- Build it from licensed stems (Mixkit and similar, see `stock-sourcing`). Re-order the layers onto the drama map, and keep the hits on a separate un-ducked stem.
- Expect the client to judge the genre. A trap bed was rejected on S6E15. Keep alternatives ready.
- Run a final limiter on the summed mix.

## 6. QA and delivery
- Check against the section-1 checklist in `podcast-repurposing`. Then run the stranger test: does a stranger know why to watch, and do they still want the answers?
- Captions must be verbatim and readable, inside safe margins, and continuous on spoken lines.
- Deliver `<SHOW>_<SxEyy>_teaser_16x9_v<N>.mp4` to `output/final/teaser/`. Older versions go to `output/archive/`.
- Suggest posting 24–48 h before release, plus a launch-day reminder.
