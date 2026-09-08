---
name: cv-tailor
description: Produce a job-specific CV variant and application answers from an existing master CV and a completed fit assessment. Use when the user is applying to a specific posting and needs a tailored CV, when an application form asks screening questions such as years of experience with a named tool, or when it asks for a written answer or a document upload. Requires a fit assessment first; if none exists, run cv-role-fit before this skill.
---

# Tailoring for a specific posting

A variant is a **reordering and a subset** of the master, plus swaps from a reserve list. It is
never a rewrite. That constraint is what keeps six variants from drifting into six different
accounts of the same career.

**Prerequisites:** a rendered master CV and a completed fit assessment at
`workspace/applications/<company>-<role>/FIT.md`. If the fit verdict was Weak, stop.

---

## 1. What may change, and what may not

| May change | May never change |
|---|---|
| Which bullets appear, and in what order | The wording of a claim beyond what its tier allows |
| Which skills rows lead | A metric's attribution |
| The headline or functional title, where defensible | Facts, dates, titles held, certifications |
| Section emphasis and which projects are shown | Anything on the redline list |
| Summary framing | |

Copy the master YAML to `workspace/cv/<company>_<role>.yaml` and edit. Record the deltas in a
comment block at the top of the file: what changed and why. Six months later that comment is
the only thing that explains the variant.

## 2. Order the content the way the posting does

Read the posting's own responsibilities list and mirror its priorities. If it opens with
agentic AI and closes with mentoring, the bullets should run in that order. This is the single
highest-leverage tailoring move and it costs nothing.

## 3. Titles

Match the posting's title when it is defensible. Two cases where it is not:

- **The title overstates.** If the posting says "Software Engineer" and the honest ceiling is
  automation and tooling engineering, pick the nearest defensible title that still carries the
  keyword.
- **Titling down prices you down.** Applying to an analyst posting with an analyst title anchors
  the band before compensation is ever discussed. Where the person's level is genuinely above
  the posting, a title that carries the posting's keywords while signalling the real level is
  the better move — an over-qualified candidate is a recognizable and useful impression.

Say in the fit assessment which case applies and why.

## 4. Stay silent on gaps

The CV does not name a gap and does not claim the capability. Silence is the correct treatment.
Gap language belongs in a cover letter, a screening answer, or the interview — where it can be
paired with the transferability argument.

## 5. Screening questions

Application forms ask numeric and yes/no questions that are, in effect, sworn statements.

- **Answer what is written, not what you think they meant.** If a form asks about a discipline
  the person has never practised, the answer is no, even when the posting's body clearly meant
  something else. Note the discrepancy in a free-text field instead.
- **Understating something real costs a filter. Claiming something absent costs the interview
  — and casts doubt on every true claim on the same form.** These are not symmetrical, and the
  asymmetry should drive every borderline answer.
- **A years-of-experience number counts from when the person actually used the thing**, not
  from when they joined the employer.
- **Never invent a number to clear a threshold.** If the honest answer does not clear it, that
  is information about the role, not a problem to solve.
- **Where a low answer is unavoidable**, prepare the one-sentence qualifier the person can say
  before being asked.

## 6. Written answers and uploads

When a form asks for a story, pick from the knowledge base's strongest evidenced material and
answer every sub-question asked — candidates routinely answer "what did you do" and skip "how
did you communicate the problem", which is usually the differentiating half.

**If the field is a file upload rather than a text box**, the file is opened detached from the
question. Therefore:

- Head it with the person's name, contact, and the question being answered.
- Plain ASCII in a `.txt` — no typographic dashes or curly quotes, which render as mojibake in
  older editors. Hard-wrap around 78 characters and use CRLF for Windows readers.
- No character limit applies, so use the space for one concrete story rather than a summary.

## 7. Verify

Every variant goes through `cv-verify` before it is sent. Variants are where redlines slip,
because attention is on the new content.

---

**Hand off to `cv-verify`.**
