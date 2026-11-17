# Analytical Presentations (v0.1)

A client-agnostic agent skill for **decision-ready analytical PowerPoint presentations**, particularly executive, board, C-suite, performance and KPI decks. It does not create PPTX files on its own. It coordinates with PowerPoint MCP and the available technical PPTX generation/editing skills.

## Why this exists

The target outcome is an actionable business recommendation supported by evidence, not a slide deck that merely displays data.

It enforces:

- Executive Summary as the first content slide, after an optional cover.
- Action titles and a coherent ghost-deck narrative.
- One primary insight per slide, supported by one or more exhibits.
- Comparison against meaningful context where available (LY, plan, benchmark, etc.).
- Comments that deepen the chart rather than repeat its values.
- Honest statements of uncertainty, hypotheses and data limitations.
- Concise business-facing text and deeper detail in notes/appendix.
- Source, period, scope, filters and exclusions in each analytical data-slide footer.
- Visual, evidence and narrative QA, preserving the client's approved presentation style.

## Example instructions to an agent

- "Review this deck through PowerPoint MCP for executive readiness. Keep the approved template, rewrite weak titles, fix commentary that restates charts and flag missing baselines/filters."
- "Create a C-suite presentation from these approved charts. Lead with an Executive Summary and three defensible recommendations. Make every analytical slide's scope explicit."
- "Audit the narrative of this PowerPoint: run a ghost-deck test, check each recommendation against the exhibits, and identify the top three fixes before editing."

## Structure

- `SKILL.md` - the entrypoint and 12 operating principles.
- `references/story-architecture.md` - Executive Summary, storyboards and ghost deck.
- `references/comparisons-and-evidence.md` - valid baselines, chart/evidence correctness.
- `references/slide-design-and-commentary.md` - executive visual rules; slide text vs notes/footer/appendix.
- `references/powerpoint-workflow.md` - safe live PowerPoint MCP or file-based editing.
- `references/quality-gates.md` - narrative/data/visual/file QA gates.
- `references/client-profile-contract.md` - design for separate private client profiles.
- `references/inspiration-and-attribution.md` - public sources and attribution links.
- `agents/openai.yaml` - skill UI metadata.

## Not included in v0.1

- No brand colors/fonts/assets, client data or proprietary KPI definitions.
- No PowerPoint plugin, scripts, fonts or external APIs. Reuse existing tools.
- No validated client presentation profile yet; a future Breitling-specific profile must come from approved client templates and live deck examples.
- Installing or enabling this skill is a separate per-harness operation; Git storage alone does not activate it.
