import sys,re,urllib.request
for q in sys.argv[1:]:
    try:
        h=urllib.request.urlopen(urllib.request.Request(f"https://mixkit.co/free-stock-video/{q}/",headers={"User-Agent":"Mozilla/5.0"}),timeout=30).read().decode("utf8","ignore")
    except Exception as e: print("==",q,"ERR",e); continue
    ids={}
    for s,i in re.findall(r'free-stock-video/([a-z0-9-]+)-(\d{3,6})/',h): ids.setdefault(i,s)
    print("==",q,":", "; ".join(f"{i} {s}" for i,s in ids.items()))
