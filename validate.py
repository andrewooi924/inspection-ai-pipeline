import json
from pathlib import Path

from config.controlled_vocab import (
    ALLOWED_DEFECT_CATEGORIES,
    ALLOWED_SEVERITIES,
    ALLOWED_DISPOSITIONS,
    ALLOWED_OWNER_TEAMS,
)


REQUIRED_ARTIFACTS = [
    "outputs/normalised_reports.json",
    "outputs/interpreted_reports.json",
    "outputs/patterns.json",
    "outputs/priority_scores.json",
    "outputs/case_routing.json",
    "outputs/review_summaries.md",
    "outputs/llm_calls.jsonl",
]


for artifact in REQUIRED_ARTIFACTS:
    assert Path(artifact).exists(), f"Missing artifact: {artifact}"


with open("outputs/interpreted_reports.json") as f:
    interpreted = json.load(f)


for report in interpreted:
    assert report["defect_category"] in ALLOWED_DEFECT_CATEGORIES
    assert report["severity"] in ALLOWED_SEVERITIES
    assert report["disposition"] in ALLOWED_DISPOSITIONS


with open("outputs/case_routing.json") as f:
    routed = json.load(f)


for case in routed:
    for team in case["teams"]:
        assert team in ALLOWED_OWNER_TEAMS


with open("outputs/priority_scores.json") as f:
    scored_reports = json.load(f)


top_cases = scored_reports[:5]


with open("outputs/review_summaries.md") as f:
    review_content = f.read()


for report in top_cases:
    assert report["report_id"] in review_content
    assert "Human Review Gate" in review_content


print("Validation successful.")