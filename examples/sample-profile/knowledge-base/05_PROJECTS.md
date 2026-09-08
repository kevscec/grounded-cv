# 05 — Projects

> **Fictional sample profile.** See `../README.md`.

---

## P1 — Retail analytics warehouse consolidation

**Ownership:** authored the model and the migration; one of three on delivery · **Tier:** B

**The problem.** Four teams maintained their own extracts and had drifted into four
incompatible definitions of "order", so two dashboards could disagree and both be defensible.

**What Robin did.** Authored the dimensional model (4 facts, 12 dimensions) and the source-to-
target mapping. Wrote the migration and the rollback. The cutover plan and stakeholder sign-off
were shared with the platform lead; the analytics team wrote the downstream dashboards.

**Technologies.** dbt, Snowflake, Airflow. Non-obvious part: the incompatible definitions were
a business disagreement, not a technical one, and had to be resolved with the teams before any
model could be correct.

**Outcome.** 11 source systems consolidated (M-08). One definition of "order".

**The story worth telling.** The first cutover attempt was rolled back after two hours because
a legacy extract wrote a status value nobody had documented. The rollback worked, which was the
part that had been built carefully. The second attempt held.

---

## P2 — Data quality and incident reduction

**Ownership:** individual · **Tier:** B

**The problem.** Inherited pipelines that failed loudly and late — 31 incidents in one quarter,
most surfacing when a business user noticed a wrong number on a dashboard.

**What Robin did.** Added 180+ tests to the transformation layer and freshness and volume
anomaly checks *upstream* of it, so a bad load fails before it reaches a model. Made a failing
test block deployment.

**Outcome.** Incidents from 31 to 4 per quarter (M-04). 180+ tests (M-06).

**The story worth telling.** The tests that mattered were not the schema tests, which caught
almost nothing. They were the volume anomaly checks — the failures that mattered were loads
that succeeded with a fraction of the expected rows.

---

## P3 — Warehouse cost reduction

**Ownership:** co-owned with the platform lead · **Tier:** A

**The problem.** Warehouse compute spend growing faster than data volume.

**What Robin did.** Query profiling and pruning, warehouse right-sizing, and moving three daily
jobs nobody read to weekly. The platform lead handled contract and capacity planning.

**Outcome.** 22% reduction across two quarters (M-03, SHARED — never written as an individual
achievement).

**The story worth telling.** The largest single saving was deleting a job. Nobody had asked
whether the report it produced was still read; it was not, and had not been for a year.
