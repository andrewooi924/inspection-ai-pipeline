from pipeline.prompts import build_pattern_prompt
from pipeline.utils import save_json
from pipeline.validators import validate_patterns
from pipeline.llm_client import LLMClient
from pipeline.llm_logger import LLMLogger
from pipeline.stages import PipelineStage


class PatternGroupingStage:
    def __init__(self):
        self.client = LLMClient()
        self.logger = LLMLogger()

    def run(self, state):
        prompt = build_pattern_prompt(
            state.interpreted_reports
        )

        result = self.client.generate_json(prompt)

        patterns = result["patterns"]

        validate_patterns(patterns)

        state.patterns = patterns

        save_json(
            "outputs/patterns.json",
            patterns,
        )

        self.logger.log(
            stage="PATTERN_GROUPING",
            provider="OpenAI",
            model=self.client.model,
            prompt=prompt,
            input_artifacts=[
                "outputs/interpreted_reports.json"
            ],
            output_artifact="outputs/patterns.json",
        )

        state.current_stage = PipelineStage.PATTERNS_GROUPED

        return state