# Source intake

What to mine from each source, and what tier it supports. Read sources **before** interviewing
— it makes the interview shorter and the questions sharper.

| Source | Extract | Typical tier | Watch for |
|---|---|---|---|
| **Old CVs (every version)** | Dates, titles, employers, education, early claims | B–C | Versions disagree. Every disagreement is a claims-register entry, not a choice to make silently |
| **LinkedIn profile or export** | Dates, titles, skills, recommendations, honors | B | Often stale. Check dates against reality before trusting them |
| **Performance reviews** | Metrics, ratings, manager language, named strengths | **A** | Contains third parties' data. Extract only what is about this person |
| **Recognition and award emails** | Who recognized, when, for what, category | **A** | The strongest tier available to most people, and the most under-used |
| **Project READMEs, repos, commit history** | What was built, when, by whom, technology | **B** | Commit counts are not impact. Look for what the code does |
| **Internal wikis and runbooks** | Ownership, scope, systems supported | B | Usually the best evidence of what someone actually owns |
| **Job descriptions for roles held** | Official scope, level, expected competencies | B | Describes the role, not the performance. Useful for scope, not for achievement |
| **AI-written profile summaries** | Candidate claims to verify | **C at best** | See below — treat with suspicion |
| **Certificates** | Issuer, date, exact scope | **A** | Check what the certificate actually tests. A two-skill language test does not establish overall fluency |

---

## AI-written summaries are input, not evidence

If the person arrives with a profile written by an AI, it is a useful inventory of topics and a
poor record of fact. Such documents reliably:

- promote contributions into ownership,
- attach team results to the individual,
- invent plausible specifics that were never in the source,
- and describe familiarity as expertise.

**Treat every claim in them as C until independently confirmed**, then re-grade. Where two AI
summaries disagree, that disagreement is often the most informative thing in either document —
it usually marks exactly where one of them extrapolated.

## Confidential material

Confidential work belongs in the knowledge base — it is most people's best material. It is
handled by recording it fully and **translating it at the point of use**:

- Mark the file or entry `INTERNAL-ONLY`.
- Maintain a translation table (`14_GLOSSARY_AND_TRANSLATION.md`) mapping internal names to
  externally safe descriptions: a product code name becomes "an order-management platform", a
  named colleague disappears, a table name becomes "a curated data layer".
- Add every internal term to `workspace/redlines.yaml` so `verify.py` fails the build if one
  survives into a rendered PDF.

Never rely on remembering to translate. That is what the redline check is for.

## Recording provenance

Every extracted fact carries where it came from. Use short source codes (`CV-2023`, `REVIEW-Q2`,
`REPO-README`) and define them in `99_SOURCE_MAP.md` if the knowledge base grows that far. A
claim whose source cannot be named is a C.
