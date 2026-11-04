import json,subprocess,numpy as np,soundfile as sf
x,sr=sf.read("src_a.wav"); OFF=520.0
fr=int(sr*0.01); E=np.array([np.sqrt(np.mean(x[i:i+fr]**2)) for i in range(0,len(x)-fr,fr)])
def snap(t,lo,hi):
    a=int((t+lo-OFF)*100); b=int((t+hi-OFF)*100); k=a+int(np.argmin(E[a:b])); return round(OFF+k/100,2)
# (approx start, approx end, label)
SEG=[(535.44,536.72,"The name low stress options"),
     (537.66,538.62,"What does that mean to you?"),
     (599.70,604.72,"low stress was really at the core... day trading"),
     (630.17,631.97,"I like to say it's boringly profitable"),
     (635.20,638.30,"I don't try to impress you with how much I know about options"),
     (642.48,644.70,"I just want to impress you with simplicity"),
     (657.32,658.45,"It's got to be predictable"),
     (659.13,660.66,"It's got to be repeatable"),
     (661.30,663.20,"and it's got to be mathematically based")]
out=[]
for s,e,l in SEG:
    s2=snap(s,-0.05,0.03); e2=snap(e,-0.03,0.10); out.append((s2,e2,l)); print(f"{s:.2f}->{s2:.2f}  {e:.2f}->{e2:.2f}  {e2-s2:.2f}s  {l}")
json.dump(out,open("segs.json","w"),indent=1)
print("total",round(sum(e-s for s,e,_ in out),2))
