from pipeline.pipeline_runner import InspectionPipeline


if __name__ == "__main__":
    pipeline = InspectionPipeline()
    pipeline.run()

    print("Pipeline completed successfully.")