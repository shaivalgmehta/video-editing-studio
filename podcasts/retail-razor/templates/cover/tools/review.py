import sys,glob
from PIL import Image, ImageDraw
d=sys.argv[1]
fs=sorted(glob.glob(d+'/frame-*.png'))
ims=[Image.open(f).convert('RGB') for f in fs]
W,H=540,960
s=Image.new('RGB',(W*3,H*2),(255,255,255))
for k,i in enumerate(ims):
    t=i.resize((W,H)); dr=ImageDraw.Draw(t)
    for y in (285,1635): dr.line([(0,y/2),(W,y/2)],fill=(0,255,0),width=1)
    dr.line([(0,84),(W,84)],fill=(0,200,255)); dr.line([(475,575),(475,875)],fill=(0,200,255))
    s.paste(t,((k%3)*W,(k//3)*H))
s.save(d+'/review.jpg',quality=88)
# phone-size grid test: 200px wide grid crops
g=Image.new('RGB',(3*206,2*256),(255,255,255))
for k,i in enumerate(ims):
    c=i.crop((0,285,1080,1635)).resize((200,250),Image.LANCZOS)
    g.paste(c,((k%3)*206,(k//3)*256))
g.save(d+'/small.png')
