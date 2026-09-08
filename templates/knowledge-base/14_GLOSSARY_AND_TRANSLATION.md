# 14 — Glossary and translation

**INTERNAL-ONLY.** This file exists so confidential work can be kept in the knowledge base and
still reach external documents safely.

## Internal terms

| Internal term | What it actually is |
|---|---|
| | |

## Internal to external translation

The left column must never appear in a generated document. The right column is what replaces it.

| Never write | Write instead |
|---|---|
| [product code name] | "an order-management platform" |
| [colleague name] | omit, or "a business partner" |
| [table or system identifier] | "a curated data layer" |
| [client name] | "a Fortune-500 client" |

## Pre-flight list

Every term in the left column above belongs in `workspace/redlines.yaml`, so the build fails if
one survives into a rendered PDF. Translation that depends on remembering does not hold.

## Employer description

How to refer to the employer when the name itself is fine but the specifics are not — for
example "a Fortune-50 manufacturer" rather than naming an internal division.
