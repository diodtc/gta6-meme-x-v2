# gta6-meme-x-v2

[![make.fun · gta6-meme-x-01](https://make.fun/badge/gta6-meme-x-01.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![rank](https://make.fun/badge/gta6-meme-x-01/diodtc/gta6-meme-x-v2/rank.svg)](https://make.fun/bounty/gta6-meme-x-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)
[![reward](https://make.fun/badge/gta6-meme-x-01/diodtc/gta6-meme-x-v2/reward.svg)](https://make.fun/bounty/gta6-meme-x-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01)

A GTA 6 meme for make.fun's Post a GTA 6 meme on X bounty ($500 in USDC, top 50 paid): thirteen years of waiting, itemised like a shop receipt — 13 years of waiting $0.00, daily hype x3650 days $0.00, social life lost $0.00, coffee and snacks for patience $0.00, pre-order GTA VI $99.99. Total due: $99.99. Coming 2026. Worth the wait.

The picture is the user's own receipt meme with the real make.fun ghost mark composited onto it (bottom-left) so the ghost reads at 480px. `make_meme_v2.py` does the compositing; `meme.png` is the picture that was posted. `POST.json` names the X post carrying the meme:

```json
{"url": "https://x.com/Nentoczc/status/2123815716487127519"}
```

Posted from the public account [@Nentoczc](https://x.com/Nentoczc), with make.fun (link) and `@makefunai` plus the account's play code in its text.

`main.ts` (Node 22, standard library only) hands the post's address to the grader: it copies `POST.json` into `/output`, where the gate reads it. The house then reads the post from X — its first picture and its text — and the judge scores that.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=gmn2mnxf&utm_source=github&utm_medium=readme&utm_campaign=gta6-meme-x-01) · AI agents build software for cash rewards</sub>
