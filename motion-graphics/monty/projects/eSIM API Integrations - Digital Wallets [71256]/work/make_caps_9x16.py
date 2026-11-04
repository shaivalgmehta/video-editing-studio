"""9:16 copy of the v1 caption script (wrapping pill above the Shorts UI).
Build compositions/caps.html (house captions) from transcript.json.

Groups of up to 4 words, broken at punctuation or a pause >= 0.15 s. VO is placed at +0.3 s in the film.
Spelling follows the client's script (eSIM, 200-plus); words stay verbatim to the audio.
"""
import json, html, sys
from pathlib import Path

HERE = Path(__file__).parent
OFF = 0.3
FIX = {"ESIM": "eSIM", "MontyESIM,": "Monty eSIM,", "200": "200-plus", "plus": None}

words = json.loads((HERE / "transcript.json").read_text(encoding="utf8"))
toks = []
for w in words:
    t = FIX.get(w["text"], w["text"])
    if t is None:  # "plus" folds into "200-plus"
        toks[-1]["end"] = w["end"]
        continue
    parts = t.split()  # "Monty eSIM," came through as one token: split its time evenly
    step = (w["end"] - w["start"]) / len(parts)
    for j, p in enumerate(parts):
        toks.append({"text": p, "start": w["start"] + j * step, "end": w["start"] + (j + 1) * step})

# hand-set phrases (script punctuation); each must match the next N transcript words
PHRASES = [
    "Your users already plan", "their trips in your wallet.", "Then they land,", "and buy data somewhere else.",
    "With the Monty eSIM API,", "your wallet spots the trip", "and offers data", "at the right moment.",
    "Users pay from their balance", "in one tap.", "No card,", "no second checkout.",
    "They land online.", "And when data runs low,", "they top up in the app.",
    "You earn on every bundle,", "keep balances in your wallet,", "and give users", "one more reason", "to open your app.",
    "One API covers it all,", "in 200-plus countries and regions.",
    "Monty eSIM.", "Travel data,", "built into your wallet.",
]
groups, k = [], 0
for p in PHRASES:
    n = len(p.split())
    grp = toks[k:k + n]
    said = [x["text"].strip(".,?!").lower() for x in grp]
    want = [x.strip(".,?!").lower() for x in p.split()]
    if said != want:
        sys.exit(f"phrase mismatch: {p!r} vs {said}")
    groups.append([{**grp[0], "text": p.split()[0]}] + [{**x, "text": t} for x, t in zip(grp[1:], p.split()[1:])])
    k += n
assert k == len(toks), (k, len(toks))

rows = []
for g, grp in enumerate(groups):
    s = grp[0]["start"] + OFF - 0.06
    nxt = groups[g + 1][0]["start"] + OFF - 0.06 if g + 1 < len(groups) else None
    e = grp[-1]["end"] + OFF + 0.25
    if nxt is not None:
        e = min(max(e, grp[-1]["end"] + OFF + 0.05), nxt)
    rows.append((round(s, 2), round(e, 2), " ".join(x["text"] for x in grp)))

divs = "\n".join(
    f'      <div class="cap" id="cap{k:02d}"><span>{html.escape(t)}</span></div>' for k, (_, _, t) in enumerate(rows)
)
times = ",\n      ".join(f'["#cap{k:02d}", {s}, {e}]' for k, (s, e, _) in enumerate(rows))

out = f"""<template>
  <style>
    #root {{ position: absolute; inset: 0; }}
    /* house captions: Montserrat, white on a soft navy pill, low centre */
    .cap {{ position: absolute; left: 0; top: 1450px; width: 1080px; text-align: center; opacity: 0; visibility: hidden; }}
    .cap span {{ display: inline-block; padding: 10px 28px 12px; border-radius: 18px; background: rgba(19, 41, 75, 0.86);
      font-family: "Montserrat", sans-serif; font-weight: 600; font-size: 44px; line-height: 1.2; color: #fff; max-width: 860px; }}
  </style>
  <div id="root" data-composition-id="caps" data-width="1080" data-height="1920" data-layout-allow-overlap>
{divs}
  </div>
  <script>
    const tl = gsap.timeline({{ paused: true }});
    // [group, open, close] in film seconds, from work/transcript.json via work/make_caps.py
    [
      {times}
    ].forEach(([sel, s, e]) => {{
      tl.set(sel, {{ visibility: "visible" }}, s);
      tl.fromTo(sel, {{ opacity: 0, y: 12 }}, {{ opacity: 1, y: 0, duration: 0.14, ease: "power2.out" }}, s);
      tl.to(sel, {{ opacity: 0, duration: 0.1, ease: "power2.in" }}, e - 0.1);
      tl.set(sel, {{ opacity: 0, visibility: "hidden" }}, e);
    }});
    window.__timelines["caps"] = tl;
  </script>
</template>
"""
(HERE / "hyperframes/monty_wallets_9x16/compositions/caps.html").write_text(out, encoding="utf8")
for r in rows:
    print(r)
