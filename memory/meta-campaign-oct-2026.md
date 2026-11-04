---
name: meta-campaign-oct-2026
description: "Meta retargeting campaign build from the 16-ad brief — folder-to-brief mapping, approved decisions, landing page plan"
metadata:
  node_type: memory
  type: project
  originSessionId: 1aa45a35-0192-4b97-baef-c09521bf947b
  modified: 2026-10-26T12:14:54.019Z
---

Building the Delesign Meta retargeting campaign from "Delesign_Full_16_Ad_Campaign.pdf" via the Meta API using creds in DelesignAds/.env (NOT the fb MCP, which is a different account). Assets live in Delesign/Marketing/Ad Campaigns. Started 2026-10-26.

Folder names don't match brief numbering. Mapping: Static 1C=1A, 2A=2B, 3B=4A (white-label, confirmed by CD), 4B=5A, 5A/5B=6A, 6A=8A, 7A/7B=9A; Video 2A=2A, 2B=3A, 2C=8B, 2D=6B. Brief's 1B/3B/4A/4B/5B/9B have no creative.

Approved decisions (2026-10-26): single ad set; everything created PAUSED; settings + audience copied from the "Ad persuasion checklist" campaign; $85k salary line in video 2A approved; Print Calgary signed off; no "terms apply" on 6A description; drop "Meet a real Delesign designer" from 2D; static 2A closing line left out. 1C, 5A, 7A, 7B creatives being reworked (create anyway, swap later).

Built 2026-10-26 in ad account act_403278359021461 (the other account in .env has no API permission): campaign "Agency Recurring Design | Lead" 120251214883250253, ad set 120251214883620253, 14 ads, all paused. Statics use BOOK_NOW; videos use BOOK_TRAVEL because placement-customized videos reject BOOK_NOW; both show "Book now". Static 1C, Static 2A, Static 4B and Video 2A point TEMPORARILY at /dedicated-graphic-designer until the new recurring-design page goes live. That page's headline is "We are the dedicated graphic design agency other agencies go to for their recurring design work." The CD dropped the guarantee page, so those ads go to /dedicated-graphic-designer.

Update 2026-10-26: deleted 5B, 7A and 7B. Swapped in new 1C and 5A creatives, the files dated (102626). Meta won't change the conversion event on a published ad set, so I created a new SCHEDULE ad set, 120251215112070253, and deleted the old one. It now holds 10 paused ads. The pixel logged only 1 Schedule event in 28 days. Webflow page /recurring-design-for-agencies (page 6adf42006bdad5ff7942cfba, site 661cf76f6672e3c7b8afecc4) was duplicated from dedicated-graphic-designer and has its hero edited, and the CD published it on 2026-10-26. Static 1C, Static 2A, Static 4B and Video 2A now point there.

**Why:** CD approved these item by item; don't re-ask.
**How to apply:** Use this mapping/name ads by folder label. Landing pages: all 4 existing delesign.com pages share one body and differ only in hero; brief says avoid "unlimited" promises. See [[user-creative-director]].
