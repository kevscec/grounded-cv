# 02 — Positioning

> **Fictional sample profile.** See `../README.md`.

## 1. The honest centre

> Robin builds and operates the batch data platform a retail analytics function runs on — 14
> pipelines, ~40 million rows a day, owned from design through on-call. The distinguishing
> trait is not any single tool: it is that they stay with a system after it ships, which is why
> the incident count fell rather than the backlog growing. Strongest on reliability, testing
> and cost; weakest on streaming and anything requiring a service to be authored.

## 2. Title options, ranked

| # | Label | Fit | Use when | Risk |
|---|---|---|---|---|
| 1 | **Data Engineer** | Strongest | The default. Matches the title held and the work done | None |
| 2 | **Analytics Engineer** | Strong | dbt-centric roles, closer to the business | Undersells the platform and on-call ownership |
| 3 | **Data Platform Engineer** | Good | Infrastructure-leaning roles | Overstates the infrastructure side — see the honest ceiling |
| X | **Senior Data Engineer** | **Not yet, as a title** | — | 4.5 years and no formal seniority. Describe the scope; let them assign the level |

## 3. Summary paragraphs

### 3.1 Primary (~65 words)
> Data engineer who owns a batch platform end to end — 14 production pipelines moving roughly
> 40 million rows a day into a retail analytics warehouse, from design through on-call. Reduced
> pipeline incidents from 31 to 4 a quarter by moving data quality checks upstream, and
> co-owned a cost effort that cut warehouse compute spend 22%. dbt certified.

### 3.2 Reliability-slanted (~60 words)
> Data engineer whose work is mostly what happens after deployment: 180+ tests in the
> transformation layer, freshness and volume anomaly checks upstream of the models, and an
> on-call rotation where the incident count fell from 31 a quarter to 4. Owns 14 production
> pipelines and the Airflow deployment they run on.

### 3.4 One-liner
> Data Engineer · 14 production pipelines, ~40M rows daily · incidents down from 31 to 4 a quarter

## 4. The honest ceiling

| Tempting claim | Reality |
|---|---|
| "Streaming data engineer" | Consumes two Kafka topics into micro-batches. Has never designed a streaming system |
| "Platform engineer" | Maintains existing Terraform; did not design the estate, does not operate Kubernetes |
| "Led the data team" | No reports. Mentored one junior engineer informally |
| "ML engineer" | Prepares data models consume. No training, no serving, no MLOps |
| "Senior" | 4.5 years. The scope argues for it; the tenure does not, and claiming it invites the comparison |

> Stating these honestly is what makes the strong claims credible.

## 5. Differentiators

1. **Stays after deployment.** The incident number fell because someone owned it. Most
   candidates at this level can describe what they built, not what happened to it afterwards.
2. **Treats cost as an engineering problem.** The 22% reduction came from query and scheduling
   decisions, not from a procurement conversation.
3. **Makes analysts independent.** The onboarding path is the kind of work that is invisible
   until it is missing.
