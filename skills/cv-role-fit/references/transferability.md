# Arguing a partial match

When a required capability is Partial, do not gloss it. Name the nearest real experience, state
the delta, and let the reader judge. Candidates who do this are trusted more than candidates
who blur it, because the blur is usually detectable and the honesty rarely is punished.

## The shape

> *"Has done [the underlying engineering problem] at [scale or context]; [the specific tool]
> would be new."*

Two halves, both required. The first half earns the credibility; the second half is what makes
the first half believable.

**Never** *"familiar with"*, *"exposure to"*, *"working knowledge of"*. Those phrases read as a
bluff even when they are true, because that is how bluffs are phrased.

## Worked patterns

These are examples of the *move*, not a list to copy. Substitute the person's real experience.

| Requirement | Nearest real experience | The argument |
|---|---|---|
| A named orchestrator (Airflow, Dagster, Prefect) | Scheduled orchestration built in-house with retries, resource gating, telemetry, alerting | "Has built the orchestration concerns these tools provide. The DAG framework itself would be new" |
| A named transformation tool (dbt) | Layered transformation, config-as-data modelling, documented field maps, multi-layer validation | "Understands layered transformation and lineage. The tool and its testing conventions would be new" |
| A different cloud warehouse | Warehouse-native SQL, jobs, clusters, catalogs on another platform | "Warehouse SQL and platform operations transfer directly; the dialect is a short ramp" |
| Containers and orchestration | Process lifecycle management, resource gating, concurrency safety, reproducible environments | "Has the operational instincts. Containers themselves are new" |
| A named agent framework | Production agent patterns shipped on a different runtime | "Has shipped the patterns these frameworks implement. The framework APIs are a short ramp" |
| Vector search / RAG | Grounding a model in enterprise truth via a governed semantic layer or schema-driven retrieval | "Solves the same problem with a different mechanism. Vector retrieval specifically is new" |
| CI/CD tooling | Idempotent build-and-validate pipelines, staged commits, documented rollbacks | "Has the discipline; the pipeline tooling is new" |
| Observability platforms | Telemetry, severity classification, a failure taxonomy and alert routing built from first principles | "Built the capability by hand rather than buying it, which usually means understanding it better than a dashboard user" |

## When not to argue it

Some gaps are structural, not adjacent. If the role is built on a capability the knowledge base
lists under honest absences — model training, people management, a discipline never practised —
then the honest output is **weak fit**, and saying so is more useful than a clever sentence.

The test: could this person do the job on day one with a week of ramp-up, or would they be
learning the core of the role while being paid to already know it? If it is the second, the
transferability argument is not honest, and it will not survive the technical screen either.
