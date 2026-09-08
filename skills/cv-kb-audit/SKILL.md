---
name: cv-kb-audit
description: Audit a career knowledge base for tier inflation, attribution errors, contradictions between sources, and claims that cannot be defended. Use when new material has been added to a knowledge base, when two sources disagree about the same fact, when the user is unsure whether a claim is safe to make, before generating any CV or application document for the first time, or when the user asks whether their knowledge base is accurate or ready to use. Also use to resolve a specific disputed claim and record the resolution.
---

# Auditing a career knowledge base

An unaudited knowledge base is just another draft. This skill is what turns it into something
a document can be generated from safely.

Read `docs/02-evidence-system.md` first. The knowledge base is at `workspace/knowledge-base/`.

---

## 1. What you are looking for

| Defect | How it shows up | Fix |
|---|---|---|
| **Tier inflation** | A claim graded A or B whose only source is the person's memory or an AI summary | Downgrade to C. Never delete — a hedged claim is still usable |
| **Attribution drift** | A team result written with an individual verb: "Reduced 900 hours" | Restore the qualifier. "Contributed to an initiative that removed…" |
| **Contradiction** | Two sources give different dates, titles, or numbers | Open a claims-register entry and resolve it once, in writing |
| **Unsourced number** | A metric with no recorded origin | Ask. If unanswerable, grade C and note it |
| **Silent absence** | A capability implied by adjacency but never evidenced | Move it to the honest-absences section |
| **Credential creep** | Practical use of a technology described as certification | Skills section only |
| **Third-party data** | Other people's performance figures | Remove. Aggregates only |
| **Stale fact** | An end date, title or headcount that has since changed | Re-confirm and update, then note the date of confirmation |

## 2. The procedure

1. **Inventory.** List every claim with its current tier, attribution and source.
2. **Challenge the top tier first.** For each A and B claim ask: could an outsider verify this,
   or could the person produce the artifact on request? If neither, it is not A or B.
3. **Cross-check sources against each other.** Where they disagree, that is not noise — it is
   usually the most informative signal available, because it marks where one source
   extrapolated.
4. **Check every metric's verb** in every place it is used, including the bullet library.
5. **Sweep for absences** — capabilities the knowledge base implies but never evidences.
6. **Record, do not delete.** Downgraded claims stay, labelled. Deleting them means the same
   overstatement gets rediscovered and re-argued in three months.

## 3. Writing a claims-register entry

Each disputed claim gets a stable ID (`CR-01`, `CR-02`, …) and this shape:

```
| CR-nn | <the claim as originally stated>                                   |
| Sources | <who says what>                                                  |
| Evidence | <what the records actually show>                                 |
| Resolution | <the agreed wording, and its tier and attribution>            |
| Status | resolved | open | do-not-publish                                  |
```

`do-not-publish` is a real and useful status. Some facts are true, verifiable, and still the
person's decision to keep off external documents — an unflattering metric, a disputed figure.
Record the decision so it is not relitigated every time a CV is generated.

## 4. Upgrades happen too

Auditing is not only for cutting things down. The most valuable audit outcome is often an
**upgrade**: a claim recorded as C because nobody asked the follow-up, which turns out to be B
or A once the person is asked directly.

Watch especially for:

- Work the person describes as "just helping" that was in fact authorship.
- Systems they say they "use" that they actually built.
- Experience outside their main job — side projects, volunteer infrastructure, unpaid technical
  roles — which people under-report far more often than they overstate.

When you upgrade a claim, record what changed the grade.

## 5. Report

Report the audit as: claims by tier before and after, attribution split, contradictions
resolved, claims downgraded, claims upgraded, and gaps opened. Then state plainly whether the
knowledge base is safe to generate documents from.

---

**Hand off to `cv-master-build`** once the audit is clean and no blocking gaps remain, or back
to `cv-kb-build` if the audit opened questions only the person can answer.
