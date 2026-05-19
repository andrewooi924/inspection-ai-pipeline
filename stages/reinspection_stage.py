from pipeline.utils import save_markdown


class ReinspectionStage:
    def run(self, state):
        content = "# Reinspection Plan\n\n"
        content += "## Priority Sampling\n"
        content += "- Inspect recurring defect parts first.\n"
        content += "- Prioritise stations involved in strong recurring patterns.\n\n"

        content += "## Defect Signatures\n"
        content += "- Solder void clustering near BGA and connector joints.\n"
        content += "- Progressive scratch length increases.\n"
        content += "- Pin alignment drift.\n\n"

        content += "## Stop Criteria\n"
        content += "- Stop production if multiple high severity recurring cases emerge in same station window.\n\n"

        content += "## Continue Criteria\n"
        content += "- Continue if reinspections remain below escalation thresholds.\n\n"

        content += "## Owner Teams\n"
        content += "- Quality\n"
        content += "- Process Engineering\n"

        save_markdown(
            "outputs/reinspection_plan.md",
            content,
        )

        return state