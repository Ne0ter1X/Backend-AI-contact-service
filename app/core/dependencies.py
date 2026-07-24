from app.services.ai_service import AIService
from app.services.email_service import EmailService
from app.services.rate_limit_service import RateLimitService

from app.repositories.stats_repository import StatsRepository

from app.services.contact_service import ContactService

ai_service = AIService()
email_service = EmailService()
stats_repository = StatsRepository()

rate_limit_service = RateLimitService()

contact_service = ContactService(
    ai_service,
    email_service,
    stats_repository,
    rate_limit_service,
)
