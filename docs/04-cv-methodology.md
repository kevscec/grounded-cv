# CV methodology

Format, structure and wording, with the reasoning. Every external claim is cited in
[sources](07-sources.md).

---

## 1. A CV has two readers

| | **The parser** | **The human** |
|---|---|---|
| What it is | An ATS resume-parsing engine inside Workday, Greenhouse, iCIMS, Taleo | A recruiter, scanning |
| How long it looks | Milliseconds | Around seven seconds on the first pass |
| What it sees | The PDF's text stream, flattened into fields: name, contact, employer, title, dates, degree, skills | Shape, whitespace, bold headings, numbers, the top of page one |
| What breaks it | Columns, tables, text boxes, headers and footers, images, non-standard headings | Density, no numbers, no visible hierarchy |

They are not in conflict on **format** — both want a single-column, plainly structured,
text-first document. They differ on **content density**: the parser wants keywords, the human
wants evidence. The resolution used here is that keywords live in the skills section, where
they cost nothing and are machine-legible, and evidence lives in the bullets, where it earns
the interview.

## 2. Format rules

Non-negotiable, because a parse failure is silent — nobody tells you it happened, and over 40%
of resumes reportedly contain at least one element that causes one.

1. **Single column.** No tables, text boxes or sidebars. Parsers read across the full page width
   and merge columns into nonsense.
2. **Contact details in the body**, never in a PDF page header or footer, which are frequently
   dropped from the text stream entirely.
3. **Standard section headings** — `Experience`, `Education`, `Skills`, `Projects`,
   `Certifications`. The parser matches headings against a known vocabulary to decide which
   field a block belongs to. "Where I've Made an Impact" parses as nothing.
4. **`Month YYYY` dates**, one range per role.
5. **A real, selectable text layer.** An image-based PDF extracts as empty.
6. **No icons carrying information.** A phone glyph beside a number is decoration; a glyph
   *instead of* the word is data loss.
7. **No photo.** Not a convention in most English-speaking markets, a bias-exposure liability,
   and unparseable.
8. **Submit PDF** unless the application asks for DOCX.

**Verify by extracting, not by looking.** A defect found in RenderCV's own default makes the
point: `show_top_note` renders a "last updated" stamp in the top margin which, in the extracted
text stream, appears *before the candidate's name* — the first thing an ATS reads when looking
for the name field. Invisible when you look at the PDF; obvious when you read its text layer.
`templates/cv-build/design.yaml` disables it.

## 3. Structure and length

Eye-tracking research reports around 7.4 seconds on a first pass, roughly 62% of gaze time
in the first 30% of the page, and nearly half of recruiters stopping after two sections.

**The rule that follows: page one must work as a standalone document.**

**Length.** The one-page rule is outdated for mid and senior candidates; two pages is now the
majority preference. But the second page must carry *different* material — projects,
recognition — not more bullets about the same role. Two full pages or one full page; a page and
a quarter reads as carelessness.

**Default section order**, reverse-chronological:

Header → Summary → Skills → Experience → Awards and Recognition → Selected Projects →
Education → Additional Experience → Certifications and Languages

Two judgment calls worth knowing you are making. **Skills above Experience** front-loads the
keyword payload into the gaze-dense zone and answers "is this the right kind of engineer?"
faster than any bullet — at the cost of pushing Experience down, which is why the skills block
stays to about five rows. **Selected Projects as a real section** is the structural answer to a
single-employer career: one employer with three named, distinct systems reads as range; one
employer with eight bullets reads as one job.

**Deliberately omitted:** photo · date of birth · nationality · national ID · marital status ·
"references available on request" · a soft-skills list · an objective section · salary.

## 4. Bullets

Full rules in the `cv-master-build` skill's `references/bullet-rules.md`. The essentials:

- The XYZ shape — *accomplished X as measured by Y by doing Z* — but with the verb and outcome
  leading and the method following.
- **A bullet needs either a number or a non-obvious engineering decision.** One with neither is
  a job description; cut it.
- One idea and one number per line. Lead with a verb. No first-person pronouns.
- Never strengthen a verb beyond what the attribution allows.

## 5. Researching your own target track

The framework has no opinion about your field. It has a method for forming one:

1. **Read ten current postings** for the role you want and tabulate every named requirement.
2. **Separate the screening layer from the evaluation layer.** Tool names are usually the
   screen; ownership, judgment and rigor are usually what gets evaluated in conversation.
3. **Score yourself honestly on both**, using the capability map's honest-absences section.
4. **Find where the two diverge.** That divergence is your strategy.

A worked example of step 4: a candidate whose data-engineering stack lacked several tools the
market screens on, but whose production ownership was unusually deep. The same research also
showed that hiring managers separate people who have *owned a platform in production* from
people who have only followed a tutorial — and that the tell is being able to name a pipeline
something downstream depended on. So the CV led with the named system and let tool names
follow.

**A CV cannot close a stack gap.** Keyword filters will screen you out regardless. What it can
do is win every reader who evaluates judgment — and padding the skills section with tools you
have not used trades that reader for a filter you will fail at the next stage anyway.
