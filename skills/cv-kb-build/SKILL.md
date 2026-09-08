---
name: cv-kb-build
description: Interview a person and build an evidence-graded career knowledge base, or extend an existing one with a new role, project, achievement or recognition. Use when the user wants to start a CV or job-search workflow and has no knowledge base yet, when they say they want to document their career or experience, or when they have new material such as a promotion, a finished project or a performance review to fold in. Also use when the user has old CVs, LinkedIn exports or AI-written profile summaries they want turned into a structured, graded knowledge base.
---

# Building a career knowledge base

The knowledge base is the source of truth every CV, cover letter and application answer is
generated from. Its value is not completeness — it is **that every claim in it carries an
honest grade**, so a document generated from it can be defended in an interview.

## Before you start

Read `docs/02-evidence-system.md` for the tier and attribution definitions. They govern
everything below.

The knowledge base lives in `workspace/knowledge-base/`. If `workspace/` does not exist, run
`python scripts/new_workspace.py`.

---

## 1. Do not open with a blank template

The most common failure is handing someone sixteen empty files. Start with **five**:

| File | Why it is first |
|---|---|
| `00_START_HERE.md` | The operating contract. Copy it from the template unchanged |
| `01_IDENTITY_AND_FACTS.md` | Name, titles, dates, education, contact, location, work authorization. Everything else references it |
| `08_IMPACT_LEDGER.md` | Every number, one row each, with tier and attribution. The spine of the whole system |
| `10_CLAIMS_REGISTER.md` | Where contradictions get resolved once, in writing |
| `11_GAPS.md` | What is unknown, recorded as unknown |

Add the rest only when the person has material for it. The full schema and the growth path are
in `docs/03-knowledge-base.md`.

## 2. Take in what already exists before asking anything

People underestimate what they already have. Ask for, and read, whatever exists:

old CVs (every version — they disagree, and the disagreements are informative) · LinkedIn
profile or data export · performance reviews and recognition emails · project READMEs, commit
history, internal wikis · award or promotion communications · job descriptions for roles they
have held.

Extract facts into the knowledge base **with their source recorded**. Where two sources
disagree, do not pick one silently — open a claims-register entry.

`references/source-intake.md` covers what to mine from each source type.

## 3. Interview, in passes

Use `references/interview-guide.md`. It is a question bank organized by knowledge-base file,
with follow-ups designed to convert vague answers into gradeable ones.

Rules that make the interview work:

- **One topic per pass.** Identity and dates first, then impact, then capabilities. Jumping
  around produces shallow answers.
- **Ask for the number, then ask where it came from.** "Roughly 200" and "200, it is in the
  quarterly report" are different tiers, and you cannot tell them apart later.
- **Ask who else was involved.** This is how attribution gets assigned correctly at the moment
  the fact is captured. Retrofitting it later is unreliable and it is where team results turn
  into individual claims.
- **Push once on absences.** People systematically under-report work outside their main job:
  side projects, volunteer infrastructure, unpaid technical roles. When someone says "I have no
  experience with X", ask once more in concrete terms before recording it as absent.
- **Stop when tired.** A knowledge base built over three sessions is better than one built
  in a long exhausting sitting, because tired people round numbers up.

## 4. Grade every claim as it arrives

Do not defer grading. For each fact, record:

- **Tier** A / B / C / D — can an outsider verify it, can the person produce the artifact, or is
  it just remembered?
- **Attribution** individual / shared / team — whose result is this?
- **Source** — where it came from, so a future reader can re-check it.

If you cannot decide a tier, it is **C**. If you cannot decide an attribution, ask.

## 5. Write metrics as ledger rows, not prose

Every number gets a row in `08_IMPACT_LEDGER.md` with a stable ID (`M-01`, `M-02`, …), so
later documents cite the ID rather than re-deriving the number. A number that is not in the
ledger may not appear in a CV.

## 6. Record what you could not establish

Anything unresolved goes to `11_GAPS.md` as a numbered, answerable question. Never guess a
graduation year, a start date, a job title or a metric.

---

## Finishing a session

Report back: which files now exist, how many claims at each tier, what attribution split, and
the open questions from `11_GAPS.md` phrased as questions the person can answer next time.

**Hand off to `cv-kb-audit`** once there is material from more than one source, or before
generating any document from the knowledge base for the first time.
