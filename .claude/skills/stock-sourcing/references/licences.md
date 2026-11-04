# Licence log and source notes

## assets/LICENSES.md template (one per HyperFrames project)
```
# Asset sources and licences: <CLIENT> <project> <deliverable>
Every item was checked on its own page on the date shown. Restricted/personal-use items were rejected (listed at the end).

## Video
| File | Source (title, id, page URL) | File URL | Licence (+ check date) |
|---|---|---|---|
| broll/hotel.mp4 | "White luxury boutique hotel room", Mixkit 4046, https://mixkit.co/free-stock-video/... | https://assets.mixkit.co/videos/4046/4046-1080.mp4 | Mixkit Stock Video Free License (https://mixkit.co/license/#videoFree), page marked videoFree, checked YYYY-MM-DD |

## Music / SFX / Images / Logos / Fonts   (same columns)
## Built in HTML (no third-party asset): list mock UIs, invented names
## Rejected: ids + reason (e.g. "49141 Restricted License")
```
Note edits made (trimmed, cropped, recoloured, composited) in the Source column.

## Per-source notes
| Source | Licence | Credit | Notes |
|---|---|---|---|
| Mixkit video/music/SFX | Mixkit Free License (videoFree / musicFree / sfxFree) | not required | Restricted License clips exist; check each page. Music tracks are fine for paid ads. |
| Pexels / Pixabay video | Pexels / Pixabay Content License | not required | Allowed in ads; no use that implies endorsement by people shown; scripts get 403. |
| Pixabay SFX (media-use bundle) | Pixabay Content License | not required | Already logged in earlier projects as "bundled with the HyperFrames media-use skill". |
| Wikimedia Commons logos | usually Public domain (text logo) + trademark | not required for PD | Show the brand as itself; no implied endorsement; keep file page URL + LicenseShortName. CC-BY files need the credit line. |
| Google Fonts | SIL OFL 1.1 | not required | Log family name + repo path. |
| Client-supplied (logos, b-roll, cover art) | client's | — | "Client-supplied; use only for <client> promotion". |
| Show/theme music from the client | unknown until the client confirms | — | Don't use without a written licence; ask the CD. |

## Enabling AI-generated video later
Status 2026-11-02: unavailable. To add a provider, any one of:
- **OpenAI (Sora)**: set a valid `OPENAI_API_KEY` with video access in the environment; test with a one-off small request before planning shots. (Current key → 401.)
- **Higgsfield**: reconnect the claude.ai Higgsfield connector (claude.ai → Settings → Connectors), top up credits, check `balance` before generating.
- **HeyGen via the media-use skill**: add the HeyGen API key that skill asks for; its docs list which generators it routes to.
- **Local LTX** (HyperFrames fallback): needs Apple Silicon or a CUDA GPU; not this laptop.
When one works, record it in this file and in the L1 stock-sourcing SKILL.md.

Rules once available:
- Only for illustrative shots no real footage can provide (abstract concepts, impossible camera moves). Never to depict a real person, a real brand's product, a real place or event as if filmed, and never to generate or alter a speaker's face or voice.
- Literal-match rule still applies; CD approves AI shots by name in the review list.
- Log provider, model, date, full prompt, seed and the provider's commercial-use terms in LICENSES.md.
