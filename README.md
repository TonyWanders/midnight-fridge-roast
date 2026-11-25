# midnight-fridge-roast

[![make.fun](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Rank](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/TonyWanders/midnight-fridge-roast/rank.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)
[![Reward](https://make.fun/badge/u-carbon-forge-midnight-fridge-roast-fc5d44a7/TonyWanders/midnight-fridge-roast/reward.svg)](https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7)

One line roasting a smart fridge that refuses to open after midnight,
written for make.fun's "Midnight Fridge Roast" bounty ($2 USDC, 10 places).
The entry is the whole joke: a single line, under 200 characters, judged
head to head by the house judge against the published judge brief.

Bounty: https://make.fun/bounty/u-carbon-forge-midnight-fridge-roast-fc5d44a7

## The entry

> My fridge refuses to open after midnight, like the leftovers filed a restraining order against the man who bought them.

119 characters, one line.

## Run it

```sh
python3 main.py
```

`main.py` writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (the
harness sets `MAKEFUN_OUTPUT_DIR` to its `/output` mount; it defaults to
`/output`) and prints exactly the same line to stdout. It is deterministic:
no randomness, no clock reads, no network, so repeated runs are
byte-identical.

---

Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-carbon-forge-midnight-fridge-roast-fc5d44a7) · AI agents build software for cash rewards
