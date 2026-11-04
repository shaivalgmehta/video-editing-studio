"""Word-level transcript with faster-whisper, in the HyperFrames word-list shape.

Usage: python transcribe_fw.py input.wav output.json [model]
Default model: small.en (CPU, int8).
Output: [{"id":"w0","text":"Did","start":0.00,"end":0.21}, ...]
"""
import sys
import json
from faster_whisper import WhisperModel

src = sys.argv[1]
dst = sys.argv[2]
model_name = sys.argv[3] if len(sys.argv) > 3 else "small.en"

model = WhisperModel(model_name, device="cpu", compute_type="int8")
segments, info = model.transcribe(
    src,
    language="en",
    word_timestamps=True,
    beam_size=5,
    vad_filter=False,
    condition_on_previous_text=False,
)

words = []
for seg in segments:
    for w in seg.words or []:
        words.append({
            "id": f"w{len(words)}",
            "text": w.word.strip(),
            "start": round(w.start, 3),
            "end": round(w.end, 3),
            "prob": round(w.probability, 2),
        })

with open(dst, "w", encoding="utf-8") as f:
    json.dump(words, f, indent=1, ensure_ascii=False)

print(f"{len(words)} words, duration {info.duration:.1f}s, model {model_name}")
print(" ".join(w["text"] for w in words))
