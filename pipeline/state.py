from dataclasses import dataclass, field
from typing import List, Dict, Any

from pipeline.stages import PipelineStage


@dataclass
class PipelineState:
    current_stage: PipelineStage = PipelineStage.INIT
    reports: List[Dict[str, Any]] = field(default_factory=list)
    parts_catalog: List[Dict[str, Any]] = field(default_factory=list)
    normalised_reports: List[Dict[str, Any]] = field(default_factory=list)
    interpreted_reports: List[Dict[str, Any]] = field(default_factory=list)
    patterns: List[Dict[str, Any]] = field(default_factory=list)
    scored_reports: List[Dict[str, Any]] = field(default_factory=list)
    top_cases: List[Dict[str, Any]] = field(default_factory=list)
    routed_cases: List[Dict[str, Any]] = field(default_factory=list)