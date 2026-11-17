# PowerPoint MCP and technical implementation workflow

Load when an agent needs to create, edit, or review an actual PowerPoint deck. This reference is a workflow bridge, **not** an alternate PPTX creation engine.

## Before modification

1. Identify the exact, user-authorized presentation file and the requested slide range/scope. Confirm whether it is an official/shared/canonical source.
2. Prefer a separate copy or save-as output for substantive edits, unless the user explicitly directs in-place editing.
3. Use the technical PowerPoint skill or local MCP's instructions for the *current* implementation. Check what the active connection actually supports instead of assuming all listed operations are available.
4. If using the connected `Breitling_PowerPoint` MCP, **activate the correct presentation first** with `ppt_activate_presentation` before any inspection or edit. Do not assume the currently open Windows PowerPoint window is the intended target.
5. Read the deck layout, masters, theme, current slide order, existing chart data, text and notes before making stylistic changes. Preserve approved brand features.
6. Prepare a storyboard/diff plan: original title -> proposed action title -> evidence -> commentary -> mandatory scope footer -> notes/appendix.

## Editing through live PowerPoint MCP

Use equivalent supported operations, when available, in a narrow loop:

- **Inspect**: `ppt_get_presentation_info`, `ppt_list_slides`, `ppt_get_slide_info`, `ppt_list_shapes`, `ppt_get_chart_data`, `ppt_get_table_data`, `ppt_get_slide_notes`, `ppt_get_theme_colors`, `ppt_list_layouts`.
- **Edit**: `ppt_set_text` or `ppt_format_text`, chart/table data setters, native shape manipulation, layout-preserving duplication, `ppt_set_slide_notes` for speaker notes.
- **Review**: `ppt_get_slide_preview` and/or `ppt_export_images`, text and chart data re-read, visual inspection of every modified slide.
- **Save**: only after satisfactory QA, respecting the authorized destination and existing change/version-control rules. Prefer `ppt_save_presentation_as` for a safe copy when possible.

Tool names are examples from one known MCP provider; do not call nonexistent tools or claim a certain state without observing it. Other harnesses may use a local PPTX library or different MCP methods.

## Alternative PPTX engines

When PowerPoint MCP is unavailable or a brand-new deck is requested:

- Use the environment's PPTX skill, e.g. its supported PptxGenJS workflow. Follow its own requirements for layout, native charts, file integrity, rendering and output path.
- For existing decks, preserve OOXML structure, slide masters, charts and notes using the technical skill's safe editing workflow. Do not degrade rich native elements into flat screenshots without consent.
- A text extractor such as MarkItDown helps audit text/content but **cannot** replace native slide rendering/visual inspection. The user-facing output must be the requested editable file when requested.

## Incremental slide loop

1. Establish slide's current intended purpose.
2. Confirm correct metrics, baseline, data provenance and footer scope.
3. Write the action title and evidence mapping.
4. Decide whether to modify a chart, commentary, annotations, or just visual hierarchy.
5. Edit only the authorized elements; avoid destructive global theme changes without approval.
6. Add/verify notes for deeper interpretation and remaining limitations.
7. Render/preview the slide, inspect text overflow, label placement, chart consistency, source and footer legibility.
8. Re-read the edited values and notes; correct until the claim matches evidence.

## Safe completion and provenance

- Re-evaluate the Executive Summary after all detail slides change; identify any stale summary statement.
- Preserve slide-specific source/scope/filter/exclusion metadata and report information gaps.
- Track which original slides changed and what was intentionally left untouched. Make a concise handoff with QA status and file location.
- Do not send confidential contents to external AI, image or chart services. Do not overwrite client originals or SharePoint files without authorization.
- Treat read-only requests as read-only regardless of MCP runtime permission mode.
