"""Objective comparison of speech-cleanup candidates.

Usage: python audio_metrics.py reference.wav candidate1.wav [candidate2.wav ...]

The reference (raw) file defines the speech / pause mask so every candidate is
measured over the same regions. Metrics per file:

  speech_rms_db   RMS over speech frames
  pause_rms_db    RMS over pause frames (residual room + noise)
  snr_db          speech_rms_db - pause_rms_db
  decay_ms        mean time for energy to fall 20 dB after a speech offset
                  (reverb-tail proxy, lower = drier)
  hf_ratio_db     energy 4-8 kHz minus energy 300-3000 Hz over speech frames
                  (very low = dull/underwater, much higher than raw = harsh/lispy)
  sib_ratio_db    energy 5-9 kHz minus energy 1-4 kHz on the loudest 10% of
                  high-band frames (sibilance proxy)
  mod_depth_db    std-dev of frame RMS within speech (pumping proxy if it rises
                  a lot versus raw)
  pause_flat      spectral flatness in pauses, 0..1 (low = tonal residue,
                  possible metallic/warbly artifact)
"""
import sys
import json
import numpy as np
import soundfile as sf

FRAME = 0.02   # s
HOP = 0.01     # s


def load(path):
    x, sr = sf.read(path, dtype="float32", always_2d=True)
    return x.mean(axis=1), sr


def frames(x, sr):
    n = int(FRAME * sr)
    h = int(HOP * sr)
    if len(x) < n:
        return np.zeros((0, n), dtype=np.float32)
    count = 1 + (len(x) - n) // h
    idx = np.arange(n)[None, :] + h * np.arange(count)[:, None]
    return x[idx]


def rms_db(fr):
    r = np.sqrt(np.mean(fr ** 2, axis=1) + 1e-12)
    return 20 * np.log10(r + 1e-12)


def band_energy_db(fr, sr, lo, hi):
    win = np.hanning(fr.shape[1])
    spec = np.abs(np.fft.rfft(fr * win, axis=1)) ** 2
    freqs = np.fft.rfftfreq(fr.shape[1], 1 / sr)
    m = (freqs >= lo) & (freqs < hi)
    e = spec[:, m].sum(axis=1) + 1e-12
    return 10 * np.log10(e)


def spectral_flatness(fr):
    win = np.hanning(fr.shape[1])
    spec = np.abs(np.fft.rfft(fr * win, axis=1)) ** 2 + 1e-12
    gm = np.exp(np.mean(np.log(spec), axis=1))
    am = np.mean(spec, axis=1)
    return gm / am


def speech_mask(level_db):
    # Adaptive: speech = frames within 25 dB of the 95th percentile level,
    # pause = frames below the 20th percentile + 3 dB. Smooth with a short hold.
    top = np.percentile(level_db, 95)
    floor = np.percentile(level_db, 20)
    speech = level_db > top - 25
    pause = level_db < floor + 3
    # hold speech for 5 frames (50 ms) either side
    k = 5
    sp = np.convolve(speech.astype(int), np.ones(2 * k + 1), mode="same") > 0
    pause = pause & ~sp
    return sp, pause


def decay_time_ms(level_db, speech, hop_s, drop_db=20.0):
    # For each speech offset, find the time until level falls drop_db below the
    # level at the offset. Cap the search at 600 ms.
    out = []
    cap = int(0.6 / hop_s)
    for i in range(1, len(speech)):
        if speech[i - 1] and not speech[i]:
            start_lvl = level_db[i - 1]
            target = start_lvl - drop_db
            j = i
            while j < min(len(level_db), i + cap) and level_db[j] > target:
                j += 1
            if j < i + cap:
                out.append((j - i) * hop_s * 1000)
            else:
                out.append(cap * hop_s * 1000)
    return float(np.mean(out)) if out else float("nan"), len(out)


def tail_db(level_db, speech, hop_s, lo_s=0.10, hi_s=0.35):
    # Mean level in the window lo_s..hi_s after each speech offset, relative to
    # the mean level of the last 100 ms of that speech run. Floor-independent
    # reverb-tail proxy: more negative = drier. Offsets followed by new speech
    # inside hi_s are skipped.
    lo, hi = int(lo_s / hop_s), int(hi_s / hop_s)
    pre = int(0.10 / hop_s)
    vals = []
    for i in range(pre, len(speech) - hi):
        if speech[i - 1] and not speech[i] and not speech[i:i + hi].any():
            ref = np.mean(level_db[i - pre:i])
            vals.append(np.mean(level_db[i + lo:i + hi]) - ref)
    return float(np.mean(vals)) if vals else float("nan"), len(vals)


def analyse(path, sr_ref, sp_mask, pause_mask):
    x, sr = load(path)
    assert sr == sr_ref, f"sample rate mismatch in {path}"
    fr = frames(x, sr)
    n = min(len(fr), len(sp_mask))
    fr = fr[:n]
    sp = sp_mask[:n]
    pa = pause_mask[:n]
    lvl = rms_db(fr)
    speech_rms = float(np.mean(lvl[sp])) if sp.any() else float("nan")
    pause_rms = float(np.mean(lvl[pa])) if pa.any() else float("nan")
    mid = band_energy_db(fr, sr, 300, 3000)
    hf = band_energy_db(fr, sr, 4000, 8000)
    lowb = band_energy_db(fr, sr, 1000, 4000)
    sib = band_energy_db(fr, sr, 5000, 9000)
    hf_ratio = float(np.mean((hf - mid)[sp]))
    sib_frames = sib[sp]
    low_frames = lowb[sp]
    top = sib_frames >= np.percentile(sib_frames, 90)
    sib_ratio = float(np.mean((sib_frames - low_frames)[top]))
    mod_depth = float(np.std(lvl[sp]))
    flat = spectral_flatness(fr)
    pause_flat = float(np.mean(flat[pa])) if pa.any() else float("nan")
    decay, n_off = decay_time_ms(lvl, sp, HOP)
    tail, n_tail = tail_db(lvl, sp, HOP)
    return {
        "file": path,
        "speech_rms_db": round(speech_rms, 1),
        "pause_rms_db": round(pause_rms, 1),
        "snr_db": round(speech_rms - pause_rms, 1),
        "decay_ms": round(decay, 0),
        "tail_db": round(tail, 1),
        "tails": n_tail,
        "offsets": n_off,
        "hf_ratio_db": round(hf_ratio, 1),
        "sib_ratio_db": round(sib_ratio, 1),
        "mod_depth_db": round(mod_depth, 1),
        "pause_flat": round(pause_flat, 3),
    }


def main():
    ref = sys.argv[1]
    cands = sys.argv[2:]
    x, sr = load(ref)
    lvl = rms_db(frames(x, sr))
    sp, pa = speech_mask(lvl)
    rows = [analyse(ref, sr, sp, pa)] + [analyse(c, sr, sp, pa) for c in cands]
    keys = ["speech_rms_db", "pause_rms_db", "snr_db", "decay_ms", "tail_db", "hf_ratio_db",
            "sib_ratio_db", "mod_depth_db", "pause_flat"]
    print(f"speech frames: {int(sp.sum())}  pause frames: {int(pa.sum())}  offsets: {rows[0]['offsets']}")
    print("file".ljust(34) + "".join(k.rjust(14) for k in keys))
    for r in rows:
        name = r["file"].replace("\\", "/").split("/")[-1]
        print(name.ljust(34) + "".join(str(r[k]).rjust(14) for k in keys))
    with open(sys.argv[1].rsplit(".", 1)[0] + "_metrics.json", "w") as f:
        json.dump(rows, f, indent=2)


if __name__ == "__main__":
    main()
