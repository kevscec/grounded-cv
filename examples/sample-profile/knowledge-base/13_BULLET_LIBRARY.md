# 13 — Bullet library

> **Fictional sample profile.** See `../README.md`.

**Tag format:** `B-nn · Tier · Attribution · metric refs`

Use a bullet as written, or tighten it. **Do not strengthen its verb.**

---

## 1. Pipelines and platform

**B-01 · Tier B · IND · M-01, M-02**
> Own 14 production pipelines end to end — design, deployment, on-call and improvement —
> moving roughly 40 million rows a day into the retail analytics warehouse.

**B-02 · Tier B · IND · M-09**
> Re-partitioned the largest fact table by event date rather than load date, cutting a full
> backfill rerun from nine hours to forty minutes and making reprocessing a routine operation
> rather than an overnight event.

**B-03 · Tier B · IND · M-08**
> Consolidated 11 source systems into a single warehouse model, replacing per-team extracts
> that had drifted into four incompatible definitions of "order".

## 2. Reliability and cost

**B-04 · Tier B · IND · M-04**
> Reduced pipeline incidents from 31 to 4 per quarter by adding freshness and volume anomaly
> checks upstream of the transformation layer, so failures surface before they reach a
> dashboard.

**B-05 · Tier A · SHARED · M-03**
> Co-owned a two-quarter cost-reduction effort that cut warehouse compute spend by 22%, through
> warehouse right-sizing, query pruning and moving three unused daily jobs to weekly.

**B-06 · Tier B · IND · M-06**
> Added 180+ tests to the transformation layer — uniqueness, referential integrity, accepted
> ranges and freshness — and made a failing test block the deployment rather than warn.

## 3. Enablement

**B-07 · Tier A · TEAM · M-05**
> Contributed to a self-serve reporting initiative that removed roughly 900 hours a year of
> manual reporting across the commercial teams.

**B-08 · Tier B · SHARED · M-07**
> Jointly delivered the analyst onboarding path — documented models, a query cookbook and a
> sandbox schema — cutting time to a first independent query from three weeks to four days.

---

## Recommended sets by target

| Target | Bullet set |
|---|---|
| Data Engineer | B-01, B-02, B-04, B-06, B-03, B-05 |
| Analytics Engineer | B-06, B-03, B-08, B-05, B-07, B-02 |
| Platform / reliability | B-01, B-04, B-05, B-02, B-06, B-08 |

## Bullets that must never be written

Kept as explicit negatives so a generating model can pattern-match against them.

| Never write | Because | Write instead |
|---|---|---|
| "Removed 900 hours of manual reporting" | M-05 is a **TEAM** metric with an individual verb. This is the single most damaging possible line on this CV | **B-07** |
| "Cut warehouse spend by 22%" | M-03 is **SHARED**. The verb claims sole ownership | **B-05** |
| "Certified in Snowflake and Airflow" | Not certified — see `01` §4 | List under skills |
| "Built the streaming platform" | Consumes two Kafka topics. See `03` §8 | Omit, or describe the consumption honestly |
| "Led the data team" | No reports, no formal lead role | "Mentored one junior engineer" |
| Any bullet naming ORION, DELTA-FEED or a `_prod_v2` table | Internal system names | Translate via `14` |
