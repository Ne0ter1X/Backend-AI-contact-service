from openai import AsyncOpenAI
from app.core.config import settings
from app.core.logger import logger


class AIService:
    def __init__(self):
        self.client = AsyncOpenAI(
            api_key=settings.openai_api_key
        )

    async def analyze_sentiment(
            self,
            text: str,
    ) -> str:
        try:
            response = await self.client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "Return only one word: "
                            "positive, neutral or negative."
                        ),
                    },
                    {
                        "role": "user",
                        "content": text,
                    },
                ],
                temperature=0,
            )

            sentiment = (
                response.choices[0]
                .message.content
                .strip()
                .lower()
            )

            if sentiment not in {
                "positive",
                "neutral",
                "negative",
            }:
                return "unknown"

            return sentiment
        except Exception as e:
            logger.warning(
                f"AI unavailable: {e}"
            )

            return "unknown"
