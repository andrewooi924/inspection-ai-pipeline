from config.controlled_vocab import (
    ALLOWED_DEFECT_CATEGORIES,
    ALLOWED_SEVERITIES,
    ALLOWED_DISPOSITIONS,
    ALLOWED_OWNER_TEAMS,
    ALLOWED_PATTERN_STRENGTHS,
)

def build_interpretation_prompt(normalised_reports):
    return f"""
You are performing manufacturing inspection interpretation.

Allowed defect categories:
{sorted(ALLOWED_DEFECT_CATEGORIES)}

Allowed severities:
{sorted(ALLOWED_SEVERITIES)}

Allowed dispositions:
{sorted(ALLOWED_DISPOSITIONS)}

Use both measurements and translated note text.

Output schema:
{{
  \"reports\": [
    {{
      \"report_id\": \"string\",
      \"defect_category\": \"string\",
      \"severity\": \"string\",
      \"disposition\": \"string\",
      \"reason_short\": \"string\",
      \"translated\": true,
      \"original_language\": \"string\"
    }}
  ]
}}

Reports:
{normalised_reports}
"""


def build_pattern_prompt(interpreted_payload):
    return f"""
Identify recurring process-related defect patterns.

Allowed pattern strengths:
{sorted(ALLOWED_PATTERN_STRENGTHS)}

Use interpreted report outputs plus timestamps, stations,
confidence values, measurements, and translated notes.

Output schema:
{{
  \"patterns\": [
    {{
      \"pattern_id\": \"string\",
      \"title\": \"string\",
      \"supporting_report_ids\": [\"R01\"],
      \"pattern_strength\": \"strong\",
      \"likely_driver\": \"string\",
      \"recommended_action\": \"string\"
    }}
  ]
}}

Input:
{interpreted_payload}
"""


def build_routing_prompt(top_cases, patterns):
    return f"""
Route inspection cases to the correct teams.

Allowed owner teams:
{sorted(ALLOWED_OWNER_TEAMS)}

Output schema:
{{
  \"routes\": [
    {{
      \"report_id\": \"string\",
      \"teams\": [\"Quality\"],
      \"briefing_note\": \"string\"
    }}
  ]
}}

Top cases:
{top_cases}

Patterns:
{patterns}
"""