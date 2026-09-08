# Quickstart

The first hour, end to end.

## 0. Install

```bash
npx skills add rendercv/rendercv-skill        # the renderer's own agent skill
npx skills add kevscec/grounded-cv            # this framework
uv tool install "rendercv[full]" --python 3.13
python -m pip install -r scripts/requirements.txt
python scripts/check_environment.py
```

Optional but strongly recommended: [Poppler](https://poppler.freedesktop.org/) for `pdftotext`.
Without it the verifier still runs, but skips the checks that read the PDF the way an ATS does —
which are the ones that catch the expensive mistakes. `check_environment.py` tells you plainly
whether that part of verification will run on your machine.

Enable the pre-commit hook, which stops personal data reaching this repository:

```bash
git config core.hooksPath .githooks
```

## 1. Create your workspace

```bash
python scripts/new_workspace.py
```

Five knowledge-base files, a CV design block, and a starter `redlines.yaml`. Everything under
`workspace/` is gitignored.

## 2. Fill in your redlines first

Open `workspace/redlines.yaml` and set your name and contact details. Add anything that must
never appear in a document — colleagues' names, internal code names, figures you have decided
not to publish.

Doing this **before** writing anything means the guard exists from the first render rather than
being added after the first near-miss.

## 3. Start the interview

Point your agent at the repo:

> *"Read AGENTS.md. I want to build my career knowledge base."*

It will load `cv-kb-build` and start asking. Bring whatever you already have — old CVs, a
LinkedIn export, performance reviews, project READMEs. Reading those first makes the interview
shorter and its questions sharper.

Expect one to three sessions. A knowledge base built across a few sittings is better than one
built in a single exhausting one, because tired people round their numbers up.

## 4. Audit before you generate

> *"Audit my knowledge base."*

Loads `cv-kb-audit`. It grades claims, finds contradictions between your sources, and tells you
plainly whether the knowledge base is safe to generate documents from. Expect some claims to be
downgraded, and expect at least one to be upgraded because nobody had asked the follow-up.

## 5. Build the master CV

> *"Build my master CV."*

Loads `cv-master-build`. It writes a content map first — every planned line traced to a graded
claim — and shows it to you **before** writing any YAML. Argue with the table; it is much
cheaper than arguing with a rendered document.

You get a two-page master and a one-page cut, both from the same source.

## 6. Then, per posting

> *"Here's a job posting: [paste or link]"*

1. `cv-role-fit` scores it and gives a verdict. Sometimes that verdict is *do not apply*, and
   that is the skill working correctly.
2. `cv-tailor` produces the variant and answers screening questions.
3. `cv-verify` runs the checks before you send anything.

```bash
python scripts/verify.py
```

## Want to see it working first?

```bash
python scripts/new_workspace.py --from-example
python scripts/verify.py
```

Seeds your workspace from `examples/sample-profile/` — a fictional profile with a complete
knowledge base, a worked fit assessment and a rendered CV — and then verifies the rendered output.
Run the whole loop against it, then replace the content with your own.
