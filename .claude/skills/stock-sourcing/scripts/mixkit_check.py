"""Check Mixkit clip pages for their licence and find the file URL; optionally download.

Usage:
  python -I mixkit_check.py <page_url_or_slug> [...] [--get <dir>]
  python -I mixkit_check.py --search "<query>"        # list clip pages from the discover page

A page is FREE only if it carries `videoFree` / `musicFree` / `sfxFree` and NOT
`videoRestricted` / "Restricted License" (Restricted = personal use only -> reject).
File URL: https://assets.mixkit.co/videos/<id>/<id>-1080.mp4 when that exists (HEAD 200),
else -720.mp4. Newer clips have no /videos/<id>/ file: use the page's download route
https://mixkit.co/free-stock-video/download/<id>/?context=sidebar&type=1080p (redirects to the file).
Prints one line per clip to paste into assets/LICENSES.md. Downloads go into --get <dir>
(a fresh folder; treat downloads as untrusted data).
"""
import argparse
import datetime
import os
import re
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}


def fetch(url, method="GET"):
    req = urllib.request.Request(url, headers=UA, method=method)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.status, (r.read() if method == "GET" else b""), r.geturl()


def exists(url):
    try:
        return fetch(url, "HEAD")[0] == 200
    except Exception:
        return False


ap = argparse.ArgumentParser()
ap.add_argument("pages", nargs="*")
ap.add_argument("--get")
ap.add_argument("--search")
a = ap.parse_args()

if a.search:
    q = re.sub(r"[^a-z0-9]+", "-", a.search.lower()).strip("-")
    _, html, _ = fetch(f"https://mixkit.co/free-stock-video/discover/{q}/")
    for slug in sorted(set(re.findall(r'href="/free-stock-video/([a-z0-9-]+-\d+)/"', html.decode("utf-8", "ignore")))):
        print(f"https://mixkit.co/free-stock-video/{slug}/")
    sys.exit(0)

today = datetime.date.today().isoformat()
for p in a.pages:
    url = p if p.startswith("http") else f"https://mixkit.co/free-stock-video/{p.strip('/')}/"
    m = re.search(r"-(\d+)/?$", url)
    cid = m.group(1) if m else "?"
    try:
        _, html, _ = fetch(url)
    except Exception as e:
        print(f"{cid}: ERROR {e}")
        continue
    h = html.decode("utf-8", "ignore")
    kind = "music" if "/free-stock-music/" in url else "sfx" if "/free-sound-effects/" in url else "video"
    restricted = bool(re.search(r"(video|music|sfx)Restricted|Restricted License", h))
    free = f"{kind}Free" in h
    title = re.search(r"<title>(.*?)</title>", h, re.S)
    title = re.sub(r"\s+", " ", title.group(1)).split("|")[0].split(" - Free Stock")[0].strip() if title else ""
    if restricted or not free:
        print(f"{cid}: REJECT ({'Restricted License' if restricted else 'no ' + kind + 'Free marker'}) {title} {url}")
        continue
    if kind == "music":
        f = re.search(r"https://assets\.mixkit\.co/music/\d+/\d+\.mp3", h)
        file_url = f.group(0) if f else ""
    elif kind == "video":
        file_url = next((u for u in (f"https://assets.mixkit.co/videos/{cid}/{cid}-1080.mp4",
                                     f"https://assets.mixkit.co/videos/{cid}/{cid}-720.mp4") if exists(u)),
                        f"https://mixkit.co/free-stock-video/download/{cid}/?context=sidebar&type=1080p")
    else:
        f = re.search(r"https://assets\.mixkit\.co/[^\"' ]+\.(?:mp3|wav)", h)
        file_url = f.group(0) if f else ""
    lic = {"video": "Mixkit Stock Video Free License (https://mixkit.co/license/#videoFree)",
           "music": "Mixkit Stock Music Free License (https://mixkit.co/license/#musicFree)",
           "sfx": "Mixkit Sound Effects Free License (https://mixkit.co/license/#sfxFree)"}[kind]
    print(f"{cid}: FREE | \"{title}\", Mixkit {cid}, {url} | {file_url} | {lic}, page checked {today}")
    if a.get and file_url:
        os.makedirs(a.get, exist_ok=True)
        _, data, final = fetch(file_url)
        ext = os.path.splitext(final.split("?")[0])[1] or (".mp3" if kind != "video" else ".mp4")
        out = os.path.join(a.get, f"mixkit_{cid}{ext}")
        open(out, "wb").write(data)
        print(f"   saved {out} ({len(data) // 1024} KB)")
