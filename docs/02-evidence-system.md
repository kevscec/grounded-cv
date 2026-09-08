# The evidence system

The one idea this framework exists to implement. Everything else is plumbing.

---

## The problem

Ask a capable model to write your CV and it will write a good one. It will also, without any
intent to deceive:

- promote work you **contributed to** into work you **did**,
- attach a team's numbers to you personally,
- describe familiarity as expertise,
- and invent the specifics it does not have, because a specific sentence reads better than a
  vague one.

None of this is caught at the writing stage. It is caught in a technical screen, by which point
it has cost you the role — and it damages the *true* claims standing next to it, because a
reviewer who catches one overstatement rereads everything else with suspicion.

The root cause is structural: **the model has no way to distinguish what you can defend from
what merely sounds true.** Feeding one model's confident prose into another compounds it, since
the second model has no signal that the first was extrapolating.

The fix is to make verifiability a property of the data, not a judgment made at writing time.

---

## Tiers: how verifiable is this claim?

| Tier | Meaning | How it may be used |
|---|---|---|
| **A** | Corroborated by an external record — an award, a performance review, a published document, something a third party wrote | Freely. State it plainly on a CV |
| **B** | Grounded in a real artifact you can produce and describe in depth — code, a config, a tracker, a dataset. Not visible to an outside verifier, but defensible in an interview | Freely. Prefer concrete phrasing over superlatives, and expect follow-up questions |
| **C** | Self-reported, or an AI's characterization, with no record confirming it | Only hedged: "contributed to", "supported", "approximately". Never a headline number |
| **D** | Contradicted by evidence, unverifiable, or a credential you do not hold | Never. Not on a CV, not in a cover letter, not in an interview |

**The rules:** you may weaken a claim. You may never strengthen one. An ungraded claim is a C.

**Tier B is where most good material lives**, and it is the tier people wrongly discard. Work
in a private repository is invisible to an employer and still completely legitimate to claim —
because the test is not "can they check it" but "can you defend it when asked". That is why
Tier B exists as its own grade rather than being lumped in with hearsay.

---

## Attribution: whose result is this?

Orthogonal to tiers, and it catches a different failure.

| Attribution | Meaning | Required phrasing |
|---|---|---|
| `individual` | Your own scope or deliverable | "Built…", "Reduced…", "Achieved…" |
| `shared` | One of a small number of owners | "Co-owned…", "Jointly delivered…" |
| `team` | A project result you contributed to | "Contributed to an initiative that…", "Part of the team that…" |

**A `team` number may never appear in a sentence whose subject is you, without its qualifier.**

This is the most consequential rule in the framework, because breaking it is invisible to the
person writing and obvious to anyone who was in the room. "Reduced 900 hours of manual work"
and "Contributed to an initiative that removed roughly 900 hours of manual work" contain the
same number. Only one of them survives a reference check.

Attribution is assigned **when a fact is captured**, not when a CV is written, because by
writing time the context is gone and the temptation to tighten the line is highest.

---

## What the two axes buy you

They are orthogonal, and the combination is what makes generation safe:

| | individual | shared | team |
|---|---|---|---|
| **A** | The strongest claim available. Lead with it | Strong, credited | "Part of the team that…" — still excellent |
| **B** | Most good material lives here | Common for platform work | Common for project results |
| **C** | Hedge it | Hedge it | Usually not worth using |
| **D** | Never | Never | Never |

A generating model no longer has to guess how confident to be. The grade tells it, every time,
and a downstream check can verify it obeyed.

---

## Three supporting mechanisms

**The claims register** resolves a disputed claim once, in writing, with a stable ID. Without
it the same overstatement gets rediscovered, re-argued, and eventually accepted out of fatigue.
It also holds `do-not-publish` decisions: facts that are true, verifiable, and still yours to
keep off external documents.

**The gaps file** records unknowns as unknowns. A generated document emits
`[TO CONFIRM: …]` rather than a plausible guess. A CV with three honest placeholders beats one
with three invented facts, because the invented ones surface in the interview.

**The redline check** greps the rendered PDF's text layer for things that must never appear —
colleagues' names, internal code names, unpublishable figures. It runs at build time, so the
rule is enforced by the tooling rather than by whoever is paying attention that day.

---

## The principle underneath

**Enforce, don't remember.**

Every part of this system exists because a rule that depends on human vigilance fails on the
day someone is tired, rushed, or applying to their eleventh role of the week. Grades are
recorded so they need not be recalled. Attribution is captured at source. Redlines fail a
build. The same principle is why this repository's own privacy rule is a pre-commit hook rather
than a paragraph in a README.
