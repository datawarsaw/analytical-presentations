# Source-locked refresh and reconciliation

Load for a request to refresh an existing deck, replace an old reporting period, update KPI values or charts, or regenerate a recurring executive review. This is a **data-integrity contract**, not a data connector or scheduler. Apply the existing comparisons, visual QA, and PowerPoint editing references as well.

## 1. Establish the source lock before editing

For every affected data slide, identify or obtain:

- **Authorized source**: exact user-approved dataset/report/workbook/query/table or linked chart; source identity/version and access identity when relevant. Do not guess an alternative, silently reuse last session's source, or broaden access.
- **Metric contract**: approved measure names, definitions, numerator/denominator, aggregation/grain, currency/unit and any conversion rules. Existing semantic-model measures remain authoritative.
- **Time and comparison**: requested period, time zone/fiscal calendar, comparison baseline and as-of/refresh timestamp (distinguish stale source data from current execution time).
- **Scope**: population, region/channel, segments, filters, exclusions, relevant return or eligibility logic, and owner/approval when required.
- **Destination**: exact deck copy, slide range, output location and whether the user authorized data replacement, narrative rewriting, or both.

Capture these as a brief **source-lock record** (per-slide differences allowed). If the source or metric contract is unknown and material, mark the affected KPI `UNVERIFIED` and stop its data refresh; do not substitute a convenient dataset. Metadata can be stored in notes, an accompanying review table, or the approved handoff according to the deliverable.

## 2. Read, recalculate, reconcile

1. Fetch or read the *actual authorized values* with supported access. A browser screenshot of a report is not proof of measure-level query access.
2. Confirm source refresh date and reporting-period completeness. Do not label stale or partial data as current.
3. Reconcile every edited numerical slide element against the source: chart series/data table, text KPI, percentages, absolute and percentage-point deltas, footnotes, annotations and notes.
4. Preserve exact values internally; apply presentation rounding only at display time. Verify numerator/denominator, cohort/filter parity, units, FX conversion, and that displayed totals/deltas are not misleading after rounding.
5. Treat missing, withheld and invalid values as **unavailable**, not zero. For a zero or missing comparison denominator, do not fabricate a percentage growth value; report an absolute change where valid.
6. Separate observed variance from driver attribution or causal explanation. Label new explanations as hypotheses unless the source supports them.

Use the existing `comparisons-and-evidence.md` for detailed metric and chart rules rather than re-creating them here.

## 3. Update the deck as a consistent unit

- Modify only the authorized slide elements on a safe deck copy (unless in-place editing was explicitly authorized). Retain approved master/layout, chart editability, notes and manual commentary where compatible.
- Refresh charts and tables **before** rewriting data labels, action titles, implications and recommendations. Replace or qualify stale commentary; do not leave prior-period "latest" claims unchanged.
- Refresh **Source | Period/as-of | Scope | Filters | Exclusions** footers for every affected analytical slide using verified values. Maintain detailed definitions and source reasoning in speaker notes/appendix.
- Revalidate cross-slide consistency, recurring visuals and summary calculations. Re-write the Executive Summary to match the new evidence, rather than copying the previous recommendations unchanged.
- If some slides cannot be verified, report exactly which ones and why. A partial update must not be presented as a fully refreshed deck.

## 4. Stop conditions and change report

**Block affected claims or delivery until reconciled** when the source is inaccessible/unauthorized; source identity differs; critical metric definitions or permissions are unknown; comparison cohorts are incompatible; a material value does not reconcile; or source freshness invalidates a "current" claim. Do not overwrite earlier validated values with guessed replacements.

For the output, provide a compact trace: `Slide | Source/version | As-of/period | Metric or change | Verified/Unverified | Notes`. Report file target, slides changed, failed reconciliations, remaining caveats, and whether the final deck was actually rendered and inspected. Escalate any material outstanding discrepancy for human approval; do not auto-publish or distribute a confidential deck.

**Miniature synthetic example:** A source provides sales 120 for the new period and 100 for the approved like-for-like baseline. A +20% label is valid if currency, filters and denominators match. If the baseline is absent, mark `% change` unavailable, even when 120 is available.
