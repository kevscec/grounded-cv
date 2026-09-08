---
name: cv-role-fit
description: Score a job posting against a career knowledge base and produce an honest fit verdict, including recommending against applying when the role does not fit. Use whenever the user shares a job description, a posting link, or a role summary and wants to know whether to apply, how well they match, what to lead with, or where they are weak. Also use when the user asks to tailor a CV to a specific job, because the fit assessment always runs before any tailored document is written.
---

# Assessing fit against a job posting

This runs **before** any CV is written. Producing a tailored CV for a role that does not fit
wastes an afternoon and teaches nothing. A verdict of "weak fit, do not apply" is a successful
outcome of this skill.

Knowledge base at `workspace/knowledge-base/`. Write the assessment to
`workspace/applications/<company>-<role>/FIT.md`.

---

## Step 1 — Decompose the posting

Extract separately. Ignore the marketing paragraphs; work from the responsibilities and
requirements lists.

- **Required capabilities** — what the person must be able to do
- **Required technologies** — named tools
- **Domain expectations** — industry, data, business context
- **Seniority signals** — ownership, mentoring, architecture, on-call, band, title
- **Hard filters** — degree, certification, location, work authorization, years of experience
- **Compensation**, if stated, and whether it is a real band or an unsourced number

## Step 2 — Score each requirement

| Score | Meaning |
|---|---|
| **Deep** | Evidenced repeatedly, defensible for an hour. Lead with it |
| **Strong** | Evidenced. Support it with a specific artifact |
| **Partial** | An adjacent capability exists, not the exact one. Argue transferability explicitly |
| **Absent** | Not in the knowledge base, or listed under honest absences. Do not manufacture it |

Pull the evidence as you score: the project, the metric ID, the pre-written bullet. Prefer the
higher tier where both would work.

## Step 3 — Verdict

| Verdict | Criteria | Action |
|---|---|---|
| **Strong fit** | Every must-have Deep or Strong; at most one Partial | Apply. Lead with the two the posting names first |
| **Good fit** | Most must-haves Deep or Strong; one or two genuinely adjacent Partials | Apply. Address the Partials head-on rather than hoping they go unnoticed |
| **Stretch** | One must-have Absent but learnable, rest strong | Apply only if the rest is unusually strong. Name the gap and the nearest experience |
| **Weak fit** | A must-have is structurally absent, or a hard filter applies | Say so. Recommending against an application is a valid, useful output |

**Count the structural absences.** A role sitting on top of two or more capabilities the
knowledge base lists as structurally absent is a weak fit however appealing it looks, and no
wording fixes that.

## Step 4 — Look past capability

Capability fit is necessary and not sufficient. Check and report:

- **Level.** Is the title a step down? A junior band with senior responsibilities is a
  downgrade that is easier to accept than to undo later.
- **Compensation.** Against the person's current and target figures. An unstated band is a
  question to ask, not an assumption to make. A band far above the requirement bar deserves
  scepticism — say so rather than getting attached to it.
- **Work authorization and location.** Regional postings often exclude specific countries;
  "remote" sometimes still means local employment.
- **Volume and competition.** Applicant count and posting age change what effort is worth
  spending.
- **Warm connections.** A referral outranks any wording change on a high-volume posting.

## Step 5 — Write it

```
VERDICT: <Strong fit | Good fit | Stretch | Weak fit>

WHY IT FITS
- <capability the posting names> — Deep. <evidence + metric ID>

WHERE IT'S THIN
- <capability> — Partial. Nearest experience: <x>. The delta is <y>.
- <capability> — Absent. <structurally absent | learnable>

BLOCKERS AND ECONOMICS
- <hard filters, level, compensation, location>

HOW TO POSITION IT
Title: <...>   Lead with: <the two strongest role-specific stories>
Address up front: <the gap most likely to disqualify>

RECOMMENDATION
<apply / apply opportunistically / do not apply>, and why.
```

Keep it short. A fit assessment that takes a page to say "weak fit" is not helping.

## Arguing a Partial

Never *"familiar with"* — it reads as a bluff. The shape is always:

> *"Has done [the underlying engineering problem] at [scale]; [the specific tool] would be new."*

See `references/transferability.md` for worked patterns.

**Gap language belongs in a cover letter or an interview, never printed on the CV.** The CV
does not name gaps; it simply does not claim the thing.

---

**Hand off to `cv-tailor`** when the verdict is Strong, Good, or a Stretch worth taking. When
the verdict is Weak, say so and stop — do not produce a CV anyway.
