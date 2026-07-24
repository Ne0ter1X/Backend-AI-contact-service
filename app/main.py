from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.controllers.contact_controller import (
    router as contact_router,
)
from app.controllers.health_controller import (
    router as health_router,
)

from app.core.exception_handler import (
    global_exception_handler,
)

from app.core.logger_middleware import (
    LoggingMiddleware,
)

from app.services.ai_service import AIService
from app.services.email_service import EmailService
from app.services.rate_limit_service import RateLimitService

from app.repositories.stats_repository import StatsRepository

from app.services.contact_service import ContactService

app = FastAPI(
    title="Landing Backend API",
    version="1.0.0",
)

ai_service = AIService()
email_service = EmailService()
stats_repository = StatsRepository()
rate_limit_service = RateLimitService()

contact_service = ContactService(
    ai_service=ai_service,
    email_service=email_service,
    stats_repository=stats_repository,
    rate_limit_service=rate_limit_service,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(
    LoggingMiddleware,
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.include_router(
    contact_router,
    prefix="/api",
)

app.include_router(
    health_router,
    prefix="/api",
)


