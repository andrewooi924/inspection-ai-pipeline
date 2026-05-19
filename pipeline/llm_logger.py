import json
from datetime import datetime, UTC
from hashlib import sha256


class LLMLogger:
    def __init__(self, path="outputs/llm_calls.jsonl"):
        self.path = path

    def log(
        self,
        stage,
        provider,
        model,
        prompt,
        input_artifacts,
        output_artifact,
    ):
        record = {
            "stage": stage,
            "timestamp": datetime.now(UTC).isoformat(),
            "provider": provider,
            "model": model,
            "prompt_hash": sha256(prompt.encode()).hexdigest(),
            "input_artifacts": input_artifacts,
            "output_artifact": output_artifact,
        }

        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")