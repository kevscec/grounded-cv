---
name: cv-verify
description: Verify a rendered CV against redlines, attribution rules, ATS text-layer parsing and page limits before it is sent. Use before submitting any application, when the user asks whether a CV is safe to send or ready to submit, after generating or editing any CV variant, or when the user wants to check that confidential names, internal code names or unpublishable figures have not survived into a rendered document.
---

# Verifying a CV before it is sent

Redlines stop being something to remember and become something the build enforces.

```bash
python scripts/verify.py
```

It renders every CV YAML in the workspace, extracts each PDF's text layer the way an ATS parser
would, and exits non-zero on any failure.

---

## What the script checks

| Check | Why |
|---|---|
| **Redlines** from `workspace/redlines.yaml` | Colleague names, internal code names, unpublishable figures, forbidden titles — anything the person has decided must never appear externally |
| **National ID patterns** | A local CV convention in some countries and a liability on an international one |
| **Attribution qualifiers** | Every configured team metric must sit in a sentence containing "contributed to", "part of the team", "co-owned" or "jointly delivered" |
| **Name is the first line of the text stream** | Catches a header or date stamp rendering ahead of the name, where an ATS reads the name field. This is not hypothetical — it is RenderCV's default |
| **Contact fields survive extraction** | Email, phone and links must be recoverable as text, not lost in a header or drawn as an icon |
| **Page count** | Master within limit, one-page cut exactly one |
| **Standard headings present** | `Experience`, `Education`, `Skills` must appear at line start |
| **Stale output** | A render that failed is tolerated only if the existing PDF is newer than its source. Otherwise the PDF is stale and must not be sent |

Without `pdftotext` installed the text-layer checks are skipped with a warning. Install Poppler
to get them; they are the ones that catch the expensive mistakes.

## Redlines are personal data

`workspace/redlines.yaml` is the user's, generated from
`templates/config/redlines.example.yaml`. It typically holds:

- Names of colleagues, managers and clients
- Internal product and project code names
- Table names, workspace identifiers, hostnames
- Figures the person has decided not to publish
- Titles they do not hold
- Credentials they do not have

Add to it whenever a new one is discovered. **The list only works if it is maintained**, and the
moment to add an entry is the moment it is noticed.

## A green run is necessary, not sufficient

The script catches what a machine can catch. Then walk the manual pass:

- [ ] Every number traces to a ledger entry with matching attribution
- [ ] No Tier C claim stated without hedging; no Tier D item anywhere
- [ ] Every bullet traces to the knowledge base, and no verb was strengthened
- [ ] No team result converted to individual by dropping its qualifier
- [ ] Certifications are exactly those held, with their real scope
- [ ] Dates are current — expected graduation, job end dates, headcounts
- [ ] Every bullet leads with a verb; no verb repeats within a section
- [ ] Nothing from the banned-construction list
- [ ] Links are live and correct
- [ ] The PDF opens, text is selectable, no orphaned headings, no quarter-page spill

## Then read it out loud

The test that catches what checklists do not. Read the summary and the first three bullets
aloud, and ask:

- Would a colleague who was in the room recognize this as accurate?
- Is there a line here you would not want to defend in an interview?
- Does it sound like a person, or like a résumé generator?

If any answer is wrong, fix it before sending. Every failure this catches is one that would
otherwise have been caught by an interviewer.

---

If checks fail, hand back to `cv-tailor` or `cv-master-build` to fix the source, then re-run.
Never edit a rendered PDF.
