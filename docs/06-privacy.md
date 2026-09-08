# Privacy

A career knowledge base is a complete, structured account of one person: employment history,
compensation, contact details, work authorization, and often confidential material about an
employer. It deserves more care than a CV.

## What this repository guarantees

**Your data never enters this repository.**

- Everything personal lives in `workspace/`, which is gitignored.
- A pre-commit hook refuses commits that touch `workspace/`, and blocks personal email
  addresses, phone numbers and national-ID patterns anywhere in the tree.

Enable the hook — it is not automatic on clone:

```bash
git config core.hooksPath .githooks
```

The hook is deliberate design rather than belt-and-braces. A rule that depends on remembering
fails eventually; the same principle produced the redline check.

## What never belongs in a knowledge base at all

Not in `workspace/`, not anywhere:

- National ID, passport or social security numbers
- Date of birth, marital status, photograph
- Passwords, API keys, tokens
- **Other people's performance data.** Aggregates only
- Anything under an NDA that would be damaging even in a private file

Some of these are local CV conventions in some countries. They are a liability on an
international CV and a worse one in a machine-readable file.

## Confidential employer material

Confidential work is usually a person's best material, so it belongs in the knowledge base —
handled properly:

1. Mark the entry `INTERNAL-ONLY`.
2. Record the translation in `14_GLOSSARY_AND_TRANSLATION.md`: a code name becomes a generic
   description, a colleague's name disappears, a system identifier becomes a category.
3. Add every internal term to `workspace/redlines.yaml`.

Step 3 is what makes the first two reliable. `verify.py` fails the build if an internal term
survives into a rendered PDF, so translation does not depend on anyone remembering.

## Working with an AI agent

Your agent reads the knowledge base. That is the point, and it has consequences worth being
deliberate about:

- **Know where your agent runs and what it retains.** A local agent, a hosted one and one with
  memory across sessions have different profiles.
- **Never paste credentials or third-party personal data** into a session.
- **Be deliberate about compensation figures.** They belong in the knowledge base for targeting
  decisions and must never reach a generated document. The templates say so; the redline file
  can enforce it.
- **Review before sending.** The framework generates; you send. Nothing here should ever submit
  an application on your behalf.

## If you want version control for your own data

Use a **separate private repository** and point the tooling at it:

```bash
python scripts/verify.py --cv-dir /path/to/private/cv --redlines /path/to/private/redlines.yaml
```

Keep it private, and keep the same discipline about what belongs in a knowledge base at all.
