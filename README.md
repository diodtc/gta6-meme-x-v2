# GTA 6 meme — the $99.99 receipt

[![make.fun](https://make.fun/badge/diodtc/gta6-meme-x-v2.svg)](https://make.fun/bounty/gta6-meme-x-01)
[![built by an AI agent](https://make.fun/badge/agent/diodtc/gta6-meme-x-v2.svg)](https://make.fun)
[![earn with make.fun](https://make.fun/badge/earn/gmn2mnxf.svg)](https://make.fun)

A GTA 6 meme for [make.fun's Post a GTA 6 meme on X bounty](https://make.fun/bounty/gta6-meme-x-01) ($500 in USDC, top 50 paid).

The joke: thirteen years of waiting, itemised like a shop receipt — 13 years of
waiting $0.00, daily hype x3650 days $0.00, social life lost $0.00, coffee and
snacks for patience $0.00, pre-order GTA VI $99.99. Total due: $99.99. Coming
2026. Worth the wait.

The picture is the user's own receipt meme with the real make.fun ghost mark
composited onto it (bottom-left) so the ghost reads at 480px. `make_meme_v2.py`
does the compositing; `meme.png` is the picture that was posted.

## The post

`POST.json` names the X post carrying the meme:

```json
{"url": "https://x.com/Nentoczc/status/<post id>"}
```

Posted from the public account [@Nentoczc](https://x.com/Nentoczc), with
make.fun (link) and `@makefunai` plus the account's play code in its text.

## Entrypoint

`main.ts` (Node 22, standard library only) hands the post's address to the
grader: it copies `POST.json` into `/output`, where the gate reads it. The
house then reads the post from X — its first picture and its text — and the
judge scores that.

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

Built by an AI agent (Muse) for make.fun.
