# 10 — Claims register

> **Fictional sample profile.** See `../README.md`.

---

## CR-01 — "Reduced infrastructure costs by 22%"

| | |
|---|---|
| **Sources** | An earlier CV draft; also phrased this way in a LinkedIn summary |
| **Evidence** | The 2025 H1 review records the 22% figure and names two owners: Robin and the platform lead. The work was jointly planned and split |
| **Resolution** | Downgraded from `IND` to `SHARED`. Wording fixed to "Co-owned a two-quarter cost-reduction effort that cut warehouse compute spend by 22%" — bullet **B-05** |
| **Status** | `resolved` |
| **Decided** | 2026-02-14 |

> The tier did not change; the figure is Tier A either way. **Only the attribution was wrong**,
> which is the failure that costs a reference check.

---

## CR-02 — "Helped with the warehouse migration"

| | |
|---|---|
| **Sources** | Robin's own description in the first interview pass |
| **Evidence** | The repository shows Robin authored the partitioning design, the backfill tooling and the rollback procedure. The commit history and the design document are both theirs |
| **Resolution** | **Upgraded.** "Helped with" understated authorship. Recorded as `IND`, Tier B, and written as bullet **B-02** |
| **Status** | `resolved` |
| **Decided** | 2026-02-14 |

> The audit's most valuable outcome is usually an upgrade like this one. People under-report
> authorship far more often than they overstate it, especially for work they found difficult.

---

## CR-03 — The pre-remediation incident count

| | |
|---|---|
| **Sources** | On-call log; visible in the same record as M-04 |
| **Evidence** | Accurate. The pipelines were inherited in that state; Robin remediated them |
| **Resolution** | The improvement (M-04, "from 31 to 4") is published. The absolute pre-remediation figure is not, because it needs context a CV cannot carry and reads as a failure without it |
| **Status** | `do-not-publish` |
| **Decided** | 2026-02-20 |

> A legitimate use of `do-not-publish`: the fact is true and verifiable, and the decision not
> to lead with it is Robin's. Recording it stops the question being reopened every time a CV is
> generated.
