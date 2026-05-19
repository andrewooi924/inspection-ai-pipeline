BASE_PRIORITY = {
    "critical": 40,
    "high": 25,
    "medium": 10,
    "low": 3,
}

DISPOSITION_BONUS = {
    "hold": 12,
    "reinspect": 6,
    "monitor": 2,
    "pass": 0,
}


class PriorityScorer:
    def compute_score(self, report, patterns):
        severity = report["severity"]
        confidence = report["confidence"]
        image_count = report["image_count"]

        measurements = report["measurements"]

        score = BASE_PRIORITY[severity]

        score += confidence * 10
        score += image_count * 2

        if measurements["void_ratio"] >= 0.20:
            score += 15

        if measurements["misalignment_mm"] >= 0.20:
            score += 10

        if measurements["scratch_length_mm"] >= 6.0:
            score += 8

        pattern_bonus = 0

        for pattern in patterns:
            if report["report_id"] in pattern["supporting_report_ids"]:
                pattern_bonus += 12

        score += pattern_bonus

        score += DISPOSITION_BONUS[report["disposition"]]

        return round(score, 2)