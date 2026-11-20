# Optional client-specific presentation profile

This file defines how a **separately maintained, access-controlled client profile** may be applied to the general analytical presentation skill. It does not contain any client's brand or business rules.

## Separation of concerns

- **Analytical Presentations (this skill)**: narrative, decision quality, comparisons, exhibits, commentary, executive density, footers, notes and QA.
- **Client presentation profile**: approved look-and-feel, templates, masters, preferred slide patterns, slide order/cover requirements, footer formatting and verified client examples.
- **Business semantics**: KPI definitions, data models, SQL rules and reporting methods live in authorized project/data documentation, not in a public/general presentation skill.
- **PowerPoint engine/MCP**: reads/edits/builds the actual file, preserving editability and validating output.

## Minimum profile contract

Store in an authorized client-only location:

```text
client-presentation-profile/
  PROFILE.md
  references/
    visual-style.md
    approved-slide-patterns.md
    footer-examples.md
  templates/
    <approved-template-file-if-licensed-and-authorized>
```

`PROFILE.md` should state scope, profile version and approval status, source/template location, how to select the appropriate master/theme, presentation modes (pre-read vs live), approved language and warnings. Examples must be anonymized or appropriately permissioned.

`visual-style.md`: validated fonts, sizes, colors, margins, logos, image usage and layout rules. Never invent values from screenshots; read the authoritative master/template.

`approved-slide-patterns.md`: documented approved patterns for executive summary, recommendations, performance comparisons, commercial waterfalls, customer segmentation, key-takeaway callouts, section dividers and appendix. Link to actual approved examples and their owners.

`footer-examples.md`: authentic **formats** for source, period, scope, filters, exclusions and refresh date. Examples should show layout and label conventions, **not hard-code filters** as universal defaults.

### Template selection and preservation

- **Existing authorized deck**: its current approved master/theme takes precedence; never apply a different template during a content-only refresh.
- **New branded deck**: use the template explicitly selected by the user; otherwise resolve the best-fitting *approved* source from the private profile. Confirm the real binary, expected layouts and placeholder mapping, and its use permissions before composing slides.
- If multiple equally applicable approved templates exist, flag the choice rather than guessing. If a required branded template cannot be obtained, do not invent its logo, fonts, theme or slide master; report the missing asset or obtain an explicit unbranded exception.
- Copy the template to the target output. Preserve masters, notes, charts, and editability; never overwrite the canonical original. Applying a profile means using approved source assets where available, not painting a lookalike from a screenshot.

Do not silently copy clients' fonts, logos, templates or confidential examples into this generic skill or public repositories.

## Rule precedence

1. Current user task and applicable platform/org safety policy.
2. Canonical project instructions, access boundaries and approved client presentation template.
3. General analytical principles in `analytical-presentations`.
4. Aesthetic preferences or inspiration examples.

Narrative principles remain desirable even when a brand layout constrains their execution. If the approved template conflicts with a generic rule, preserve the template and explain a minimal exception instead of redesigning the brand.

## Profile acceptance checklist

- [ ] Specific approved template identified; no reliance on pilot/draft presentation as brand authority.
- [ ] Correct permissions for all agents who will read the profile.
- [ ] Font/colors/master details measured from approved sources.
- [ ] Real footer formats checked for source, periods, scope, filters and exclusions.
- [ ] Representative content slides approved by an authorized reviewer.
- [ ] Revision/version/owner/source date and rollback instructions documented.
- [ ] Source deck and business data remain in authorized client storage; public/general skill contains no confidential material.
