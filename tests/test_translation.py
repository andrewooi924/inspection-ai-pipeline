from pipeline.translation import TranslationService


def test_language_detection():
    service = TranslationService()

    result = service.detect_language(
        "penjajaran pin di sebelah kiri nampak senget sedikit"
    )

    assert result == "ms"