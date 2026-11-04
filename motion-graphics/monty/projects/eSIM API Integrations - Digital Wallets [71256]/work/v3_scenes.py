"""v3 motion pass: write each scene's timeline (camera pans between scenes, one-at-a-time builds, slow drift)."""
import re
from pathlib import Path

C = Path(__file__).parent / "hyperframes/monty_wallets/compositions"


def swap(fn, script):
    p = C / fn
    s = p.read_text(encoding="utf8")
    s = re.sub(r"  <script>.*?</script>", lambda m: "  <script>\n" + script.strip("\n") + "\n  </script>", s, flags=re.S)
    p.write_text(s, encoding="utf8")


swap("s01.html", """
    KIT.acc("#s01-hl .acc");
    const tl = gsap.timeline({ paused: true });
    KIT.drift(tl, "#s01-cam", 3.95);
    // "Your users already plan their trips in your wallet."
    // headline -> the wallet -> its trip -> the trip's spend, card by card -> back to the headline
    KIT.build(tl, "#s01-hl .ln:nth-child(1)", 0.05, { d: 0.7 });
    tl.fromTo("#s01-ph", { y: 620 }, { y: 0, duration: 1.0, ease: "expo.out" }, 0.35);
    KIT.build(tl, "#s01-trip", 1.2, { y: 14 });
    KIT.build(tl, "#s01-c1", 1.45, { x: 24, y: 0 });
    KIT.build(tl, "#s01-c2", 1.7, { x: 24, y: 0 });
    KIT.build(tl, "#s01-c3", 1.95, { x: -24, y: 0 });
    KIT.build(tl, "#s01-hl .ln:nth-child(2)", 2.2);
    KIT.panOut(tl, "#s01-stage", 3.15);
    window.__timelines["s01"] = tl;
""")

swap("s02.html", """
    const tl = gsap.timeline({ paused: true });
    // the camera pans in on "Then they land" already in place
    KIT.panIn(tl, "#s02-stage");
    KIT.drift(tl, "#s02-cam", 4.2);
    tl.fromTo("#s02-ph", { y: 560 }, { y: 0, duration: 0.95, ease: "expo.out" }, 0.7);
    // "...and buy data somewhere else."  second line -> where the money went, one by one -> the verdict on the phone
    KIT.build(tl, "#s02-hl .ln:nth-child(2)", 1.85);
    KIT.build(tl, "#s02-c1", 2.05, { x: 24, y: 0 });
    KIT.build(tl, "#s02-c2", 2.25, { x: -24, y: 0 });
    KIT.build(tl, "#s02-c3", 2.45, { x: -24, y: 0 });
    tl.fromTo("#s02-tx2", { opacity: 0, scale: 1.35, transformOrigin: "0% 50%" }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.in" }, 2.88);
    KIT.panOut(tl, "#s02-stage", 3.4);
    window.__timelines["s02"] = tl;
""")

swap("s03.html", """
    KIT.acc("#s03-hl .acc");
    const tl = gsap.timeline({ paused: true });
    // the camera pans onto the map with "Spot the trip." in place
    KIT.panIn(tl, "#s03-stage");
    KIT.drift(tl, "#s03-cam", 7.5);
    // "...your wallet spots the trip"  the route draws to Paris, the pin drops
    tl.to("#s03-route", { strokeDashoffset: 0, duration: 2.7, ease: "power1.inOut" }, 1.0);
    tl.fromTo("#s03-pin", { opacity: 0, y: -240 }, { opacity: 1, y: 0, duration: 0.32, ease: "power3.in" }, 3.75);
    // "...and offers data at the right moment."  the offer opens beside the pin, then the line that names it
    KIT.build(tl, "#s03-nt", 4.9, { x: -30, y: 0 });
    KIT.build(tl, "#s03-hl .ln:nth-child(2)", 5.25);
    KIT.panOut(tl, "#s03-stage", 6.7);
    window.__timelines["s03"] = tl;
""")

swap("s04.html", """
    KIT.acc("#s04-one .acc");
    const tl = gsap.timeline({ paused: true });
    // the camera pans onto the wallet holding the offer
    KIT.panIn(tl, "#s04-stage");
    // "...in one tap."  the tap, the balance changes, the words
    tl.fromTo("#s04-tap", { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power2.out" }, 2.4);
    tl.to(["#s04-btn", "#s04-tap"], { scale: 0.94, duration: 0.09, yoyo: true, repeat: 1, ease: "power2.out" }, 2.72);
    tl.fromTo("#s04-rip", { opacity: 0.9, scale: 0.3 }, { opacity: 0, scale: 1.5, duration: 0.7, ease: "power2.out" }, 2.75);
    tl.to("#s04-tap", { opacity: 0, duration: 0.25, ease: "power2.in" }, 3.1);
    tl.to("#s04-b1", { opacity: 0, y: -24, duration: 0.3, ease: "power2.in" }, 2.85);
    tl.fromTo("#s04-b2", { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.4, ease: "expo.out" }, 3.0);
    KIT.build(tl, "#s04-one .ln", 3.0, { x: -24, y: 0 });
    // "No card, no second checkout."
    KIT.build(tl, "#s04-c1", 3.45, { x: 24, y: 0 });
    KIT.build(tl, "#s04-c2", 4.25, { x: -24, y: 0 });
    // hand-off: the phone travels to where the next scene's phone stands while the rest pans away
    tl.to("#s04-ph", { x: 440, y: -125, duration: 0.6, ease: "power3.inOut" }, 5.25);
    tl.to("#s04-ph", { opacity: 0, duration: 0.2, ease: "none" }, 5.7);
    KIT.panOut(tl, ["#s04-hl", "#s04-one", "#s04-c1", "#s04-c2"], 5.25);
    window.__timelines["s04"] = tl;
""")

swap("s05.html", """
    KIT.acc("#s05-hl .acc");
    const tl = gsap.timeline({ paused: true });
    // the phone is the one from the last scene, landed (its lock screen fades up in place); the headline follows once it settles
    tl.fromTo("#s05-ph", { opacity: 0 }, { opacity: 1, duration: 0.3, ease: "none" }, 0.4);
    KIT.build(tl, "#s05-hl .ln:nth-child(1)", 0.6, { x: -24, y: 0 });
    // "They land online."  -> the notification
    KIT.build(tl, "#s05-nt", 1.0, { x: 30, y: 0 });
    // "And when data runs low, they top up in the app."  -> the data card, its bar drains, then the line
    KIT.build(tl, "#s05-dc", 2.7, { x: -24, y: 0 });
    tl.fromTo("#s05-fill", { scaleX: 1 }, { scaleX: 0.2, duration: 0.8, ease: "power2.inOut" }, 3.0);
    KIT.build(tl, "#s05-hl .ln:nth-child(2)", 3.75);
    // the camera scrolls down into the close
    KIT.panOut(tl, "#s05-stage", 5.05, "y");
    window.__timelines["s05"] = tl;
""")

swap("s06.html", """
    KIT.acc("#s06-hl .acc");
    const tl = gsap.timeline({ paused: true });
    KIT.panIn(tl, "#s06-stage", "y");
    KIT.drift(tl, "#s06-cam", 7.7, { x: 0, y: 26 });
    // one card per clause, left to right
    KIT.build(tl, "#s06-c1", 0.5, { y: 30 });
    tl.to("#s06-arrow", { strokeDashoffset: 0, duration: 0.8, ease: "power2.inOut" }, 0.95);
    tl.fromTo("#s06-head", { opacity: 0 }, { opacity: 1, duration: 0.2, ease: "none" }, 1.7);
    KIT.build(tl, "#s06-c2", 2.6, { y: 30 });
    KIT.build(tl, "#s06-c3", 4.4, { y: 30 });
    KIT.build(tl, "#s06-hl .ln:nth-child(2)", 5.0);
    KIT.panOut(tl, "#s06-stage", 6.9, "y");
    window.__timelines["s06"] = tl;
""")

swap("s07.html", """
    KIT.acc("#s07-hl .acc");
    const tl = gsap.timeline({ paused: true });
    KIT.panIn(tl, "#s07-stage", "y");
    KIT.drift(tl, "#s07-cam", 5.6, { x: 0, y: 26 });
    // "One API covers it all"  the line runs left to right and each step appears as it reaches it
    tl.fromTo("#s07-line", { scaleX: 0 }, { scaleX: 1, duration: 2.0, ease: "none" }, 0.8);
    [1, 2, 3, 4, 5].forEach((k) => KIT.build(tl, `#s07-c${k}`, 0.75 + (k - 1) * 0.45, { y: 18 }));
    KIT.build(tl, "#s07-hl .ln:nth-child(2)", 2.75);
    KIT.panOut(tl, "#s07-stage", 4.8, "y");
    window.__timelines["s07"] = tl;
""")

swap("s08.html", """
    KIT.acc("#s08-hl .acc");
    const tl = gsap.timeline({ paused: true });
    KIT.panIn(tl, "#s08-stage", "y");
    // a slow push-in for the finish
    KIT.drift(tl, "#s08-cam", 7.35, { x: 0, sc: 1.07 });
    KIT.build(tl, "#s08-eb", 0.5);
    KIT.build(tl, "#s08-hl .ln:nth-child(1)", 1.95);
    KIT.build(tl, "#s08-hl .ln:nth-child(2)", 2.95);
    // the address on the music's final hit
    KIT.build(tl, "#s08-url", 4.85, { y: 16 });
    window.__timelines["s08"] = tl;
""")
print("done")
