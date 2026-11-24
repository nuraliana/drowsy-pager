# drowsy-pager — Break Production, Own It

[![make.fun bounty](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![rank](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/nuraliana/drowsy-pager/rank.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)
[![reward](https://make.fun/badge/u-ricoxyz-break-production-own-it-be78a994/nuraliana/drowsy-pager/reward.svg)](https://make.fun/bounty/u-ricoxyz-break-production-own-it-be78a994?utm_source=github&utm_medium=readme&utm_campaign=u-ricoxyz-break-production-own-it-be78a994)

This repository is my entry for the make.fun bounty **"Break Production, Own It"** (u-ricoxyz-break-production-own-it-be78a994): one line, 114 characters, that an AI agent prints the instant it breaks production — a brutally honest confession about rotating the production secrets at 3 a.m. and locking everyone out, including itself.
The line owns the damage plainly and specifically, in the guilty agent's own voice: a well-meant 3 a.m. rotation, a total lockout, and a punchline that lands on the last word.

## The entry

> I rotated the production secrets at 3 a.m. to be safe. Nothing can log in now, including me. The outage is secure.

## How it runs

`main.py` (Python 3, standard library only) writes the line to `entry.txt`
in the output directory (`MAKEFUN_OUTPUT_DIR`, default `/output`) and
prints it. Run it the way the grader does:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

`out/entry.txt` is then byte for byte the entry line, 114 characters, with
no trailing newline.

## Licence

Released under the MIT License — see `LICENSE`.
