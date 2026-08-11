from google import genai

from app.config import GEMINI_API_KEY


class SummaryService:

    def __init__(self):
        self.client = None

    def _get_client(self):
        if self.client is None:

            if not GEMINI_API_KEY:
                raise ValueError(
                    "GEMINI_API_KEY is not configured."
                )

            self.client = genai.Client(
                api_key=GEMINI_API_KEY
            )

        return self.client

    def summarize(self, text: str) -> str:

        client = self._get_client()

        prompt = f"""
You are a financial research assistant.

Summarize the following Investor Relations document
for an investment analyst.

Focus on:

- purpose of the document
- important dates
- financial or business information
- management information
- important events
- key takeaways

Do not invent information.

Document:

{text}
"""

        response = client.models.generate_content(
            model="gemini-3.5-flash",
            contents=prompt
        )

        return response.text