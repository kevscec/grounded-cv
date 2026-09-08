# Fit assessment — Northstar Analytics, Senior Data Engineer

> **Fictional example.** See `../../README.md`.

**Posting:** remote (EU) · full-time · 6 days old · 40 applicants · senior band stated.
**Assessed:** 2026-03-02.

---

## VERDICT: **Good fit — apply, and address the seniority question before they raise it.**

Every core requirement is Deep or Strong. Two named nice-to-haves are genuinely thin, and one
hard number is short. None of the gaps sits in the honest-absences section as structural, which
is what separates this from a stretch.

---

## WHY IT FITS

| Their requirement | Score | Evidence |
|---|---|---|
| Design, build and own batch pipelines | **Deep** | 14 pipelines owned end to end, ~40M rows daily (M-01, M-02) |
| SQL and Python | **Deep** | Daily, across the platform |
| dbt in production | **Deep** | Certified; 180+ tests authored in the transformation layer (M-06) |
| Cloud warehouse — Snowflake | **Deep** | The warehouse Robin owns |
| Orchestrator — Airflow | **Deep** | Owns the deployment, not just the DAGs |
| **Own data quality and testing** | **Deep** | Incidents from 31 to 4 a quarter by moving checks upstream (M-04) |
| **Warehouse cost as a first-class concern** | **Strong**, Tier A | Co-owned a 22% reduction (M-03) — a stated nice-to-have that Robin can evidence with a review record |
| Make data self-serve for analysts | **Strong** | Onboarding from 3 weeks to 4 days (M-07, SHARED) |
| On-call | **Deep** | Already on the rotation for what they build |
| Written communication | **Strong**, Tier A | Named for it in the 2025 H1 review |
| Retail domain (nice to have) | **Strong** | Current employer is retail |

**Lead with:** the incident reduction and the cost work. The first is the clearest evidence of
staying with a system after it ships; the second is a nice-to-have most applicants will not be
able to evidence at all.

## WHERE IT'S THIN

1. **"5+ years" — Robin has 4.5.** Short by six months against a stated number. Not worth
   inflating, and not worth apologising for; the scope argues the case. Do not use "Senior" as
   a self-applied title (see `02` §2) — let them assign the level.
2. **Streaming — Minimal, and they ask for it in the main list.** Robin consumes two Kafka
   topics into micro-batches and has never designed a streaming system. This is the gap most
   likely to matter. **Argue it, do not hide it:** has built the reliability and quality
   concerns a streaming system needs, on batch; Flink and streaming design would be new.
3. **Infrastructure as code — Working.** Maintains existing Terraform, did not design the
   estate. "Comfortable with" is a fair claim; "owns" is not.
4. **Mentoring — Working.** One junior engineer, informally, no reports. They ask for
   mentoring, not for management, so this is closer than it looks — but do not inflate it.

## BLOCKERS AND ECONOMICS

- **Work authorization:** EU remote, Robin is in Portugal. Clean.
- **Level:** the posting is senior and Robin is targeting senior. Aligned.
- **Compensation:** band stated at senior level. No mismatch to manage.
- **Volume:** 40 applicants after 6 days is low. Effort here is well spent.

## HOW TO POSITION IT

**Title on the CV:** `Data Engineer`. Not "Senior" — the tenure invites a comparison that the
scope wins on its own.

**Bullet set:** the Data Engineer set from `13` (B-01, B-02, B-04, B-06, B-03, B-05), with B-04
and B-05 promoted to first and second, because data quality ownership and cost are the two
requirements Robin evidences most strongly and that other applicants usually cannot.

**Silent on:** streaming design, Kubernetes, anything implying people management. The CV does
not name the gaps; it simply does not claim them.

**Prepared for the screen:**

> *"I've built the reliability and data-quality practice a streaming system needs — upstream
> anomaly checks, alerting, on-call ownership — on batch. Streaming design itself, and Flink
> specifically, would be new to me."*

## RECOMMENDATION

**Apply.** Raise the seniority question yourself in the first conversation rather than letting
it sit — 4.5 years against a stated 5 is a fact they will find, and it is much weaker as a
discovery than as an opening.
