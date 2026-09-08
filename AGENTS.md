# AGENTS.md — operating instructions for AI agents

You are working with **grounded-cv**, a framework for building a career knowledge base and
generating CVs from it where every claim is graded by how verifiable it is.

Read this file completely before acting. It tells you where the user is in the workflow and
which skill to load.

---

## 1. The one rule that outranks everything

**Never make a claim stronger than its evidence allows.**

Every claim in a knowledge base carries a **tier** (how verifiable) and every metric carries an
**attribution** (whose result it is). You may weaken a claim. You may never strengthen one.

| Tier | Meaning | Use |
|---|---|---|
| **A** | Corroborated by an external record — award, review, published document | Freely, plainly |
| **B** | Grounded in a real artifact the person can produce and defend in detail | Freely; prefer concrete phrasing |
| **C** | Self-reported or an AI's characterization; no record confirms it | Only hedged, never as a headline number |
| **D** | Contradicted, unverifiable, or a credential not held | Never. Not anywhere |

| Attribution | Required phrasing |
|---|---|
| `individual` | "Built…", "Reduced…", "Achieved…" |
| `shared` | "Co-owned…", "Jointly delivered…" |
| `team` | "Contributed to an initiative that…", "Part of the team that…" |

**Hard rule:** a `team` number may never appear in a sentence whose subject is the person,
without its qualifier. Dropping the qualifier to tighten a line is the single most common and
most damaging failure in AI-written CVs.

**When you hit a gap, surface it — never fill it.** Emit `[TO CONFIRM: what you need]` inline
and list every placeholder at the end of your output. A CV with three honest placeholders beats
one with three invented facts, because the invented ones surface in the interview.

---

## 2. Where does the user's work live

- **`workspace/`** — the user's knowledge base, CVs and applications. Gitignored. Create it
  with `python scripts/new_workspace.py` if it does not exist.
- **This repo** — the method: skills, templates, docs, tooling. Never write personal data here.

If the user asks you to commit their knowledge base to this repo, stop and point them at
`docs/06-privacy.md`.

---

## 3. Pick a skill

Load the skill that matches; do not improvise the procedure.

| The user wants to… | Load |
|---|---|
| Start from nothing, or add a role / project / achievement | `cv-kb-build` |
| Reconcile sources that disagree, grade new claims, or prepare a KB for use | `cv-kb-audit` |
| Know whether a job posting is worth applying to | `cv-role-fit` |
| Produce a general-purpose CV | `cv-master-build` |
| Apply to a specific posting, or answer screening questions | `cv-tailor` |
| Check a CV before sending it | `cv-verify` |

**If nothing exists yet**, the order is: `cv-kb-build` → `cv-kb-audit` → `cv-master-build`.
Then, per posting: `cv-role-fit` → `cv-tailor` → `cv-verify`.

Each skill hands off to the next at the end of its instructions, so you can run the whole loop
without the user naming skills.

---

## 4. Orientation before you act

Check, in this order:

1. Does `workspace/knowledge-base/` exist and contain `00_START_HERE.md`?
   **No** → the user is at the beginning. Load `cv-kb-build`.
2. Does `workspace/knowledge-base/11_GAPS.md` list blocking gaps?
   **Yes** → resolve those before generating any document.
3. Does `workspace/cv/` contain a rendered master CV?
   **No** → load `cv-master-build` before tailoring anything.
4. Did the user paste a job posting? → load `cv-role-fit` first, *before* writing any CV.

**Do not skip the fit assessment.** Producing a tailored CV for a role that does not fit wastes
the user's time and yours. "Weak fit, do not apply" is a valid and valuable output.

---

## 5. Rendering

CVs are rendered with **RenderCV**. Install its official skill —
`npx skills add rendercv/rendercv-skill` — which carries the YAML schema, themes and CLI. This
framework does not duplicate that knowledge; it decides *what goes in the YAML*, not how the
YAML works.

Two invariants this framework adds on top:

- `design.page.show_top_note: false` — the default renders a date stamp that lands **before the
  candidate's name** in the extracted text stream, where an ATS reads the name field.
- **Each CV variant renders to its own output folder.** RenderCV names output from `cv.name`,
  not from the input filename, so two variants sharing a folder overwrite each other.

---

## 6. Before anything is sent

Run `python scripts/verify.py`. It renders, extracts the PDF text layer the way an ATS parser
would, and fails on redline hits, team metrics missing their qualifier, a name that is not the
first line, missing contact fields, or a page-count violation.

A green run is necessary, not sufficient. The manual checklist in `cv-verify` still applies.

---

## 7. Tone when writing CV content

- Concrete over superlative. "Mined 4,703 production errors into a 92-pattern taxonomy" beats
  "world-class observability expertise".
- One idea and one number per bullet.
- Lead with a verb. No first-person pronouns in CV bullets.
- Technology in service of an outcome, never a keyword list. Keywords live in the skills
  section, where they cost nothing.
