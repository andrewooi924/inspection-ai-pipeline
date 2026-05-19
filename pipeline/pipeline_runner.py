from pipeline.state import PipelineState
from pipeline.stages import PipelineStage

from stages.input_loader import InputLoaderStage
from stages.normalisation_stage import ReportNormalisationStage
from stages.interpretation_stage import InterpretationStage
from stages.pattern_grouping_stage import PatternGroupingStage
from stages.scoring_stage import ScoringStage
from stages.routing_stage import RoutingStage
from stages.explanation_stage import ExplanationStage
from stages.trend_analysis_stage import TrendAnalysisStage
from stages.disagreement_stage import DisagreementStage
from stages.alert_stage import AlertStage
from stages.reinspection_stage import ReinspectionStage
from stages.validation_stage import ValidationStage


class InspectionPipeline:
    def __init__(self):
        self.stages = [
            InputLoaderStage(),
            ReportNormalisationStage(),
            InterpretationStage(),
            PatternGroupingStage(),
            ScoringStage(),
            RoutingStage(),
            ExplanationStage(),
            TrendAnalysisStage(),
            DisagreementStage(),
            AlertStage(),
            ReinspectionStage(),
            ValidationStage(),
        ]

    def run(self):
        state = PipelineState()

        for stage in self.stages:
            state = stage.run(state)

        state.current_stage = PipelineStage.RESULTS_FINALISED

        return state