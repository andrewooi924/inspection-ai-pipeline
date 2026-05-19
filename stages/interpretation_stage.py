from pipeline.prompts import build_interpretation_prompt
from pipeline.utils import save_json
from pipeline.validators import validate_interpreted_reports
from pipeline.llm_client import LLMClient
from pipeline.llm_logger import LLMLogger
from pipeline.stages import PipelineStage


class InterpretationStage:
    def __init__(self):
        self.client = LLMClient()
        self.logger = LLMLogger()

    def run(self, state):
        prompt = build_interpretation_prompt(
            state.normalised_reports
        )

        result = self.client.generate_json(prompt)

        interpreted = result["reports"]

        validate_interpreted_reports(interpreted)

        merged = []

        for base in state.normalised_reports:
            match = next(
                r for r in interpreted
                if r["report_id"] == base["report_id"]
            )

            merged.append({**base, **match})

        state.interpreted_reports = merged

        save_json(
            "outputs/interpreted_reports.json",
            merged,
        )

        self.logger.log(
            stage="REPORT_INTERPRETATION",
            provider="OpenAI",
            model=self.client.model,
            prompt=prompt,
            input_artifacts=[
                "outputs/normalised_reports.json"
            ],
            output_artifact="outputs/interpreted_reports.json",
        )

        state.current_stage = PipelineStage.REPORTS_INTERPRETED

        return state