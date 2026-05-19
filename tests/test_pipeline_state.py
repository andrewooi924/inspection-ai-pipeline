from pipeline.stages import PipelineStage


def test_pipeline_stage_enum():
    assert PipelineStage.INIT.value == "INIT"