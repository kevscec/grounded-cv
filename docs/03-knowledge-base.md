# The knowledge base

One directory of Markdown files describing one person's career, where every claim carries a
tier and every metric carries an attribution.

Lives at `workspace/knowledge-base/`. Templates in `templates/knowledge-base/`.

## Why files, and why Markdown

Plain files are diffable, portable, editable by a human without a tool, and readable by any
agent. They also load **selectively**: an agent assessing a job posting reads the capability map
and the gaps file, not the whole career.

The numbering is deliberately non-contiguous so files can be added later without renumbering,
and so a reference to `08_IMPACT_LEDGER.md` means the same thing in every knowledge base built
with this framework.

## The schema

### Core — start with these five

| File | Holds |
|---|---|
| `00_START_HERE.md` | The operating contract: tiers, attribution, redlines, read order. Copy unchanged; edit only the redlines |
| `01_IDENTITY_AND_FACTS.md` | Names, titles, dates, education, certifications, contact, location, work authorization, targets |
| `08_IMPACT_LEDGER.md` | Every number, one row each, with a stable ID, tier and attribution |
| `10_CLAIMS_REGISTER.md` | Disputed claims, resolved once with a stable ID |
| `11_GAPS.md` | What is unknown, recorded as unknown |

### Recommended — add as material accumulates

| File | Holds |
|---|---|
| `02_POSITIONING.md` | Title options ranked by defensibility, summary variants, the honest ceiling, differentiators |
| `03_CAPABILITY_MAP.md` | Capabilities with depth, tier and evidence — **and the honest-absences section** |
| `05_PROJECTS.md` | One entry per project: problem, personal contribution, technology, outcome, the story worth telling |
| `13_BULLET_LIBRARY.md` | Pre-written, externally safe bullets tagged with tier, attribution and metric refs |

### Optional

`04_TECHNOLOGY_INVENTORY.md` · `06_DIFFERENTIATOR.md` · `07_WAYS_OF_WORKING.md` ·
`09_RECOGNITION.md` · `12_ROLE_FIT_GUIDE.md` · `14_GLOSSARY_AND_TRANSLATION.md` ·
`99_SOURCE_MAP.md`

`14_GLOSSARY_AND_TRANSLATION.md` is only optional if there is no confidential material. If
there is any, it is required.

## The three files that do the real work

**`08_IMPACT_LEDGER.md`** is the spine. Every number lives here once, with an ID, and every
document cites the ID rather than re-deriving the number. The rule that makes it work: *a number
not in the ledger does not appear in a CV.* Without that rule, numbers drift between documents
and nobody notices which version is right.

**`03_CAPABILITY_MAP.md` §8 — honest absences** is the section people skip and the one that
makes everything else possible. Without a written record of what you *cannot* do, a fit
assessment can only find matches, and an assessment that never returns "weak fit" is not an
assessment.

**`13_BULLET_LIBRARY.md`** is where the second CV gets cheap. Bullets are written once, graded
once, and reused. It also carries an explicit list of bullets that must **never** be written —
kept as negative examples so a generating model can pattern-match against them.

## How it grows

1. **Session one:** the core five. Enough to generate a defensible CV.
2. **After the first CV:** add the bullet library, so the second one does not start over.
3. **Before the first fit assessment:** add the capability map, especially the absences.
4. **When it hurts:** add the rest. A file with nothing in it is worse than a missing file,
   because it looks like an answered question.

## What must never be in it

National ID or passport numbers · date of birth · marital status · other people's performance
data · passwords, tokens or keys · anything you would not want in a file an AI agent reads.

A knowledge base is a high-value target precisely because it is a complete, structured account
of one person. Treat it accordingly — see [privacy](06-privacy.md).
