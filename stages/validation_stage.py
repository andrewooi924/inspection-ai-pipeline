from pathlib import Path
from pipeline.stages import PipelineStage


class ValidationStage:
    REQUIRED_FILES = [
        "outputs/normalised_reports.json",
        "outputs/interpreted_reports.json",
        "outputs/patterns.json",
        "outputs/priority_scores.json",
        "outputs/case_routing.json",
        "outputs/review_summaries.md",
        "outputs/llm_calls.jsonl",
    ]

    def run(self, state):
        for path in self.REQUIRED_FILES:
            assert Path(path).exists(), f"Missing {path}"

        state.current_stage = PipelineStage.VALIDATION_COMPLETE

        return state