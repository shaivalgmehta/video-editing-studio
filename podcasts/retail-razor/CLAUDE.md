# The Retail Razor Show (client, level 3)

Applies under `podcasts/retail-razor/`. The workspace rules (`../../CLAUDE.md`, L1 skills `video-edit-core`,
`video-qa-delivery`, `stock-sourcing`) and the podcast rules (`../CLAUDE.md`, L2 skills `podcast-repurposing`,
`podcast-reel`, `podcast-teaser`, `podcast-cover`) apply first. This file adds only what is specific to this client.

## Client
- **The Retail Razor Show**: flagship of the Retail Razor podcast network ("the #1 indie podcast network for retail &
  brand leaders"; sister shows Data Blades, Retail Transformers, Blade to Greatness). Season 6 in Oct 2026. Topics: AI in
  retail, agentic commerce, retail media, the human connection in CX. Audience is mostly senior retail leaders and
  watches on mobile.
- **Hosts:** Ricardo Belmar (founder, host, producer) and Casey Golden (co-host). Credit them as
  "Ricardo Belmar / Host, The Retail Razor Show" and "Casey Golden / Co-host, The Retail Razor Show".
- **Tagline:** "Cutting through the clutter" (in the logo lock-up and the reel outro). Long form: "Cutting through the
  clutter in retail strategy, retail technology, and executive leadership."
- **Platforms (always these four, in this order):** Apple Podcasts, Spotify, YouTube, Goodpods. Handle @retailrazor,
  retailrazor.com.
- **Brand files:** `brand/Retail Razor Info Oct 2026.pptx` (media kit; the logo is its image1.png),
  `brand/The Retail Razor Show Podcast Description.docx`.
- **Source footage so far:** the finished episode mp4 only (1920x1080, a burned-in show frame with title box top-left,
  logo box top-right, "Recorded live at…" box bottom-left, captions y ≈ 990–1080). Every shot is a crop that has to
  avoid those boxes. Re-measure the boxes each episode.
- **Episodes:** `episodes/<SxEyy_guest-slug>/`. First job: `episodes/S6E15_leslie-ann-hall/` (guest Leslie Ann Hall,
  Founder & CEO, Iced Media; release Tue 3 Nov 2026). It holds the six reels, the teaser and the covers.

## Brand tokens (as approved for S6E15; details in skill `trrs-style`)
| Token | Value |
|---|---|
| Ground | `radial-gradient(ellipse 90% 60% at 30% 22%, #4a2a1d 0%, #2a1610 45%, #120a07 100%)` (warm brown, from the episode cover) |
| Cream text | `#fbeee6` |
| Brand red | `#e3262b`; highlight `#ff4a55`; caption key words `#ff3b44` |
| Peach labels / active caption word | `#f2b48c`; muted peach `#d9a98a` |
| Type | Montserrat 900 (headlines, captions); Caveat 700 (reel name tags); Caveat Brush (teaser handwriting) |
| Logo | `rr_logo.png` (R mark + "RETAIL RAZOR" + "Cutting through the clutter"); `rr_mark.png` = the R only |

The media kit uses a different system: #16171B ground, red #D81F26, Archivo Black headlines, Space Mono labels. The CD
tried it on teaser v2 and **reverted to the warm brown look above**. Do not use the media-kit system for video.

## Standing CD decisions (from the S6E15 review rounds; apply without re-asking)
Reels (9:16):
1. **No headline or title text in reels.** The only branding is the Retail Razor logo, top-left at left 60 / top 132,
   height 112. It is **hidden whenever full-screen b-roll or a full-screen card is on**.
2. **Full-width speaker window** like the Sharkpreneur reference: x 0, y 325, 1080 x 1270, with a thin red line top and
   bottom. Never a small window or picture-in-picture.
3. **Nothing over faces.** No chips, labels or definitions over the speaker. B-roll and explainer cards play full screen.
4. **B-roll is literal and real.** Show real legacy brands with their real logos, real Reddit scrolling, real UIs and real
   products. Generic mood stock gets rejected (the CD rejected a library shelf for "legacy brands" and a typewriter for
   "decades of signals").
5. **Rebuilt UIs are OK.** Faithful HTML rebuilds of Reddit, AI answers, PDPs, shops and so on are fine, but use invented
   usernames, brands, products and handles, never real people's names.
6. **Never show the guest's clients as negative examples.** Find out who the guest's company works with, and don't use
   those brands as the "bad" or "old" example. (S6E15: Iced Media's clients L'Oréal and its brands, Walmart, LVMH and its
   brands, Moroccanoil.)
7. **No invented numbers.** Cards carry no made-up percentages, counters or figures. A number appears only if the
   speaker says it (it then shows in the captions) or it is a sourced fact logged in LICENSES.md (e.g. a brand's
   founding year with a Wikipedia source).
8. **End with air.** Hold about 0.5–0.6 s after the final word before the outro (the CD chose R1 v2's ~0.57 s tail over v4's 1.2 s hold), picture on the speaker with the camera drift
   continuing, room tone under it. Never clip the last word's tail; if the source runs into the next speaker, crossfade
   into room tone.
9. **List cards end complete.** An R4-style checklist or rules card must show the LAST item ticked before it leaves the
   screen. Hold the finished card about 2 s.
10. **Ricardo's backchannels** ("Okay", "Yeah", "Oh, interesting") are acceptable. Remove one only when it sits in a
    clean gap, and don't caption murmurs that sit under the guest's words.
11. **Music:** Mixkit "Close Up" (1167) is OK as the reel bed **until the client provides the licence for the show theme**
    (imunobeats; imunobeats.com does not resolve). Once the licence arrives, swap the bed in the template.
12. Unclear words: cut the sentence (workspace rule). S6E15 examples: "transact", and "does not continuity" stayed out.
    Ask the CD when the cut changes the meaning.

Teaser (16:9): the approved look is **S6E15 teaser v5**: warm brown/peach glow, Montserrat 900 slams, Caveat Brush
handwriting (the CD picked it from 11 fonts and rejected Mr Dafoe), both hosts named, platform icons rather than text,
the client's own video cover used as supplied for the title card, whip pans with B&W flashes, and continuous captions.
It ends on a line cut off mid-sentence. v6 and v7 (music changes only) were unapproved explorations. See `trrs-teaser`.

Covers: CD review of the S6E15 cover series was still pending when this file was written (2026-11-02). Treat
`trrs-cover` as the current proposal, not an approved look.

## Skills and templates here
| Need | Skill | Template (copy, never edit in place) |
|---|---|---|
| tokens, logo, captions, name tags, outro, sound levels | `trrs-style` | - |
| 9:16 reels from an episode | `trrs-reel` | `templates/reel/` |
| 16:9 episode teaser | `trrs-teaser` | `templates/teaser/` |
| reel cover stills | `trrs-cover` | `templates/cover/` |
| IG/LinkedIn carousels (1080x1350 + PDF) | `trrs-carousel` | S6E15 `work/carousels/` scripts (no template yet) |

Deliverable names: `TRRS_<SxEyy>_R<N>_9x16_v<N>.mp4`, `TRRS_<SxEyy>_teaser_16x9_v<N>.mp4`,
`TRRS_<SxEyy>_R<N>_cover.png`.

## Open items with the client
- Show-theme licence (imunobeats): needed before the theme can replace the Mixkit beds.
- No raw camera ISO files so far, so every crop comes from the finished episode with its burned-in boxes. Ask for clean
  camera files if they exist.
