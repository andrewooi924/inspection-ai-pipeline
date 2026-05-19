from pipeline.scoring import PriorityScorer


def test_priority_scoring():
    scorer = PriorityScorer()

    report = {
        "severity": "high",
        "confidence": 0.9,
        "image_count": 4,
        "measurements": {
            "void_ratio": 0.22,
            "misalignment_mm": 0.0,
            "scratch_length_mm": 0.0,
        },
        "disposition": "hold",
        "report_id": "R01",
    }

    patterns = [
        {
            "supporting_report_ids": ["R01"]
        }
    ]

    score = scorer.compute_score(report, patterns)

    assert score > 0