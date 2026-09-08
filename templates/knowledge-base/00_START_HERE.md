# 00 — START HERE: operating contract for the consuming AI

You are reading a knowledge base about one person. Your job is probably to write a CV, a cover
letter, a profile, an interview brief or a role-fit assessment. This file tells you how to use
the rest of it without misrepresenting them.

Read this file completely before writing anything.

---

## 1. What this is and is not

- It **is** a graded record of one person's career, where every claim carries a mark of how
  verifiable it is.
- It **is not** uniformly reliable, and it is not a CV. Some of it is well-evidenced; some is
  recalled. The grading is what tells you which is which.
- It is **role-agnostic**. Do not assume a target role. Run the fit procedure against the
  posting you actually have.

## 2. The tier system

**Never present a claim as stronger than its tier allows. Never upgrade a tier.**

| Tier | Meaning | How you may use it |
|---|---|---|
| **A** | Corroborated by an external record — award, review, published document | Freely. State it plainly |
| **B** | Grounded in a real artifact this person can produce and describe in detail | Freely, but prefer concrete phrasing over superlatives. Expect follow-up questions |
| **C** | Self-reported, or an AI's characterization, with no record confirming it | Only hedged: "contributed to", "supported", "approximately". Never a headline number |
| **D** | Contradicted, unverifiable, or a credential not held | Never. Not in a CV, not in a cover letter, not in an interview answer |

If a claim is not graded anywhere, treat it as **C**.

## 3. The attribution rule

| Attribution | Meaning | Required phrasing |
|---|---|---|
| `individual` | This person's own scope or deliverable | "Built…", "Reduced…", "Achieved…" |
| `shared` | One of a small number of owners | "Co-owned…", "Jointly delivered…" |
| `team` | A project result they contributed to | "Contributed to an initiative that…", "Part of the team that…" |

**Hard rule:** a `team` number may never appear in a sentence whose subject is this person
without its qualifier. Dropping the qualifier to tighten a line is the most damaging edit you
can make to this document, because it is invisible to you and obvious to a former colleague.

## 4. Read order by task

| Writing… | Read, in order |
|---|---|
| A CV for a specific job | `12_ROLE_FIT_GUIDE` → `03_CAPABILITY_MAP` → `08_IMPACT_LEDGER` → `13_BULLET_LIBRARY` → `02_POSITIONING` |
| A general CV or profile | `02_POSITIONING` → `03` → `05_PROJECTS` → `08` → `13` |
| A role-fit assessment | `03_CAPABILITY_MAP` → `12_ROLE_FIT_GUIDE` → `11_GAPS` |
| An interview brief | `05_PROJECTS` → `07_WAYS_OF_WORKING` → `09_RECOGNITION` |
| Anything at all | This file, plus `10_CLAIMS_REGISTER` if a claim looks too good |

## 5. Redlines

Edit this list to match this person's situation. Every entry should also appear in
`workspace/redlines.yaml` so the build enforces it.

1. **Never invent identity facts.** Education, dates, employers, contact details and
   certifications are recorded in `01_IDENTITY_AND_FACTS`. If something is missing it is in
   `11_GAPS`. Leave `[TO CONFIRM: …]` and say so. Do not guess a graduation year.
2. **Never claim a certification** not listed in `01`. Practical use of a technology is not a
   certification.
3. **Never claim a title this person does not hold.** Describing the work is fine; awarding the
   title is not.
4. **Never put a colleague's name, an internal code name, a table name or a system identifier
   on an external document.** Translate via `14_GLOSSARY_AND_TRANSLATION`.
5. **Never attribute team results to this person individually.** See section 3.
6. **Never describe exposure as hands-on experience.**
7. **Never reproduce third parties' performance data.**
8. *(add this person's own)*

## 6. When you hit a gap

Do not fill it. In order of preference: check `11_GAPS`, which may already log it; ask the
person one short question; or emit `[TO CONFIRM: …]` inline and list every placeholder at the
end of your output.

A CV with three honest placeholders is worth more than one with three invented facts, because
the invented ones are discovered in the interview.

## 7. Tone

- **Concrete over superlative.** A specific number and mechanism beats any adjective.
- **Outcome-attached.** Technology in service of a result, never a keyword list.
- **One number per bullet.**
- **No first-person pronouns in CV bullets.** Lead with a verb.

## 8. Sanity check before you ship

- [ ] Every number I used appears in `08_IMPACT_LEDGER` with matching attribution
- [ ] No Tier C claim stated without hedging
- [ ] No Tier D item appears anywhere
- [ ] No internal name, code name or colleague name survived
- [ ] Every unknown is a visible placeholder, not a guess
- [ ] The role framing came from the fit assessment, not from my own assumption
