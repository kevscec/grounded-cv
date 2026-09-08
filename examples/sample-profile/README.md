# Sample profile — Robin Doe

> ### This profile is entirely fictional.
>
> Robin Doe does not exist. Northwind Retail Group and Contoso Logistics are the industry's
> standard placeholder company names. Every metric here is invented to illustrate the format,
> and none of it should be copied into a real knowledge base.

It exists to answer the question a blank template cannot: **what does a good entry actually
look like?**

## The output

![The rendered sample CV](cv/robin-doe-cv-preview.png)

Rendered from `cv/master.yaml` by RenderCV, using the shared design block. Every line traces
back to a graded claim in `knowledge-base/`.

## What is here

```
knowledge-base/    a 9-file knowledge base at the "recommended" tier
applications/      a fictional job posting and the fit assessment produced from it
cv/                the master CV YAML, the design block, and the rendered result
redlines.yaml      what must never appear in a generated document
```

## Run it

```bash
python scripts/new_workspace.py --from-example
python scripts/verify.py
```

That seeds your workspace with this profile and runs the full verification. Then replace the
content with your own — the structure stays, the facts do not.

## What to look at first

**`knowledge-base/08_IMPACT_LEDGER.md`** — how a metric is recorded. Note `M-05`, a team result.
It is a real achievement and it is tagged `TEAM`, so every document that uses it must say
"contributed to". Then look at bullet `B-07` to see the same number written correctly, and the
"never write" table at the bottom of the bullet library to see it written *incorrectly*, kept
deliberately as a negative example.

**`knowledge-base/03_CAPABILITY_MAP.md` §8** — the honest absences. This is the section people
skip and the reason the fit assessment can reach a verdict of anything other than "yes".

**`applications/northstar-data-engineer/FIT.md`** — a worked assessment that recommends applying
*with a named gap addressed up front*, rather than pretending the gap is not there.

**`knowledge-base/10_CLAIMS_REGISTER.md`** — `CR-01` shows a claim being downgraded, and `CR-02`
shows one being upgraded, which is the outcome people do not expect from an audit.
