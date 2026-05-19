from pipeline.validators import validate_interpreted_reports


def test_vocab_validation():
    reports = [
        {
            "defect_category": "surface_scratch",
            "severity": "medium",
            "disposition": "monitor",
        }
    ]

    validate_interpreted_reports(reports)