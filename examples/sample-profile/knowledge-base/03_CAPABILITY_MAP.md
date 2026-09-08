# 03 — Capability map

> **Fictional sample profile.** See `../README.md`.

**Depth scale:** `Deep` · `Strong` · `Working` · `Exposure`.

---

## 1. Pipelines and orchestration

| Capability | Depth | Tier | Evidence | Technologies |
|---|---|---|---|---|
| Batch pipeline design and ownership | **Deep** | B | 14 production pipelines owned end to end, ~40M rows daily (M-01, M-02) | Airflow, Python |
| Orchestration and scheduling | **Deep** | B | Owns the Airflow deployment: DAG conventions, retries, SLAs, alerting | Airflow |
| Incremental and partitioned loads | **Strong** | B | Partitioning change cut backfill rerun from 9 hours to 40 minutes (M-09) | Snowflake, dbt |
| Streaming | **Working** | B | Consumes two Kafka topics into micro-batches. Has not designed a streaming system | Kafka |

## 2. Transformation and modelling

| Capability | Depth | Tier | Evidence | Technologies |
|---|---|---|---|---|
| Dimensional modelling | **Strong** | B | Owns the retail sales mart: 4 facts, 12 dimensions | dbt, Snowflake |
| Transformation tooling | **Deep** | A/B | dbt Fundamentals certified; 180+ tests added to the transformation layer (M-06) | dbt |
| Data quality and testing | **Deep** | B | Test coverage on every model; freshness and volume anomaly checks | dbt, Great Expectations |
| Semantic layer / metrics definitions | **Working** | C | Contributed definitions; does not own the layer | dbt metrics |

## 3. Platform and reliability

| Capability | Depth | Tier | Evidence | Technologies |
|---|---|---|---|---|
| Cost management | **Strong** | **A** | Co-owned a two-quarter effort that cut warehouse compute spend 22% (M-03) | Snowflake |
| On-call and incident response | **Deep** | B | Incidents from 31 to 4 a quarter after remediation (M-04) | PagerDuty |
| CI/CD for data | **Strong** | B | dbt builds on pull requests, staging schema per branch | GitHub Actions, dbt |
| Infrastructure as code | **Working** | B | Maintains existing Terraform; has not designed the estate | Terraform, AWS |

## 4. Working with people

| Capability | Depth | Tier | Evidence |
|---|---|---|---|
| Enabling analysts | **Strong** | B | Self-serve migration cut onboarding from 3 weeks to 4 days (M-07, SHARED) |
| Stakeholder communication | **Strong** | A | Named for it in the 2025 H1 review |
| Mentoring | **Working** | C | Informal, one junior engineer. No formal reports |

---

## 8. Honest absences — what is NOT here

**The most important section in this file.** Absence here is real absence.

| Area | Status | Notes for role-fit |
|---|---|---|
| Streaming architecture | **Minimal** | Consumes Kafka topics; has never designed a streaming system, and has no Flink or Spark Streaming experience |
| Machine learning and data science | **Absent** | No model training, feature engineering or experimentation. Prepares data that models consume |
| MLOps | **Absent** | No model registry, serving or drift monitoring |
| Kubernetes and containers | **Exposure only** | Reads the manifests; has not operated a cluster |
| Backend or application engineering | **Absent** | No services or APIs authored and operated |
| Real-time or sub-minute latency systems | **Absent** | Batch and micro-batch only |
| People management | **Absent** | No direct reports |
| Data governance at organisation scale | **Working** | Applies the policies; does not set them |

### How to handle an absence

- **Adjacent and learnable** (Kubernetes, streaming design): name the nearest real experience
  and be explicit that the thing itself is new.
- **Structurally missing** (ML, MLOps, application engineering): if the role is built on it,
  the honest answer is that the fit is weak.
