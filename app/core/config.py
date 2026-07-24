from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    openai_api_key: str

    smtp_host: str
    smtp_port: int
    smtp_username: str | None = None
    smtp_password: str | None = None

    smtp_use_tls: bool = False

    owner_email: str
    from_email: str

    rate_limit_requests: int = 5
    rate_limit_window: int = 60

    class Config:
        env_file = ".env"


settings = Settings()
