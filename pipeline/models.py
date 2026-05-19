from pydantic import BaseModel
from typing import List


class InterpretedReport(BaseModel):
    report_id: str
    defect_category: str
    severity: str
    disposition: str
    reason_short: str
    translated: bool
    original_language: str


class PatternGroup(BaseModel):
    pattern_id: str
    title: str
    supporting_report_ids: List[str]
    pattern_strength: str
    likely_driver: str
    recommended_action: str


class RoutedCase(BaseModel):
    report_id: str
    teams: List[str]
    briefing_note: str