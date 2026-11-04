"""Build the captions scene for a Delesign ad from the cut's word timestamps.

Usage: python build_captions.py [<words.json> <hyperframes_dir> <aroll_duration>] [--project <job dir>]
  With no positionals it rebuilds ad 2A v2 inside the job folder (default: current folder):
  <project>/work/transcripts/2A_aroll_v2_parakeet_words.json -> <project>/work/hyperframes/2A, 43.767 s.
Writes <hyperframes_dir>/compositions/captions.html  (HyperFrames scene)
       <hyperframes_dir>/assets/captions_groups.json  (the groups, read by finish.py for the SRT)

Rules (brief, Stage 4): 2-4 words per chunk, 2 lines max, word-by-word highlight
(active word Sunset Orange, rest white) on a charcoal rounded backing at 85%,
Hanken Grotesk Bold ~64-72px, bottom of the pill anchored at 65% of frame height,
6% side margins, US spelling, "Delesign" spelled exactly.
"""
import argparse
import json
import re
from pathlib import Path
from _paths import project_dir

_ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
_ap.add_argument("words", nargs="?", help="word-timed JSON (aligned)")
_ap.add_argument("hf", nargs="?", help="HyperFrames project folder of the ad")
_ap.add_argument("duration", nargs="?", type=float, help="A-roll duration in seconds")
_ap.add_argument("--project", help="job folder for the 2A defaults (default: current folder)")
_args = _ap.parse_args()
if _args.duration is not None:
    SRC = Path(_args.words); PROJ = Path(_args.hf); DURATION = _args.duration
elif _args.words is None:
    _P = project_dir(_args.project)
    SRC = _P / "work" / "transcripts" / "2A_aroll_v2_parakeet_words.json"; PROJ = _P / "work" / "hyperframes" / "2A"; DURATION = 43.767
else:
    _ap.error("give all three of <words.json> <hyperframes_dir> <aroll_duration>, or none")
OUT_HTML = PROJ / "compositions" / "captions.html"
OUT_JSON = PROJ / "assets" / "captions_groups.json"
SPEECH_END = DURATION - 0.1

# ASR fixes: brand name, plural he says, "coat" not "code". Only spelling, never words.
FIX = {
    "Delisign.": "Delesign.",
    "Delisign": "Delesign",
    "graphic": "graphics",
    "code.": "coat.",
    "long?": "long.",
}

raw = json.load(open(SRC, encoding="utf-8"))
raw = raw if isinstance(raw, list) else raw.get("words", raw)
words = []
for w in raw:
    t = w["text"].strip()
    t = FIX.get(t, t)
    words.append({"text": t, "start": round(float(w["start"]), 3), "end": round(float(w["end"]), 3)})
# Brand name: the ASR never gets "Delesign" the same way twice. Normalize any token that is a mangled
# single-word form, and merge the two-token forms ("Dad design", "Dell design") into one word.
import re as _re
def _brandish(t):
    core = _re.sub(r"[^a-z]", "", t.lower())
    return core in ("delisign", "ddsign", "dellsign", "delesign", "deliesign", "dilesign")
i = 0
while i < len(words):
    t = words[i]["text"]
    punct = _re.search(r"[,.!?]$", t)
    if _brandish(t):
        words[i]["text"] = "Delesign" + (punct.group(0) if punct else "")
    elif t.lower().rstrip(",.") in ("dad", "dell", "deli", "the") and i + 1 < len(words)             and words[i + 1]["text"].lower().rstrip(",.!?") == "design" and t.lower() != "the":
        nxt = words.pop(i + 1)
        p2 = _re.search(r"[,.!?]$", nxt["text"])
        words[i]["text"] = "Delesign" + (p2.group(0) if p2 else "")
        words[i]["end"] = nxt["end"]
    i += 1
# ASR wobbles between "and then the process" and "and there's a process" (script, and 2 of 3 passes): pin the latter.
for i in range(len(words) - 3):
    if [x["text"].lower() for x in words[i:i + 4]] == ["and", "then", "the", "process"]:
        words[i + 1]["text"], words[i + 2]["text"] = "there's", "a"

MAX_WORDS = 4
PAUSE = 0.15
MAX_CHARS = 26   # per group, keeps most groups on one line at 66px within 950px

groups, cur = [], []
for i, w in enumerate(words):
    cur.append(w)
    nxt = words[i + 1] if i + 1 < len(words) else None
    chars = sum(len(x["text"]) for x in cur) + len(cur) - 1
    punct = bool(re.search(r"[,.!?]$", w["text"]))
    gap = (nxt["start"] - w["end"]) if nxt else 0
    nxt_chars = chars + 1 + (len(nxt["text"]) if nxt else 0)
    if not nxt or punct or gap >= PAUSE or len(cur) >= MAX_WORDS or nxt_chars > MAX_CHARS * 1.6:
        groups.append(cur)
        cur = []
if cur:
    groups.append(cur)

# Merge lonely one-word groups: into the previous group when that stays short and open,
# else into the next group when that has room and follows closely.
merged = []
i = 0
while i < len(groups):
    g = groups[i]
    prev_ok = merged and len(merged[-1]) < MAX_WORDS and not re.search(r"[.!?]$", merged[-1][-1]["text"]) \
        and g[0]["start"] - merged[-1][-1]["end"] < 0.3
    nxt = groups[i + 1] if i + 1 < len(groups) else None
    next_ok = nxt is not None and len(nxt) < MAX_WORDS and not re.search(r"[.!?]$", g[-1]["text"]) \
        and nxt[0]["start"] - g[-1]["end"] < 0.3
    if len(g) == 1 and prev_ok:
        merged[-1].extend(g)
    elif len(g) == 1 and next_ok:
        groups[i + 1] = g + nxt
    else:
        merged.append(g)
    i += 1
groups = merged

out_groups = []
for gi, g in enumerate(groups):
    nxt = groups[gi + 1] if gi + 1 < len(groups) else None
    start = g[0]["start"]
    end = g[-1]["end"]
    # show until the next group starts (or 0.35 s after the last word), never past speech end + 0.4
    vis_end = min(nxt[0]["start"], end + 0.35) if nxt else min(end + 0.35, DURATION - 0.04)
    out_groups.append({"id": f"g{gi}", "start": start, "end": end, "visEnd": round(vis_end, 3),
                       "words": [{"text": w["text"], "start": w["start"], "end": w["end"]} for w in g]})

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
json.dump(out_groups, open(OUT_JSON, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

groups_js = json.dumps(out_groups, ensure_ascii=False)

html = f"""<template>
  <style>
    @font-face {{
      font-family: "Hanken Grotesk";
      src: url("assets/fonts/HankenGrotesk-Variable.ttf") format("truetype");
      font-weight: 100 900;
      font-display: block;
    }}
    #root {{
      position: absolute;
      inset: 0;
      pointer-events: none;
      font-family: "Hanken Grotesk", sans-serif;
    }}
    .cap-group {{
      position: absolute;
      left: 0;
      width: 1080px;
      bottom: 672px; /* pill bottom at 1248 = 65% of 1920 */
      display: flex;
      justify-content: center;
      opacity: 0;
      overflow: visible;
    }}
    .cap-pill {{
      max-width: 950px; /* 6% side margins */
      padding: 18px 40px 22px;
      border-radius: 24px;
      background: rgba(30, 41, 59, 0.85); /* Charcoal #1E293B at 85% */
      text-align: center;
      overflow: visible;
    }}
    .cap-line {{
      display: flex;
      justify-content: center;
      gap: 0.32em;
      white-space: nowrap;
      line-height: 1.14;
      font-weight: 700;
      letter-spacing: -0.01em;
    }}
    .cap-word {{
      display: inline-block;
      color: #ffffff;
    }}
  </style>
  <div id="root" data-composition-id="captions" data-width="1080" data-height="1920" data-layout-allow-caption-zone>
    <div id="captions-stage"></div>
    <div id="captions-drv" class="clip" data-start="0" data-duration="{DURATION}" data-track-index="0"
         style="position:absolute;width:1px;height:1px;opacity:0;pointer-events:none"></div>
  </div>
  <script>
    (function () {{
      var GROUPS = {groups_js};
      var FONT = "Hanken Grotesk";
      var BASE = 66, MIN = 54, MAX_LINE = 870; // 950 pill max minus padding
      var ACTIVE = "#FF5532", INACTIVE = "#ffffff";
      var ctx = document.createElement("canvas").getContext("2d");
      function width(text, size) {{
        ctx.font = "700 " + size + "px " + FONT;
        return ctx.measureText(text).width * 1.06;
      }}
      function lineWidth(ws, size) {{
        return ws.reduce(function (t, w, i) {{ return t + width(w.text, size) + (i ? size * 0.32 : 0); }}, 0);
      }}
      function split(ws, size) {{
        if (lineWidth(ws, size) <= MAX_LINE) return [ws];
        var best = null, imb = Infinity;
        for (var s = 1; s < ws.length; s++) {{
          var a = ws.slice(0, s), b = ws.slice(s);
          var wa = lineWidth(a, size), wb = lineWidth(b, size);
          if (wa <= MAX_LINE && wb <= MAX_LINE && Math.abs(wa - wb) < imb) {{ best = [a, b]; imb = Math.abs(wa - wb); }}
        }}
        return best;
      }}
      var stage = document.getElementById("captions-stage");
      GROUPS.forEach(function (g, gi) {{
        var size = BASE, lines = split(g.words, size);
        while (!lines && size > MIN) {{ size -= 2; lines = split(g.words, size); }}
        if (!lines) lines = [g.words];
        var el = document.createElement("div");
        el.className = "cap-group"; el.id = "cap-" + g.id;
        var pill = document.createElement("div"); pill.className = "cap-pill";
        var wi = 0;
        lines.forEach(function (lw) {{
          var line = document.createElement("div"); line.className = "cap-line"; line.style.fontSize = size + "px";
          lw.forEach(function (w) {{
            var span = document.createElement("span"); span.className = "cap-word";
            span.id = "cap-" + g.id + "-w" + (wi++); span.textContent = w.text; line.appendChild(span);
          }});
          pill.appendChild(line);
        }});
        el.appendChild(pill); stage.appendChild(el);
      }});

      var tl = gsap.timeline({{ paused: true }});
      GROUPS.forEach(function (g) {{
        var el = "#cap-" + g.id;
        var t0 = Math.max(0.05, g.start);
        tl.fromTo(el, {{ opacity: 0 }}, {{ opacity: 1, duration: 0.06, ease: "none" }}, t0);
        g.words.forEach(function (w, i) {{
          var ws = el + "-w" + i;
          tl.set(ws, {{ color: i === 0 ? ACTIVE : INACTIVE }}, t0);
          if (i > 0) tl.to(ws, {{ color: ACTIVE, duration: 0.06, ease: "none" }}, Math.max(t0, w.start - 0.03));
        }});
        // hard off at visEnd (= the next group's start), so two groups never overlap
        tl.set(el, {{ opacity: 0 }}, g.visEnd);
      }});
      window.__timelines["captions"] = tl;
    }})();
  </script>
</template>
"""
OUT_HTML.parent.mkdir(parents=True, exist_ok=True)
OUT_HTML.write_text(html, encoding="utf-8")
print(f"{len(words)} words -> {len(out_groups)} groups")
for g in out_groups:
    print(f"{g['start']:6.2f}-{g['visEnd']:6.2f}  " + " ".join(w['text'] for w in g['words']))
