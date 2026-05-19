from pipeline.utils import save_markdown
from pipeline.stages import PipelineStage


class ExplanationStage:
    def run(self, state):
        markdown = "# Prioritised Review Cases\n\n"

        for report in state.top_cases:
            recurring = (
                "Yes"
                if report["pattern_ids"]
                else "No"
            )

            markdown += f"## {report['report_id']} - {report['part_name']}\n\n"
            markdown += f"- Defect Category: {report['defect_category']}\n"
            markdown += f"- Severity: {report['severity']}\n"
            markdown += f"- Disposition: {report['disposition']}\n"
            markdown += f"- Priority Score: {report['priority_score']}\n"
            markdown += f"- Recurring Pattern: {recurring}\n"
            markdown += f"- Explanation: Elevated due to severity, confidence, evidence count, and measurement thresholds.\n"
            markdown += "- Human Review Gate: Verify raw inspection imagery, dimensional thresholds, and process traceability before any production disposition decision.\n\n"

        save_markdown(
            "outputs/review_summaries.md",
            markdown,
        )

        state.current_stage = PipelineStage.EXPLANATIONS_GENERATED

        return state