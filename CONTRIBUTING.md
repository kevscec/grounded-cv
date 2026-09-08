# Contributing

Thanks for looking. This project has an unusually specific point of view, so the most useful
thing to know before opening a PR is what it is trying to be.

## The point of view

**Verifiability is a property of the data, not a judgment made at writing time.** Every feature
should make it easier to record how defensible a claim is, or harder to accidentally overstate
one. Features that make a CV *sound* better without making it *truer* are out of scope, however
well they would demo.

A corollary: **enforce, don't remember.** If a rule matters, it belongs in a check that fails a
build, not in a paragraph asking people to be careful.

## What is especially welcome

- **Knowledge-base template improvements**, particularly for career shapes this does not serve
  well yet — academia, contracting, career changes, long gaps, non-technical roles.
- **New checks in `scripts/verify.py`**, with a negative control proving the check fires.
- **Fixes to the ATS and formatting research** in `docs/04-cv-methodology.md`, with a source.
  Corrections are more valuable than additions here; several widely-repeated figures in this
  space trace back to nothing.
- **Translations** of the documentation.
- **Reports of things that broke** in a real job search. Those are the most useful issues.

## What is out of scope

- Rendering backends other than RenderCV. The seam exists; the maintenance cost of a second one
  does not pay for itself yet.
- Anything that submits an application automatically. The framework generates; a person sends.
- Features whose value depends on the user not checking the output.

## Ground rules for changes

1. **No personal data, ever.** Not in examples, not in tests, not in a fixture. The sample
   profile is fictional and uses `example.com` addresses. The pre-commit hook enforces this:

   ```bash
   git config core.hooksPath .githooks
   ```

2. **A new check needs a negative control.** Add it to `scripts/test_verify.py`, which plants a
   violation for every check and asserts it is caught. A check that never fires is worse than no
   check, because it produces false confidence.

   ```bash
   python scripts/test_verify.py
   ```

3. **Skills must pass the spec validator:**

   ```bash
   python scripts/validate_skills.py
   ```

4. **The example must still verify:**

   ```bash
   python scripts/verify.py --cv-dir examples/sample-profile/cv \
                            --redlines examples/sample-profile/redlines.yaml
   ```

5. **Skill descriptions are load-bearing.** They are the only text an agent sees before deciding
   whether to load a skill, so they must say both *what* the skill does and *when* to use it,
   and must not overlap with a neighbouring skill.

## Documentation style

Write for someone who is competent and busy. State the reason a rule exists, not only the rule.
Where a claim comes from outside, cite it in `docs/07-sources.md` and be honest about how much
weight it carries — a good deal of published advice in this field is content marketing, and
saying so is more useful than repeating it.

## Conduct

Be decent and assume good faith. Disagreement about the design is welcome; disrespect is not.
