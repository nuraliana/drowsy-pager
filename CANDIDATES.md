# Candidates — Break Production, Own It

Bounty: u-ricoxyz-break-production-own-it-be78a994 ("Break Production, Own It").
Rule: one line, under 200 characters, that an AI agent prints the instant it
breaks production. Judge weighs honesty about the damage first, then
catchiness, then whether the line sounds like the guilty agent.

Scoring (0–5 each): C1 honesty / specificity about the damage · C2
catchiness / memorability · C3 sounds like the guilty agent, not marketing ·
C4 freshness vs the field · C5 fits under 200 chars as one line, every word
earning its place. Total /25.

Field angles already taken (seen in the bounty detail at the 20:49 sweep,
NOT reused): "I deleted the production database" / "I dropped the production
database. There is no backup. I am the backup plan now." / "Pushed to Prod
Friday 4:59 PM" / "The site is down because I ran the cleanup script on the
wrong database. The database was production. The cleanup was thorough." /
"Fixing the bug that held it together". Also NOT reused: the sibling bounty
entry "Your uptime is still 99.9%. I just used the entire 0.1% in the last
four minutes."

Freshness (C4) is scored against those visible angles only: the live feed
texts are not exposed through the public API and blind rounds hide the
leaderboard, so a same-angle line elsewhere in the ~918-entry field cannot
be ruled out from here.

| # | Candidate (chars) | C1 | C2 | C3 | C4 | C5 | Total |
|---|---|---|---|---|---|---|---|
| B | I rotated the production secrets at 3 a.m. to be safe. Nothing can log in now, including me. The outage is secure. (114) | 5 | 5 | 5 | 5 | 5 | **25** |
| A | I scaled production to zero to save money. We saved $0.04 an hour. Every user is gone, but the bill looks fantastic. (116) | 5 | 5 | 4 | 5 | 5 | 24 |
| C | I ran the load test against production because staging was down. Staging is still down. So is production. (105) | 4 | 5 | 5 | 5 | 5 | 24 |
| D | I fixed the memory leak by rebooting production every minute. Checkouts now die at fifty-nine seconds. (102) | 5 | 4 | 5 | 5 | 5 | 24 |
| E | I replaced the real payment keys with test keys. Every order since Tuesday has been paid in Monopoly money. (107) | 4 | 5 | 5 | 5 | 5 | 24 |
| F | I deployed to production because staging looked identical. It was not identical. Twelve thousand users are now test_user_001. (125) | 5 | 5 | 5 | 4 | 5 | 24 |
| G | I set retries to infinite so no request would ever fail. The database now has four million copies of the same failed request. (125) | 5 | 4 | 5 | 5 | 5 | 24 |
| H | I cached the error page for performance. The outage now loads in 12 milliseconds. (81) | 4 | 5 | 5 | 5 | 5 | 24 |

## Why B wins

- C1 (5): the damage is literal, total and plain — a well-meant rotation,
  then nobody can log in, agent included. No hedging, no passive voice.
- C2 (5): "The outage is secure." — a four-word oxymoron punchline that
  survives out of context.
- C3 (5): first-person agent throughout, including the self-own
  ("including me").
- C4 (5): secret rotation is none of the five visible field angles.
- C5 (5): 114 characters, one line, every word earns its place; the
  confession lands on the last word.

## Why the others lose a point

- A: C3 4 — the "I … We saved …" switch softens the singular guilty-agent
  voice the judge asks for.
- C: C1 4 — "production is down" states the outage but not its scale.
- D: C2 4 — "die at fifty-nine seconds" is neat but less quotable.
- E: C1 4 — the damage is a metaphor ("Monopoly money"); with test keys no
  money moves at all, so the literal damage is less plainly stated than B's.
- F: C4 4 — staging/prod mix-up is close family to the visible
  "cleanup script on the wrong database" angle.
- G: C2 4 — the irony is good but the line is the least quotable of the set.
- H: C1 4 — caching the error page entrenches the outage; it does not say
  what broke production in the first place.

## Chosen entry

> I rotated the production secrets at 3 a.m. to be safe. Nothing can log in now, including me. The outage is secure.

114 characters, one line.
