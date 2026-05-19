from collections import Counter
from pipeline.utils import save_json


class TrendAnalysisStage:
    def run(self, state):
        defect_distribution = Counter(
            r["defect_category"]
            for r in state.interpreted_reports
        )

        station_distribution = Counter(
            r["station"]
            for r in state.interpreted_reports
        )

        trend_summary = {
            "defect_distribution": defect_distribution,
            "most_affected_station": station_distribution.most_common(1)[0][0],
            "worsening_pattern_detected": any(
                p["pattern_strength"] == "strong"
                for p in state.patterns
            ),
        }

        save_json(
            "outputs/shift_trends.json",
            trend_summary,
        )

        return state