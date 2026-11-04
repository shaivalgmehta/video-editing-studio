# TRRS S6E15 teaser: EDL (master timeline 60.00 s, 1920x1080, 30 fps)

Source: `podcasts/retail-razor/episodes/S6E15_leslie-ann-hall/input/S6E15 Leslie Ann Hall.mp4` (1920x1080, 29.97 fps). The source is the finished episode. It has a purple show frame, logo boxes in the top-left (x<425, y<160) and top-right (x>1700, y<185), a "Recorded live at SHOPTALK" box at the bottom-left (x<450, y>950), and burned-in captions below y≈995. The camera is a single locked wide two-shot. Every crop must stay inside the clean window, which runs x 80–1835 and y 185–990, and must avoid those boxes.

## Crops (source pixels → scaled to 1920x1080, lanczos, then light unsharp)
- WIDE   : x=230  y=185 w=1440 h=810   (both people)
- L_MED  : Leslie medium, x=870  y=185 w=960 h=540
- L_CU   : Leslie close-up, x=1060 y=185 w=736 h=414   (head + shoulders; keep her eyes about 1/3 down)
- R_MED  : Ricardo medium, x=110  y=185 w=960 h=540
- R_CU   : Ricardo close-up, x=250  y=185 w=736 h=414
Treat these as starting values. Verify each one against frames from the actual segment, and adjust x/y so the face sits well and no logo, frame edge or caption pixel shows.

## Segments
| # | master in–out | source in–out | words (first … last) | shot(s) |
|---|---|---|---|---|
| S1 | 0.00–4.90 | 438.25–443.15 | "AI search is a mirror for what the world thinks about your brand." | L_CU |
| S2 | 4.90–9.50 | 261.75–266.35 | "how AI is really impacting discovery and the whole consumer shopping process." | R_MED to 7.30, then WIDE |
| GAP | 9.50–12.50 | — | title card (black video, silent voice) | black |
| S3a | 12.50–16.90 | 468.78–473.18 | "traditional SEO really rewards more of those legacy brands," | L_MED |
| S3b | 16.90–21.75 | 481.50–486.35 | "With GEO, it's a much bigger opportunity for indie brands, challenger brands," | L_CU |
| S4a | 21.75–26.85 | 504.75–509.85 | "they'll have 200 products in their portfolio and they want to rank for everything." | L_MED |
| S4b | 26.85–30.35 | 510.55–514.05 | "But the truth is, they might not deserve to rank for everything." | L_CU |
| S5 | 30.35–32.70 | 825.00–827.35 | "We call it bottom funnel bloat," | WIDE |
| S6 | 32.70–37.95 | 855.05–860.30 | "what we call this new customer journey at Iced Media is from vibes to validation." | L_MED |
| S7 | 37.95–44.25 | 945.55–951.85 | "but is this the best product for me? Is it worth the price? Are there competitors I'm not aware of?" | L_CU |
| S8 | 44.25–53.25 | 1065.45–1074.45 | "We know that over half of Redditors do what they call a final check on Reddit before they make a purchase." + Ricardo "Oh, interesting" | L_MED to 52.35, then R_CU (Ricardo's "Oh interesting" is ≈1073.55–1074.40) |
| S9 | 53.25–55.40 | 514.10–516.25 | "So the number one thing that we encourage is" (hard cut before "being") | L_CU |
| END | 55.40–60.00 | — | black (end card is a graphic) | black |
