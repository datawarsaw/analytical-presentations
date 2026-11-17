# Slide design, commentary and supporting detail

Load during drafting or visual review of C-suite data slides.

## Visual hierarchy for senior audiences

- **Headline first**: the title is the business insight, not "Results" or "Performance". Keep it legible and preferably to one or two lines; follow the approved template's font hierarchy.
- **Evidence second**: show the one visual focal point that supports the headline. Multiple charts are acceptable when they form one comparison, with matching units, scales and labels.
- **Implication third**: a small side annotation, callout or subhead adds business meaning, not a prose recap of the chart.
- **Scope last**: keep the mandatory footer compact but readable. Footers are not a dumping ground for conclusions or methodology.

Do not enforce academic font sizes, plain white backgrounds, or arbitrary palette limits against an approved corporate design. Be ruthless about redundant text, not about a fixed number of charts.

### Practical defaults (when no brand system exists)

- Use a consistent grid, generous margins and deliberate alignment. Maintain strong text/background contrast.
- Prefer direct labels to a distant legend. Use one accent color selectively for the focal comparison, plus muted context.
- Keep body annotations short, commonly 1-3 business-focused statements; treat ~40-50 words of body text as a **warning**, not an invariant limit. A pre-read may need somewhat more; if a slide becomes crowded, move depth into notes or appendix.
- Avoid text smaller than is comfortably readable in the actual viewing mode. For a live presentation, increase sizes substantially; for a pre-read, detailed captions may be appropriate.
- No decorative icons, gradients, shadows, photos or animation unless they have a clear explanatory purpose or are part of an approved brand system.
- Make charts native/editable if the chosen technical engine and file permit it; otherwise explain the limitation. Do not silently flatten native charts into images.

## Commentary must deepen, not duplicate

Treat "commentary" as visible explanatory text/callouts on a content slide. Native PowerPoint speaker notes are a separate surface; native review-thread comments are not the same thing.

**Bad (duplicate):** Chart already labels +12% YoY; commentary reads "Revenue increased 12% YoY."

**Better (implication):** "The improvement is concentrated in two markets, leaving broader-market resilience unproven."

**Better (recommendation):** "Validate the market-level drivers before scaling the campaign to all regions."

**Better (uncertainty):** "The baseline is not matched for store openings; treat the reported change as directional."

Do not invent concentration, driver, campaign or baseline claims: all examples above are **synthetic patterns**, not supplied facts.

Use a short internal commentary check:

1. Does this sentence merely narrate labels or restate the chart?
2. Does it add explanation, implication, uncertainty or action?
3. Can the added statement be verified, or must it be marked as a hypothesis?
4. Does the sentence support the same insight as the title?

If no defensible interpretation is available, omit the callout. Whitespace is better than padding.

## Mandatory data-slide footer

Include, as relevant to *that slide's* claim:

- **Source**: authorized source, report/table version or owner, where known.
- **Period/as-of**: exact reporting dates and data refresh cut-off.
- **Scope**: population, markets, countries, channels, product set, currency, business unit.
- **Filters**: selections, eligibility, metric mode, period alignment, active cohorts, when applicable.
- **Exclusions**: omitted entities, returns, incomplete records, exceptional markets or channels, when applicable.
- **Definition**: critical metric calculation or denominator if ambiguity affects interpretation; full definitions can live in notes/appendix.

A two-line, labeled footer is fine. Prefer `Source | Period | Scope | Filters | Excl` with appropriately compressed content. If an exclusion is not known, do not claim "None". If metadata are missing, flag the gap before finalizing; never fabricate an apparently authoritative footer.

**Illustrative format (not a client-approved example):**

`Source: Commercial reporting v3 | Period: FY26 Q3, refreshed 15 Oct | Scope: selected retail markets; net sales, local FX | Filters: comparable stores | Excl: newly opened stores`

Replace the entire example with verified details when using a real deck.

For a non-data slide (cover, section divider, summary of recommendations), use the approved template's metadata conventions; do not force a meaningless "filters" footer.

## Where depth belongs

| Surface | Appropriate content | Exclude |
| --- | --- | --- |
| Main slide | Single message, comparison/driver, short business interpretation, actionable recommendation | Deep calculation, repeated labels, entire methodology |
| Footer | Source, exact time/scope, filters, exclusions, concise definitions | Analysis, recommendations, speculative causes |
| **Speaker notes** | Detailed explanation of the slide, calculations, sources, drivers/hypotheses, presenter script, caveats | Sensitive data not allowed in the deck, unverified assertions disguised as facts |
| Appendix | Expanded cuts, sensitivity analyses, detailed data tables, supporting/alternative exhibits | Critical caveat that invalidates the main-slide claim |
| Linked source data | Full method, reproducible queries, underlying datasets (with correct access controls) | Secrets in a shared deck |

Preserve existing speaker notes during updates. Notes are part of the deliverable when supported; never assume inserting a footer is equivalent to creating notes.
