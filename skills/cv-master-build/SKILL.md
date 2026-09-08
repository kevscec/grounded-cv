---
name: cv-master-build
description: Build the master CV from a career knowledge base using RenderCV, producing a two-page master and a one-page cut plus a content map tying every line to a graded claim. Use when the user has a knowledge base and needs a general-purpose CV, when they want to rebuild or restructure their existing master CV, when they ask about CV structure, section order, length or design, or when a tailored variant is requested but no master exists yet.
---

# Building the master CV

The master is the general-purpose CV and the parent of every tailored variant. Build it once,
carefully; variants are then reorderings and subsets of it, never rewrites.

**Prerequisite:** an audited knowledge base at `workspace/knowledge-base/` with no blocking
gaps. If gaps remain, resolve them first — a CV with invented facts is worse than a late CV.

**Rendering:** RenderCV, via its own agent skill (`npx skills add rendercv/rendercv-skill`).
That skill knows the YAML schema, themes and CLI. This one decides what goes in the YAML.

---

## 1. Decide the content before writing YAML

Write `workspace/cv/CONTENT_MAP.md` first, from `templates/cv-build/CONTENT_MAP.md`. One row
per planned CV line:

| Slot | Draft line | KB ref | Tier | Attribution | Why it earns its place |
|---|---|---|---|---|---|

Every bullet traces to the knowledge base. Every number traces to a ledger ID with its
attribution intact. **A line that cannot be traced does not go in.**

This is the review checkpoint. Show it to the person before writing any YAML — it is far
cheaper to argue about a table than about a rendered document.

## 2. Structure

Reverse-chronological. Default order, adjust with reason:

Header → Summary → Skills → Experience → Awards and Recognition → Selected Projects →
Education → Additional Experience → Certifications and Languages

**Page one must work as a standalone document.** Roughly half of readers stop after two
sections, so the strongest material cannot wait for page two.

**Length:** two full pages or one full page, never a page and a quarter. Two pages is now the
majority preference for mid and senior candidates — but the second page must carry *different*
material (projects, recognition), not more bullets about the same role. Full reasoning and
sources in `docs/04-cv-methodology.md`.

Build both a two-page master and a one-page cut. **The cut is a subset defined in the content
map**, never a separate rewrite, so the two can never contradict each other.

## 3. Bullets

Check every bullet against `references/bullet-rules.md`. In short:

- Lead with a verb. No first-person pronouns. One idea and one number per line.
- A bullet needs either a number or a non-obvious engineering decision. A bullet with neither is
  a job description, and it gets cut.
- Technology in service of an outcome. Keywords live in the skills section.
- Never strengthen a verb beyond what the attribution allows.

## 4. Design

Copy `templates/cv-build/design.yaml`. It encodes decisions that matter for machine parsing:

- **`show_top_note: false`** — the RenderCV default renders a date stamp that lands *before the
  candidate's name* in the extracted text stream, where an ATS reads the name field. This is a
  real defect, verified by extracting the text rather than by looking at the PDF.
- Single column, no photo, no icons carrying information, standard section headings,
  `Month YYYY` dates, contact details in the body and never in a page header.

Theme is a human-readability decision, not a parsing one: RenderCV's own parser report found
extraction accuracy identical across its themes.

## 5. Render

Each variant renders to **its own output folder** — RenderCV derives the output filename from
`cv.name`, not from the input filename, so two variants sharing a folder overwrite each other.

```bash
rendercv render workspace/cv/master.yaml -o workspace/cv/out/master -d workspace/cv/design.yaml
```

## 6. Check the balance

Look at the rendered pages, not just the text. Watch for an orphaned heading at the foot of a
page, a single line spilling over, and dead space caused by an entry that could not be split.
Fix by cutting content or reordering sections — **not** by shrinking the font.

---

**Hand off to `cv-verify`** before the CV is sent anywhere, and to `cv-role-fit` when a specific
posting appears.
