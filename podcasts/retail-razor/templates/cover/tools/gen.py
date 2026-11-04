"""Generate a TRRS reel-cover HyperFrames project (index.html + compositions/cN.html) from a JSON config.

Generalised from S6E15 work/covers/gen.py. One 1080x1920 cover per second; export cover in slot i (0-based, sorted by number) at (i + 0.5) s.
Usage:
  python gen.py --config covers.json --project <cover project dir> --cutinfo <cut_info.json from bake.py>
covers.json (see covers.sample.json):
  {"show": "THE RETAIL RAZOR SHOW", "episode": "S6E15", "guest_line": "WITH GUEST NAME, COMPANY",
   "guest_alt": "Guest Name",
   "covers": {"1": {"lines": [["DO YOU CHECK", [], 120, 960], ["REDDIT", ["REDDIT"], 205, 640], ["BEFORE YOU BUY?", [], 120, 960]],
                    "prop": "reddit", "face_x": 700, "sub": null}, ...}}
  lines = [text, key words shown red, max font px, max width px]; a line narrower than 960 leaves room for the prop
  beside it. A word "->" (or the arrow character) draws the red arrow glyph. prop = one of PROPS below or "none".
  face_x = x (px) where the guest's face centre lands. Optional "dy" nudges the cutout vertically. sub = optional line under the headline.
Guest image per cover: assets/img/guest_rN_glow.png (from bake.py); cut_info.json gives its w/h/face-x.
"""
import argparse, json
from PIL import ImageFont

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
ap.add_argument("--config", required=True)
ap.add_argument("--project", required=True, help="HyperFrames cover project dir (has assets/fonts/Montserrat.ttf)")
ap.add_argument("--cutinfo", required=True, help="cut_info.json written by bake.py")
a = ap.parse_args()

PROJ = a.project.rstrip("/\\") + "/"
CFG = json.load(open(a.config, encoding="utf8"))
INFO = json.load(open(a.cutinfo, encoding="utf8"))
COVERS = {int(k): v for k, v in CFG["covers"].items()}
FONT = ImageFont.truetype(PROJ + "assets/fonts/Montserrat.ttf", 100)
FONT.set_variation_by_axes([900])
SCALE = 1.6   # cutout scale on the cover
PAD = 70      # glow padding baked around the cutout (bake.py P)
MAXW = 960


def width100(s):
    return FONT.getlength(s.replace("→", "MM").replace("->", "MM"))


def fit(s, cap, maxw=MAXW):
    return int(min(cap, maxw * 100 / width100(s) * 0.97))


ARROW = ('<svg class="ar" viewBox="0 0 120 80" aria-hidden="true"><path d="M6 40 H92 M70 14 L100 40 L70 66" '
         'fill="none" stroke="currentColor" stroke-width="16" stroke-linecap="square"/></svg>')


def line_html(text, keys, size, cid, i):
    out = []
    for w in text.split(' '):
        if w in ('→', '->'):
            out.append(ARROW)
        elif w.strip('.?') in keys:
            out.append(f'<span class="key">{w}</span>')
        else:
            out.append(w)
    return f'<div id="{cid}-l{i}" class="ln" style="font-size:{size}px">{" ".join(out)}</div>'


PROPS = {
    'none': '',
    'reddit': '''
    <div id="{c}-prop" class="prop" style="left:700px; top:{ky}px;">
      <div class="rd-badge">
        <svg viewBox="0 0 100 100" aria-hidden="true"><path d="M50 14 L84 52 H64 V84 H36 V52 H16 Z" fill="#fff"/></svg>
      </div>
    </div>''',
    'geo': '''
    <div id="{c}-prop" class="prop geo" style="right:60px; top:322px;">
      <span class="geo-old">SEO</span>
      <svg class="geo-ar" viewBox="0 0 120 80" aria-hidden="true"><path d="M6 40 H92 M70 14 L100 40 L70 66" fill="none" stroke="#f2b48c" stroke-width="14"/></svg>
      <span class="geo-new">GEO</span>
    </div>''',
    'crack': '''
    <div id="{c}-prop" class="prop ai" style="left:70px; top:{ky}px;">
      <div class="ai-q"><span class="ai-spark">&#10022;</span> AI answer</div>
      <div class="ai-row"><b>1</b><i style="width:120px"></i></div>
      <div class="ai-row hot"><b>2</b><em>Your brand</em></div>
      <div class="ai-row"><b>3</b><i style="width:96px"></i></div>
      <svg class="ai-crack" viewBox="0 0 270 210" aria-hidden="true">
        <path d="M150 0 L132 46 L158 72 L120 118 L146 150 L112 210" fill="none" stroke="#120a07" stroke-width="9" stroke-linejoin="miter"/>
        <path d="M132 46 L92 62 M158 72 L210 90 M120 118 L72 126 M146 150 L196 176" fill="none" stroke="#120a07" stroke-width="5"/>
        <path d="M150 0 L132 46 L158 72 L120 118 L146 150 L112 210" fill="none" stroke="#ff4a55" stroke-width="3" transform="translate(3 1)"/>
      </svg>
    </div>''',
    'rules': '''
    <div id="{c}-prop" class="prop rules" style="right:60px; top:318px;">
      <div class="rule"><span>RULE</span><b>1</b><svg viewBox="0 0 40 40"><path d="M7 21 L16 30 L33 10" fill="none" stroke="#fff" stroke-width="6"/></svg></div>
      <div class="rule"><span>RULE</span><b>2</b><svg viewBox="0 0 40 40"><path d="M7 21 L16 30 L33 10" fill="none" stroke="#fff" stroke-width="6"/></svg></div>
      <div class="rule"><span>RULE</span><b>3</b><svg viewBox="0 0 40 40"><path d="M7 21 L16 30 L33 10" fill="none" stroke="#fff" stroke-width="6"/></svg></div>
    </div>''',
    'funnel': '''
    <div id="{c}-prop" class="prop" style="left:660px; top:{ky}px; width:360px; height:410px;">
      <svg viewBox="0 0 390 470" width="360" height="410" aria-hidden="true">
        <defs>
          <radialGradient id="{c}-pool" cx="50%" cy="45%" r="60%"><stop offset="0" stop-color="#ff4a55"/><stop offset="1" stop-color="#b3141b"/></radialGradient>
        </defs>
        <path d="M18 24 H372 L262 190 H128 Z" fill="rgba(251,238,230,0.06)" stroke="#fbeee6" stroke-width="6" stroke-linejoin="round"/>
        <path d="M128 190 H262 L236 262 H154 Z" fill="rgba(251,238,230,0.06)" stroke="#fbeee6" stroke-width="6" stroke-linejoin="round"/>
        <ellipse cx="195" cy="368" rx="186" ry="96" fill="url(#{c}-pool)" stroke="#ffd2c4" stroke-width="3" stroke-dasharray="10 9"/>
        <text x="195" y="380" text-anchor="middle" font-family="Montserrat" font-weight="900" font-size="30" letter-spacing="2" fill="#fbeee6">SAME CUSTOMERS</text>
      </svg>
    </div>''',
    'valid': '''
    <div id="{c}-prop" class="prop vchip" style="left:612px; top:{ky}px;">
      <div class="v-num">02</div>
      <div class="v-body">
        <div class="v-title">VALIDATION</div>
        <div class="v-pills"><span class="v-fill">BEST FOR ME?</span><span>WORTH IT?</span></div>
      </div>
    </div>''',
}

CSS = '''
    @font-face { font-family: "Montserrat"; src: url("assets/fonts/Montserrat.ttf") format("truetype"); font-weight: 100 900; font-display: block; }
    #root { position: absolute; inset: 0; overflow: hidden; font-family: "Montserrat", sans-serif;
      background: radial-gradient(ellipse 90% 60% at 30% 22%, #4a2a1d 0%, #2a1610 45%, #120a07 100%); }
    #root .glowbg { position: absolute; left: 260px; top: 760px; width: 1000px; height: 1000px; border-radius: 50%;
      background: radial-gradient(circle, rgba(227,38,43,0.22) 0%, rgba(227,38,43,0.08) 40%, rgba(227,38,43,0) 70%); }
    #root .logo { position: absolute; left: 60px; top: 318px; height: 96px; filter: drop-shadow(0 2px 10px rgba(0,0,0,0.6)); }
    #root .show { position: absolute; left: 192px; top: 330px; color: #f2b48c; font-weight: 800; font-size: 28px; letter-spacing: 0.13em; line-height: 1.4; }
    #root .head { position: absolute; left: 60px; width: 960px; color: #fbeee6; font-weight: 900; letter-spacing: -0.01em; z-index: 4;
      text-shadow: 0 0 40px rgba(255,150,100,0.30), 0 6px 26px rgba(0,0,0,0.65); }
    #root .ln { line-height: 1.0; white-space: nowrap; margin-bottom: 8px; }
    #root .key { color: #ff4a55; text-shadow: 0 0 34px rgba(227,38,43,0.70), 0 6px 26px rgba(0,0,0,0.6); }
    #root .ar { height: 0.62em; width: 0.93em; vertical-align: 0.05em; color: #ff4a55; filter: drop-shadow(0 0 18px rgba(227,38,43,0.7)); }
    #root .sub { margin-top: 18px; font-weight: 700; font-size: 44px; letter-spacing: -0.005em; line-height: 1.15; color: #fbeee6; white-space: normal; text-shadow: 0 4px 18px rgba(0,0,0,0.7); }
    #root .sub b { color: #f2b48c; font-weight: 800; }
    #root .les { position: absolute; z-index: 2; }
    #root .fade { position: absolute; left: 0; top: 1320px; width: 1080px; height: 600px; z-index: 3;
      background: linear-gradient(180deg, rgba(18,10,7,0) 0%, rgba(18,10,7,0.78) 42%, rgba(18,10,7,0.96) 100%); }
    #root .guest { position: absolute; left: 60px; top: 1556px; z-index: 5; color: #f2b48c; font-weight: 800; font-size: 28px; letter-spacing: 0.16em; }
    #root .guest i { display: inline-block; width: 56px; height: 4px; background: #e3262b; vertical-align: 0.3em; margin-right: 18px; font-style: normal; }
    #root .prop { position: absolute; z-index: 3; }
    /* R1 reddit */
    #root .rd-badge { width: 170px; height: 170px; border-radius: 50%; background: #ff4500; display: flex; align-items: center; justify-content: center;
      box-shadow: 0 0 0 8px rgba(255,69,0,0.22), 0 14px 40px rgba(0,0,0,0.55), 0 0 60px rgba(255,69,0,0.45); }
    #root .rd-badge svg { width: 104px; height: 104px; }
    #root .rd-tag { position: absolute; left: 190px; top: 56px; padding: 12px 18px; border-radius: 30px; background: #1a1a1b; border: 2px solid #343536;
      color: #d7dadc; font-weight: 800; font-size: 25px; letter-spacing: 0.08em; white-space: nowrap; display: none; }
    /* R2 geo */
    #root .geo { display: flex; align-items: center; gap: 14px; height: 96px; }
    #root .geo-old { font-weight: 900; font-size: 34px; color: rgba(251,238,230,0.55); padding: 8px 16px; border: 3px solid rgba(251,238,230,0.35); border-radius: 8px;
      text-decoration: line-through; text-decoration-color: #ff4a55; text-decoration-thickness: 5px; }
    #root .geo-ar { width: 54px; height: 36px; }
    #root .geo-new { font-weight: 900; font-size: 42px; color: #fff; background: #e3262b; padding: 8px 20px; border-radius: 8px; letter-spacing: 0.02em;
      box-shadow: 0 0 36px rgba(227,38,43,0.6); }
    /* R3 ai card */
    #root .ai { width: 330px; padding: 24px 24px 26px; background: #f6efe9; border-radius: 18px; transform: rotate(5deg);
      box-shadow: 0 18px 50px rgba(0,0,0,0.6), 0 0 0 3px rgba(227,38,43,0.6), 0 0 50px rgba(227,38,43,0.35); }
    #root .ai-q { font-weight: 800; font-size: 28px; color: #3a2a24; margin-bottom: 14px; }
    #root .ai-spark { color: #e3262b; }
    #root .ai-row { display: flex; align-items: center; gap: 12px; height: 50px; margin-top: 8px; padding: 0 12px; border-radius: 10px; background: #e8ddd5; }
    #root .ai-row b { font-weight: 900; font-size: 24px; color: #7a645a; }
    #root .ai-row i { height: 12px; border-radius: 6px; background: #c9b8ad; display: block; }
    #root .ai-row.hot { background: #fff; box-shadow: inset 0 0 0 3px #e3262b; }
    #root .ai-row.hot b, #root .ai-row.hot em { color: #e3262b; font-style: normal; font-weight: 900; font-size: 28px; }
    #root .ai-crack { position: absolute; left: 0; top: 0; width: 100%; height: 100%; }
    /* R4 rules */
    #root .rules { display: flex; gap: 12px; height: 104px; align-items: center; }
    #root .rule { position: relative; width: 96px; height: 96px; border-radius: 14px; background: rgba(18,10,7,0.7); border: 3px solid #e3262b;
      box-shadow: 0 0 30px rgba(227,38,43,0.4); text-align: center; }
    #root .rule span { position: absolute; left: 0; right: 0; top: 12px; color: #f2b48c; font-weight: 800; font-size: 17px; letter-spacing: 0.18em; }
    #root .rule b { position: absolute; left: 0; right: 0; top: 28px; color: #fbeee6; font-weight: 900; font-size: 56px; line-height: 1; }
    #root .rule svg { position: absolute; right: -12px; bottom: -12px; width: 40px; height: 40px; border-radius: 50%; background: #e3262b; padding: 4px; }
    /* R6 validation chip */
    #root .vchip { display: flex; align-items: center; gap: 16px; padding: 16px 20px; border-radius: 16px; background: rgba(18,10,7,0.72);
      border: 4px solid #e3262b; box-shadow: 0 0 40px rgba(227,38,43,0.45), 0 14px 40px rgba(0,0,0,0.55); }
    #root .v-num { color: #f2b48c; font-weight: 900; font-size: 32px; }
    #root .v-title { color: #ff4a55; font-weight: 900; font-size: 34px; letter-spacing: 0.01em; }
    #root .v-pills { display: flex; gap: 8px; margin-top: 8px; }
    #root .v-pills span { font-weight: 800; font-size: 16px; letter-spacing: 0.06em; color: #fbeee6; padding: 6px 10px; border-radius: 20px; border: 2px solid rgba(251,238,230,0.6); white-space: nowrap; }
    #root .v-pills .v-fill { background: #fbeee6; color: #120a07; border-color: #fbeee6; }
'''


def scene(n, cfg):
    c = f'c{n}'
    top = 448
    y = top
    lines_html = []
    key_y = None
    for i, (t, keys, cap, maxw) in enumerate(cfg['lines']):
        size = fit(t, cap, maxw)
        lines_html.append(line_html(t, keys, size, c, i))
        if maxw < 960 and key_y is None:
            key_y = (y, size)
        y += size * 1.0 + 8
    sub_html = ''
    if cfg.get('sub'):
        sub_html = f'<div id="{c}-sub" class="sub">{cfg["sub"]}</div>'
        y += 18 + 44 * 1.15 * (2 if len(cfg['sub']) > 34 else 1)
    head_bottom = y
    inf = INFO[str(n)]
    head_top = head_bottom - 40 + cfg.get('dy', 0)
    w = inf['w'] * SCALE
    left = cfg['face_x'] - inf['fx'] * SCALE
    img_top = head_top - PAD * SCALE
    # prop vertical: centred on its anchor line
    ky = 0
    if key_y and cfg['prop'] != 'none':
        ly, ls = key_y
        ky = int(ly + ls / 2 - {'reddit': 85, 'crack': 120, 'funnel': 150, 'valid': 60}.get(cfg['prop'], 0))
        if cfg['prop'] == 'funnel':
            ky = top + 8
    if cfg['prop'] == 'crack':
        ky = int(head_bottom + 90)
    prop = PROPS[cfg['prop']].replace('{c}', c).replace('{ky}', str(ky))
    return f'''<template>
  <style>{CSS}  </style>
  <div id="root" data-composition-id="{c}" data-width="1080" data-height="1920" data-layout-allow-overflow data-layout-allow-overlap>
    <div id="{c}-all" class="clip" data-start="0" data-duration="1" data-track-index="0" style="position:absolute; inset:0;">
      <div id="{c}-glowbg" class="glowbg"></div>
      <img id="{c}-les" class="les" src="assets/img/guest_r{n}_glow.png" alt="{CFG.get("guest_alt", "Guest")}"
        style="left:{left:.0f}px; top:{img_top:.0f}px; width:{w:.0f}px;">
      <div id="{c}-fade" class="fade"></div>
      <img id="{c}-logo" class="logo" src="assets/img/rr_logo.png" alt="The Retail Razor Show">
      <div id="{c}-show" class="show">{CFG.get("show", "THE RETAIL RAZOR SHOW")}<br>{CFG["episode"]}</div>
      <div id="{c}-head" class="head" style="top:{top}px;">
        {chr(10).join("        " + l for l in lines_html).strip()}
        {sub_html}
      </div>{prop}
      <div id="{c}-guest" class="guest"><i></i>{CFG["guest_line"]}</div>
    </div>
  </div>
  <script>
    (function () {{
      const tl = gsap.timeline({{ paused: true }});
      tl.set("#{c}-head", {{ opacity: 1 }}, 0);
      window.__timelines["{c}"] = tl;
    }})();
  </script>
</template>
'''


for n, cfg in COVERS.items():
    open(PROJ + f"compositions/c{n}.html", "w", encoding="utf-8").write(scene(n, cfg))

hosts = "\n".join(
    f'      <div id="c{n}" data-composition-id="c{n}" data-composition-src="compositions/c{n}.html" data-start="{i}" data-duration="1" '
    f'data-track-index="{i + 1}" data-track-kind="graphics" data-width="1080" data-height="1920" style="z-index: {i + 1}"></div>'
    for i, n in enumerate(sorted(COVERS)))
TOTAL = len(COVERS)
open(PROJ + "index.html", "w", encoding="utf-8").write(f'''<!doctype html>
<html lang="en" data-resolution="portrait">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
    <style>
      * {{ margin: 0; padding: 0; box-sizing: border-box; }}
      html, body {{ width: 1080px; height: 1920px; overflow: hidden; background: #120a07; }}
      #root {{ position: relative; width: 1080px; height: 1920px; overflow: hidden; background: #120a07; }}
    </style>
  </head>
  <body>
    <!-- TRRS {CFG["episode"]} reel covers. One cover per second (in cover-number order); export stills at (slot + 0.5) s.
         GENERATED by tools/gen.py from covers.json: do not hand-edit, change the config and re-run. -->
    <div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL}" data-width="1080" data-height="1920">
{hosts}
    </div>
    <script>
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
''')
print("ok", sorted(COVERS))
