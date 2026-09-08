# Sources

Every external claim in this repository's documentation, with its source and an honest note on
how much weight it carries.

---

## Tier 1 — Primary data and first-party technical documentation

| Source | What it supports |
|---|---|
| [Agent Skills specification](https://agentskills.io/specification) · [overview](https://agentskills.io/) | The SKILL.md format, required frontmatter, folder layout, progressive disclosure, client support |
| [RenderCV documentation](https://docs.rendercv.com/) · [PyPI](https://pypi.org/project/rendercv/) | Version requirements, Typst engine, themes, YAML schema, CLI |
| [RenderCV ATS compatibility report](https://docs.rendercv.com/ats_compatibility/) | Every theme submitted to Affinda, Extracta and Klippa via Eden AI, plus Poppler and PyMuPDF extraction; ~99% extraction accuracy and identical results across themes |
| [RenderCV agent skill](https://github.com/rendercv/rendercv-skill) | The renderer's own skill, which this framework depends on rather than duplicating |
| [AGENTS.md](https://agents.md/) | The agent-instructions convention |
| [HR Dive — recruiter eye-tracking](https://www.hrdive.com/news/eye-tracking-study-shows-recruiters-look-at-resumes-for-7-seconds/541582/) | The ~7.4-second first-pass scan |

**Direct testing.** The `show_top_note` defect described in
[04-cv-methodology.md](04-cv-methodology.md) was found by rendering a CV and reading its
extracted text layer, not by reading any guide. It is the single most actionable finding in
this documentation and it came from looking at what the machine sees.

## Tier 2 — Convergent secondary reporting

Multiple independent sources agreeing. Reliable in aggregate; individual percentages should be
read as directional.

| Finding | Where |
|---|---|
| Single-column layouts only; parsers merge columns; contact out of headers and footers; standard headings; `Month YYYY` dates | [How Workday, Greenhouse and Taleo read your resume](https://www.shashiworks.com/ats-workday-greenhouse-taleo.html) · [Greenhouse ATS formatting](https://resumeats.net/blog/greenhouse-ats-resume-formatting-best-practices) · [ATS resume format guide](https://craftmyresume.ai/blog/ats-resume-format-guide-2026/) |
| Over 40% of resumes contain at least one parse-breaking element | [NeuraCV](https://neuracv.com/resources/blog/ats-resume-format-2026) |
| ~62% of gaze in the first 30% of the page; ~48% stop after two sections | [Resumly](https://www.resumly.ai/blog/optimizing-resume-sections-order-based-on-recruiter-eyetracking-research-findings) · [A4CV](https://a4cv.app/blog/six-second-resume-scan-eye-tracking-reveals-what-recruiters-see/) |
| Two pages now preferred for mid and senior candidates | [Resume Optimizer Pro](https://resumeoptimizerpro.com/blog/ideal-resume-length) · [Gainrep](https://www.gainrep.com/resources/one-page-resume-or-two/) · [Hireflow](https://hireflow.net/blog/one-page-resume-vs-two-page-resume-what-wins-now) |
| The XYZ bullet formula, attributed to Laszlo Bock, former SVP of People Operations at Google | [Teal](https://www.tealhq.com/post/xyz-resume) · [Resume.io](https://resume.io/blog/xyz-resume-format) · [Wonsulting](https://www.wonsulting.com/job-search-hub/the-power-of-quantifiable-results-how-to-use-the-xyz-formula-to-supercharge-your-resume) |

## Tier 3 — Role-specific hiring commentary

Opinion rather than data, but consistent enough to act on. All are content marketing from
resume-tool vendors, weighted accordingly and used only where several agreed.

| Finding | Where |
|---|---|
| Hiring managers distinguish real production ownership from tutorial-level work; name a system something depended on; prefer ownership verbs | [Data Engineer Academy](https://dataengineeracademy.com/blog/data-engineer-resume-guide-and-what-recruiters-actually-notice/) · [BeamJobs](https://www.beamjobs.com/resumes/data-engineer-resume-examples) |
| Missing evaluation evidence is treated as disqualifying for AI roles; do not claim prompt engineering without production proof; do not list model names as skills | [LevStack](https://levstack.io/en/blog/ai-engineer-resume-2026/) · [Resume Optimizer Pro](https://resumeoptimizerpro.com/blog/ai-engineer-examples) · [MirrorCV](https://mirrorcv.com/resume-guide/ai-ml-engineer) |

---

## An honest caveat

Most sources in Tiers 2 and 3 are published by companies selling resume software, and several
cite each other's numbers without a traceable primary study. Treat the specific percentages as
directional rather than precise.

Two findings are quoted often enough, and consistently enough, to act on regardless: **page one
carries the decision**, and **two pages is no longer penalized for mid and senior candidates**.
The rest of this framework's rules would hold even if those numbers moved, because they follow
from how parsers and readers work rather than from any particular survey.
