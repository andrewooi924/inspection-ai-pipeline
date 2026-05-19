from langdetect import detect
from deep_translator import GoogleTranslator


SUPPORTED_ENGLISH_CODES = {"en"}


class TranslationService:
    def detect_language(self, text: str) -> str:
        try:
            return detect(text)
        except Exception:
            return "unknown"

    def translate_to_english(self, text: str, source_lang: str) -> str:
        if source_lang in SUPPORTED_ENGLISH_CODES:
            return text

        return GoogleTranslator(source="auto", target="en").translate(text)