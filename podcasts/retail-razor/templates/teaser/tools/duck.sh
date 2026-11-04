#!/bin/sh
# Sidechain-duck the teaser music bed under the voice. Defaults = the APPROVED S6E15 teaser v5 settings
# (episodes/S6E15_leslie-ann-hall/work/episode/duck.sh): music ~-14 LUFS raw, drops ~12 dB under speech (ratio 4,
# threshold 0.05), recovers in ~200 ms so re-entries after a stop still slam. Hits/risers/booms live in a separate,
# UN-ducked hits.wav. Output is padded/trimmed to exactly DUR seconds.
# (v6/v7 used a gentle duck instead, VOL=0.28 TH=0.25 RA=1.5 ATT=30 REL=300; those were unapproved explorations.)
# Usage: sh duck.sh <music.wav> <voice.wav> <out.wav> [DUR_SECONDS]   env: VOL TH RA ATT REL
set -e
M="$1"; V="$2"; O="$3"; DUR="${4:-60}"
[ -n "$O" ] || { echo "usage: sh duck.sh music.wav voice.wav out.wav [dur]"; exit 1; }
VOL=${VOL:-0.62}
TH=${TH:-0.05}
RA=${RA:-4}
ATT=${ATT:-20}
REL=${REL:-200}
N=$(python -c "print(int(round($DUR*48000)))")
ffmpeg -v error -y -i "$M" -i "$V" -filter_complex \
  "[1:a]aformat=channel_layouts=stereo,volume=2[key];[0:a]volume=$VOL[m];[m][key]sidechaincompress=threshold=$TH:ratio=$RA:attack=$ATT:release=$REL:makeup=1,apad=whole_len=$N,atrim=end_sample=$N[d]" \
  -map "[d]" -ar 48000 -c:a pcm_s16le "$O"
echo "ducked -> $O (VOL=$VOL TH=$TH RA=$RA, $DUR s)"
