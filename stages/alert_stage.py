from pipeline.utils import save_json


class AlertStage:
    def run(self, state):
        high_scores = [
            r["priority_score"]
            for r in state.top_cases
        ]

        max_score = max(high_scores)

        if max_score >= 75:
            alert = "red"
        elif max_score >= 60:
            alert = "orange"
        elif max_score >= 40:
            alert = "yellow"
        else:
            alert = "green"

        result = {
            "alert_rating": alert,
            "justification": {
                "top_reports": [
                    r["report_id"]
                    for r in state.top_cases
                ],
                "pattern_count": len(state.patterns),
            },
            "recommended_operational_posture": "Increase inspection frequency and perform engineering containment review.",
        }

        save_json(
            "outputs/alert_rating.json",
            result,
        )

        return state