from pipeline.prompts import build_routing_prompt
from pipeline.utils import save_json
from pipeline.validators import validate_routing
from pipeline.llm_client import LLMClient
from pipeline.llm_logger import LLMLogger
from pipeline.stages import PipelineStage


class RoutingStage:
    def __init__(self):
        self.client = LLMClient()
        self.logger = LLMLogger()

    def run(self, state):
        prompt = build_routing_prompt(
            state.top_cases,
            state.patterns,
        )

        result = self.client.generate_json(prompt)

        routes = result["routes"]

        validate_routing(routes)

        state.routed_cases = routes

        save_json(
            "outputs/case_routing.json",
            routes,
        )

        self.logger.log(
            stage="CASE_ROUTING",
            provider="OpenAI",
            model=self.client.model,
            prompt=prompt,
            input_artifacts=[
                "outputs/priority_scores.json",
                "outputs/patterns.json",
            ],
            output_artifact="outputs/case_routing.json",
        )

        state.current_stage = PipelineStage.ROUTING_COMPLETE

        return state