from pipeline.scoring import PriorityScorer
from pipeline.utils import save_json
from pipeline.stages import PipelineStage


class ScoringStage:
    def __init__(self):
        self.scorer = PriorityScorer()

    def run(self, state):
        scored = []

        for report in state.interpreted_reports:
            score = self.scorer.compute_score(
                report,
                state.patterns,
            )

            pattern_ids = []

            for pattern in state.patterns:
                if report["report_id"] in pattern["supporting_report_ids"]:
                    pattern_ids.append(pattern["pattern_id"])

            enriched = {
                **report,
                "priority_score": score,
                "pattern_ids": pattern_ids,
            }

            scored.append(enriched)

        scored.sort(
            key=lambda x: x["priority_score"],
            reverse=True,
        )

        top_cases = scored[:5]

        state.scored_reports = scored
        state.top_cases = top_cases

        save_json(
            "outputs/priority_scores.json",
            scored,
        )

        state.current_stage = PipelineStage.PRIORITIES_COMPUTED

        return state