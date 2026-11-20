#!/usr/bin/env python3
"""Small static integrity tests for the Analytical Presentations skill.

No PowerPoint automation, data source, model or remote access is exercised here.
"""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
ENTRY = (ROOT / "SKILL.md").read_text(encoding="utf-8")


class SkillContractTests(unittest.TestCase):
    def test_skill_identity_and_description(self):
        self.assertTrue(ENTRY.startswith("---\nname: analytical-presentations\n"))
        intro = ENTRY.split("---", 2)[1]
        for term in ("refresh", "reimagine", "PowerPoint", "KPI"):
            self.assertIn(term, intro)

    def test_markdown_links_resolve(self):
        sources = [ROOT / "SKILL.md", *(ROOT / "references").glob("*.md"), ROOT / "README.md"]
        for source in sources:
            data = source.read_text(encoding="utf-8")
            for target in re.findall(r"\]\(([^)#]+)(?:#[^)]+)?\)", data):
                if target.startswith(("https://", "http://", "mailto:", "#")):
                    continue
                self.assertTrue((source.parent / target).is_file(), f"Broken link: {source.name} -> {target}")

    def test_core_principles_preserved(self):
        for rule in ("Executive Summary", "Ghost-deck", "One insight per slide", "footers", "speaker", "claim"):
            self.assertIn(rule.lower(), ENTRY.lower())
        for filename in (
            "story-architecture.md", "comparisons-and-evidence.md", "slide-design-and-commentary.md",
            "powerpoint-workflow.md", "quality-gates.md", "client-profile-contract.md",
            "inspiration-and-attribution.md",
        ):
            self.assertTrue((ROOT / "references" / filename).is_file(), filename)

    def test_new_specialist_contracts(self):
        refs = {
            "slide-alternatives.md": ("Comparison-led", "Driver/segment-led", "Decision-led", "editable"),
            "source-refresh-and-reconciliation.md": ("source-lock", "UNVERIFIED", "denominator", "Executive Summary"),
        }
        for filename, tokens in refs.items():
            content = (ROOT / "references" / filename).read_text(encoding="utf-8")
            for token in tokens:
                self.assertIn(token.lower(), content.lower(), f"Missing {token} in {filename}")
            self.assertIn(filename, ENTRY)
        self.assertLess(ENTRY.index("**Combined refresh and redesign:**"), ENTRY.index("## Workflow"))

    def test_regression_suite_has_expected_coverage(self):
        cases = (ROOT / "tests" / "regression-cases.md").read_text(encoding="utf-8")
        ids = re.findall(r"\| (AP-\d{2}) [^|]+\|", cases)
        self.assertEqual(ids, [f"AP-{i:02d}" for i in range(1, 17)])
        for term in ("Missing approved source", "Invalid growth denominator", "Native element preservation", "Mixed refresh and reimagine"):
            self.assertIn(term, cases)

    def test_generic_no_private_profile_or_template_embedded(self):
        self.assertFalse((ROOT / "templates").exists())
        self.assertFalse((ROOT / "assets").exists())
        self.assertIn("approved template", ENTRY)
        self.assertIn("No organization-specific", (ROOT / "README.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
