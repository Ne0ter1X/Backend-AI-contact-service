from app.core.logger import logger


class ContactService:

    def __init__(
        self,
        ai_service,
        email_service,
        stats_repository,
        rate_limit_service,
    ):
        self.ai_service = ai_service
        self.email_service = email_service
        self.stats_repository = stats_repository
        self.rate_limit_service = rate_limit_service

    async def process(
            self,
            request,
            ip: str,
    ):
        self.rate_limit_service.check(ip)

        sentiment = await self.ai_service.analyze_sentiment(
            request.comment
        )

        self.stats_repository.increment(sentiment)

        owner_message = f"""
        New contact request

        Name: {request.name}

        Email: {request.email}

        Phone: {request.phone}

        Comment:

        {request.comment}

        Sentiment:

        {sentiment}
        """

        await self.email_service.send_to_owner(
            subject="New contact request",
            body=owner_message,
        )

        await self.email_service.send_confirmation(
            email=request.email,
            subject="We received your request",
            body="Thank you! We will contact you soon."
        )

        logger.info(
            f"Contact request from {request.email}"
        )

        return {
            "message": "Success",
            "sentiment": sentiment,
        }
