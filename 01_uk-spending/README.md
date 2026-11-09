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

## 1. Discover - what the data says

To see where customers spend more than two years ago, I first need to know which spend categories grew between September 2024 and September 2026. So I compare each category’s index at those two points and rank them by growth.

### Q1 · Which categories grew, Sep 2024 → Sep 2026?
Query: [`sql/q1_change_2y.sql`](sql/q1_change_2y.sql)

![Q1](charts/q1_change_2y.png)


**Recurring spend is outpacing everything else.** Per-account spend rose 18% in two years, but unevenly. The fastest-growing categories are recurring, mostly at-home payments: Entertainment +41%, Utilities +28%, Transport +24%, Health +23%. Discretionary, out-of-home spend grew below total: Restaurants +14%, Travel +13%. Groceries (+16%) is the exception — recurring, yet slow.

Entertainment stands alone: 13pp ahead of second place and 2.3x the total rate.


Q1 only shows how much each category grew versus two years ago. All nine went up, so on its own it cannot answer where customers spend more and where they spend less. But total spend rose 18%: any category that grew more slowly than that is one where customers allocated less of their extra money. I redefine “spending less” as losing share of total, and divide each category’s index by the total index.


### Q2 · Which categories gained or lost share of spend?
Query: [`sql/q2_mix.sql`](sql/q2_mix.sql) · rel_idx = category index ÷ total index, Sep 2026 (1.00 = grew at the same pace as total since 2023)

![Q2](charts/q2_mix.png)
Query: sql/q2_mix.sq· rel_idx = category index % total index, Sep 2026( 1. 00 = grew at the same pace as total since 2023)
Char: charts/q2_mix.png

**Only Entertainment is pulling share; dining and travel are losing it.** Entertainment sits at 1.25 — it grew 25% faster than total spend. Services, Utilities, Shopping, Health and Transport cluster at 1.04-1.09, close to total.Restaurants (0.92) and Travel (0.93) are below 1:spend on both still rose, but more slowly than everythign else, so their share of the wallet shrank.


total = 9개 카테고리를 합친 전체 지출의 지수. 2023 평균 = 100. 2026.09엔 121.32.

Q1 and Q2 answered “where”: Entertainment is the fastest-growing category. The task asks for a segment × category, so now I need the segment. The only customer segment this dataset offers is age — three groups, 18-34, 35-54 and 55+. Since Entertainment grew fastest, my assumption is that younger customers, the heaviest entertainment consumers, are driving it. I test that with each age group’s two-year change.
### Q3 · Which age group drives the growth?
Query: [`sql/q3_age.sql`](sql/q3_age.sql) · chart data: [`sql/q3_age_monthly.sql`](sql/q3_age_monthly.sql)

![Q3](charts/q3_age.png)

**The older the account, the faster it grew.** From Sep 2024 to Sep 2026, per-account spend rose 33% for 55+, 20% for 35-54 and 12% for 18-34, against 18% overall. The three groups moved almost together through 2022-2023; from 2025, 55+ pulled away upward. 35-54 and 55 + show a clear year-end peak every December; 18-34 does not.
This rejects the assumption that younger customers drive the growth. Two things this data cannot tell me: which age group spends the most in absolute temrs (each index is relative to that group's own 2023 average), and which group contributes most to total growth (the £ weight of each group is unknown).

## What the three findings say together
Customers are spending more each year, and the increase is going to recurring, at-home payments rather than to eating out or travelling. The shift is strongest among older customers. 
Revolut already has a Subscriptions feature for tracking and blocking recurring payments; whether it is built for a customer base that is adding recurring spend — and reaching the 55+ segment that is adding it fastest —— is the question for the next section.

Q3 reverses the starting assumption. The segment adding spend fastest is not 18-34 but 55+. Growth alone, however, does not justify a feature bet: a segment can grwo quickly from a small base. The next question is therefore size —— how much the 55+ segment spends in absolute terms. This dataset is a per-account index and cannot answer that, so I turn to ONS household expenditure by age.

Decision rule, set before looking at the data: I will target the segment with the highest growth, provided it accounts for at least 25% of UK household spending. Below that threshold, I switch to the largest segment that still grows above the overall rate.



### Q4 · How big is the 55+ segment in £?
Query: [`sql/q4_age_size.sql`](sql/q4_age_size.sql) · Data: ONS Family Spending FYE2023-25, Tables A12-A16 (`data/external/`)

![Q4](charts/q4_age_size.png)

**55+ is a large segment, not a niche.** Households headed by someone aged 50-64 spend the most per week (£688). Households headed by someone aged 30-49 are the largest group in total (£6.7bn a week, 37%). Add up every household headed by someone aged 50 or over and they make up 55% of UK weekly spending.

ONS splits age at 50 and 65, not at 55. So I can only give a range for 55+: 23% if I count 65+ only, 55% if I count everyone 50+, and about 44% if I assume 55-64 is two-thirds of the 50-64 group. The lowest figure is close to the 25% bar I set before running the query. The middle figure clears it easily.

The last time Revolut published its UK customer mix was July 2022: 11% of 4.8m UK customers were 55+. The UK base has since grown to 13m, with no newer split. Even against the lowest market figure (23%), 55+ was under-represented at Revolut by about half. That means two opportunities at once: the 55+ customers already on Revolut are growing their spend fastest (Q3), and most 55+ spenders in the UK are not on Revolut yet.

Two caveats on this comparison. First, the two datasets count different things: ONS counts UK households, the Revolut index counts Revolut accounts. So I use ONS only to answer "how big is the market" and the Revolut data only to answer "how fast is it growing" — I never multiply one by the other. Second, both numbers are dated: the ONS figure is a 2023-25 average and the Revolut 11% is from 2022. An up-to-date 55+ share of Revolut's UK base would be needed to confirm the gap; I list it as the first data gap in section 7.

## What the four findings say together
Customers are spending more each year, and the extra money is going to recurring, at-home payments rather than eating out or travel (Q1, Q2). Older customers are driving this most: 55+ accounts grew 33% in two years, against 18% overall (Q3). That segment is large — at least a quarter of UK household spending — and was under-represented at Revolut the last time the mix was published (Q4).

So the segment is 55+. Whether 55+ customers are also the ones adding recurring spend fastest is a hypothesis, not a fact: this dataset has no age × category split. Revolut already has a Subscriptions feature for recurring payments. Whether that feature reaches the 55+ segment is the question for the next section.