# 08 — Impact ledger

> **Fictional sample profile.** Every number below is invented. See `../README.md`.

**Every number, in one place.** If a metric is not on this page, it does not appear in a CV.

## Attribution key

| Code | Meaning | Required phrasing |
|---|---|---|
| `IND` | Robin's own scope or deliverable | "Built…", "Reduced…", "Achieved…" |
| `SHARED` | One of a small number of owners | "Co-owned…", "Jointly delivered…" |
| `TEAM` | A project result Robin contributed to | "Contributed to an initiative that…" |
| `CTX` | Unverified context | Hedge heavily, or omit |

---

## Metrics

| ID | Metric | Value | Attribution | Tier | Source |
|---|---|---|---|---|---|
| M-01 | Production pipelines owned end to end | **14** | IND | B | `REPO-platform`, on-call rota |
| M-02 | Rows processed daily across owned pipelines | **~40 million** | IND | B | `REPO-platform` job metrics |
| M-03 | Warehouse compute spend reduced over two quarters | **22%** | SHARED | **A** | `REVIEW-2025H1` |
| M-04 | Pipeline incidents per quarter, after remediation | **from 31 to 4** | IND | B | On-call log |
| M-05 | Manual reporting hours removed by the self-serve migration | **~900/year** | **TEAM** | **A** | `REVIEW-2025H1`, programme close-out |
| M-06 | Data quality tests added to the transformation layer | **180+** | IND | B | `REPO-transform` |
| M-07 | Analyst onboarding time to first independent query | **3 weeks to 4 days** | SHARED | B | Team retro notes |
| M-08 | Source systems consolidated into the warehouse | **11** | IND | B | `REPO-platform` |
| M-09 | Backfill rerun time after the partitioning change | **9 hours to 40 minutes** | IND | B | Job history |

> **Phrasing note on M-05.** This is the largest number in the ledger and it belongs to a
> programme, not to Robin. It is only ever written as "contributed to an initiative that…".
> Written with an individual verb it becomes the single most damaging line on the CV, because
> anyone who was on that programme would recognize it immediately.

> **Phrasing note on M-03.** Co-owned with the platform lead. "Co-owned a cost-reduction effort
> that cut…" is correct; "Cut warehouse spend by 22%" is not.

## Headline strips

- **General:** 14 production pipelines · ~40M rows daily · 22% warehouse spend reduction (co-owned)
- **Reliability-slanted:** pipeline incidents from 31 to 4 a quarter · 180+ data quality tests
- **Platform-slanted:** 11 source systems consolidated · analyst onboarding from 3 weeks to 4 days

## Do not publish

| ID | Metric | Reason |
|---|---|---|
| M-10 | Pre-remediation incident count in a single quarter | Real and verifiable, but it was inherited, not caused. Robin decided it needs context that a CV cannot carry. See CR-03 |
