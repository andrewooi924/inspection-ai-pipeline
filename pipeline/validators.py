from config.controlled_vocab import (
    ALLOWED_DEFECT_CATEGORIES,
    ALLOWED_SEVERITIES,
    ALLOWED_DISPOSITIONS,
    ALLOWED_OWNER_TEAMS,
    ALLOWED_PATTERN_STRENGTHS,
)


def validate_interpreted_reports(reports):
    for report in reports:
        assert report["defect_category"] in ALLOWED_DEFECT_CATEGORIES
        assert report["severity"] in ALLOWED_SEVERITIES
        assert report["disposition"] in ALLOWED_DISPOSITIONS


def validate_patterns(patterns):
    for pattern in patterns:
        assert pattern["pattern_strength"] in ALLOWED_PATTERN_STRENGTHS


def validate_routing(routed_cases):
    for case in routed_cases:
        for team in case["teams"]:
            assert team in ALLOWED_OWNER_TEAMS