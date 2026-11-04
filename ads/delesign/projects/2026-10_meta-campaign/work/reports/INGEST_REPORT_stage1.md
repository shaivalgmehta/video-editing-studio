# Stage 1 Ingest Report: Ad 2A "The fourth way"

Date: 2026-10-22

## Source files found

Only one camera file was present. It was at the project root and has been moved into `/raw`.
The brief was also moved from the root into `/script`.

| File | Container | Video | Resolution (stored) | Displayed | FPS | Duration | Audio | Size |
|---|---|---|---|---|---|---|---|---|
| raw/VID20261022172544.mp4 | MP4 | HEVC, yuv420p, bt709, ~40 Mbps | 3840×2160 | 2160×3840 portrait (rotation=90 flag) | 30 nominal, 29.15 average (variable frame rate, 1895 frames) | 65.00s | AAC stereo 48kHz 256k | 312 MB |

Notes:
- Native vertical phone shot. ffmpeg auto-applies the rotation flag, so all derived files are portrait.
- Variable frame rate. Proxies and the final cut are conformed to constant 30fps.
- Stereo channels are close in level (L RMS -19.2 dB, R RMS -17.0 dB). Downmixed to mono for cleanup.
- Peaks on the source reach -0.7 dBFS. Clipping check is logged below.

## Derived files

| File | Spec |
|---|---|
| work/proxies/VID20261022172544_540p.mp4 | 540×960, H.264 CRF 23, constant 30fps, AAC 128k, 65.00s |
| ads/delesign/projects/2026-10_meta-campaign/work/audio_raw/take01_VID20261022172544.wav | 48kHz, 24-bit PCM, mono, 65.00s |

## Folder layout created

```
/raw
/ads/delesign/brand/go
/ads/delesign/brand/broll  (+ /portfolio)
/ads/delesign/brand/brand  (+ /music)
/script
/work/proxies  /ads/delesign/projects/2026-10_meta-campaign/work/audio_raw  /ads/delesign/projects/2026-10_meta-campaign/work/audio_clean  /ads/delesign/projects/2026-10_meta-campaign/work/transcripts  /ads/delesign/projects/2026-10_meta-campaign/work/edl  /work/hyperframes
/out
```

## Open items for the creative director

- Only one take (one continuous 65s file). If more camera files exist, drop them in `/raw` and re-run ingest.
- `/ads/delesign/brand/go`, `/ads/delesign/brand/broll`, `/ads/delesign/brand/brand` are empty. Needed by Stage 4: Golden Gate B-roll, 3 portfolio pieces, Go screenshots/recordings, logo SVG, fonts, music bed, SFX, and the $85,000 source footnote.
