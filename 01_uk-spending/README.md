# 01 UK consumer spending -> next-quarter feature bet

Role assumed: Graduate Product Owner (Technical), UK consumer app · Data: ONS "Revolut spending on debit cards", edition 2026-10-29 · Tools: DuckDB, SQL, Python

## 0. The task
A senior P0 asked, after the Monday metrics review:
> "Show me, with data, where our UK customers spend more and where they spend less than two years ago. Pick one segment × spend category worth betting a feature on next quarter. Tell me why that one, what we'd build, how much it would move, and how we'd know we were wrong. One page by Friday. No numbers, no meeting."

The deliverable is a feature proposal. The analysis exists to back it.

## How I approached it
| Step | Question | Method | Output |
|---|---|---|---|
| 1. Discover | Where is per-account spend shifting? Who drives it? | Segmentation by category, age, channel. 2-year change and share-of-wallet shift. | Q1–Q4 queries + charts |
| 2. Define | What is the opportunity, in one sentence? Is it real? | Cross-check against inflation, cash-to-card shift, new-customer mix. Pre-define success metric. | Problem statement |
| 3. Prioritise | Which feature, and why not the others? | 3 options scored on impact × effort × risk. Check what already exists in the app. | Decision + rejected options |
| 4. Spec | What exactly would we build? | User flow, scope-out, system diagram, event logging. | PRD summary |
| 5. Ship | How do we roll it out safely? | Pilot design: segment, %, duration, control group. | Rollout plan |
| 6. Measure | How much would it move? | Segment size × adoption assumption × spend uplift assumption. Three scenarios. | Impact estimate |
| 7. Learn | How would I know I was wrong? | Stop rules by week. Data this dataset cannot answer. | Limitations + next data request |


Data limits up front: the index is per-account, nominal, UK-only, 2023 = 100. It tells me how fast each category grows, not how big it is. No age x
category cross-tab.
