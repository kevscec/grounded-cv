# The workflow

Two loops. A slow one you run once, and a fast one you run per posting.

```
    ┌─────────────── the slow loop, run once ───────────────┐
    │                                                       │
    │   cv-kb-build  ──►  cv-kb-audit  ──►  cv-master-build │
    │   interview          grade &          content map,    │
    │   & intake           reconcile        render, verify  │
    │                                                       │
    └───────────────────────────┬───────────────────────────┘
                                │
    ┌───────────────────────────▼─── per posting ───────────┐
    │                                                       │
    │   cv-role-fit  ──►  cv-tailor  ──►  cv-verify         │
    │   verdict            variant &       redlines &       │
    │   (may be STOP)      answers         ATS checks       │
    │                                                       │
    └───────────────────────────────────────────────────────┘
```

## The slow loop

**Phase 1 — `cv-kb-build`.** Read what already exists, then interview in passes. Grade each
claim as it arrives; retrofitting grades later does not work. Expect one to three sessions.

**Phase 2 — `cv-kb-audit`.** Grade challenge, contradiction resolution, absence sweep. Ends
with a plain statement of whether the knowledge base is safe to generate from. Re-run whenever
material is added.

**Phase 3 — `cv-master-build`.** Content map first, reviewed before any YAML is written. Then a
two-page master and a one-page cut from one source.

## The fast loop

**Phase 4 — `cv-role-fit`.** Decompose the posting, score each requirement, produce a verdict —
Strong, Good, Stretch or Weak — plus level, compensation and location checks.

**This phase can end the loop.** "Weak fit, do not apply" is a successful outcome. An assessment
that never returns it is not an assessment, it is a formality.

**Phase 5 — `cv-tailor`.** A variant is a reordering and a subset, plus swaps from a reserve
list. Never a rewrite. Also handles screening questions and written answers.

**Phase 6 — `cv-verify`.** `python scripts/verify.py`, then the manual pass, then read it aloud.

## Where the loops touch

The fast loop feeds the slow one. Every posting teaches you something about your own profile:

- A requirement you keep scoring **Partial** is a gap worth closing in reality, not in wording.
- A capability postings keep asking for that is not in the capability map belongs there.
- A bullet that worked well belongs in the bullet library.
- A screening question you answered awkwardly usually means the knowledge base was ambiguous.

After a few applications, run `cv-kb-audit` again with what you learned.

## Rules that hold across every phase

1. **Never upgrade a tier. Never drop an attribution qualifier.**
2. **Surface gaps, never fill them.**
3. **Verify before sending. Every time, including the variant that changed one line.**
4. **A weak fit is an output, not a failure.**

## Roughly how long

| Phase | First time | Afterwards |
|---|---|---|
| Knowledge base | 2–4 hours across sessions | minutes to add material |
| Audit | 30–60 minutes | 10 minutes |
| Master CV | 1–2 hours | rebuild in 20 minutes |
| Fit assessment | 20 minutes | 10 minutes |
| Tailored variant | 30 minutes | 15 minutes |
| Verify | 2 minutes | 2 minutes |

The slow loop is the investment. Everything after it is cheap, which is the entire point: the
cost of applying well drops far enough that applying badly stops being tempting.
