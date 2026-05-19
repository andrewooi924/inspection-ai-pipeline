from pipeline.utils import load_json
from pipeline.stages import PipelineStage


class InputLoaderStage:
    def run(self, state):
        state.reports = load_json("data/inspection_reports.json")
        state.parts_catalog = load_json("data/parts_catalog.json")

        state.current_stage = PipelineStage.INPUTS_LOADED

        return state