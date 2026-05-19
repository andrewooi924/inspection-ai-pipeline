from pipeline.translation import TranslationService
from pipeline.utils import save_json
from pipeline.stages import PipelineStage


class ReportNormalisationStage:
    def __init__(self):
        self.translation_service = TranslationService()

    def run(self, state):
        catalog_lookup = {
            part["part_id"]: part
            for part in state.parts_catalog
        }

        normalised = []

        for report in state.reports:
            language = self.translation_service.detect_language(
                report["operator_note"]
            )

            translated = language != "en"

            note = report["operator_note"]

            if translated:
                note = self.translation_service.translate_to_english(
                    report["operator_note"],
                    language,
                )

            part_info = catalog_lookup[report["part_id"]]

            normalised_record = {
                **report,
                "part_name": part_info["part_name"],
                "product_line": part_info["product_line"],
                "original_operator_note": report["operator_note"],
                "note_for_interpretation": note,
                "original_language": language,
                "translated": translated,
            }

            normalised.append(normalised_record)

        state.normalised_reports = normalised

        save_json(
            "outputs/normalised_reports.json",
            normalised,
        )

        state.current_stage = PipelineStage.REPORTS_NORMALISED

        return state