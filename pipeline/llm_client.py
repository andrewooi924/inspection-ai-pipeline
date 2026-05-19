import json
from openai import OpenAI


class LLMClient:
    def __init__(self, model="gpt-4.1-mini"):
        self.client = OpenAI()
        self.model = model

    def generate_json(self, prompt: str):
        response = self.client.chat.completions.create(
            model=self.model,
            temperature=0,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a manufacturing inspection analysis assistant. "
                        "Always return valid JSON only."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return json.loads(
            response.choices[0].message.content
        )