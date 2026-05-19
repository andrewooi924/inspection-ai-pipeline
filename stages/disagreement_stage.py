from pipeline.utils import save_json


class DisagreementStage:
    def run(self, state):
        disagreements = []

        for report in state.interpreted_reports:
            weak_alignment = (
                report["confidence"] < 0.70
                # and report["severity"] in ["high", "critical"]
            )

            if weak_alignment:
                disagreements.append({
                    "report_id": report["report_id"],
                    "disagreement_reason": "Low confidence but elevated interpreted severity.",
                    "recommended_follow_up": "Manual engineering review and secondary inspection validation.",
                })

        save_json(
            "outputs/disagreement_cases.json",
            disagreements,
        )

        return state