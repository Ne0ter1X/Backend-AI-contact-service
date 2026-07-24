import smtplib
from email.message import EmailMessage

from app.core.config import settings
from app.core.logger import logger


class EmailService:

    async def send_to_owner(
        self,
        subject: str,
        body: str,
    ):
        try:
            msg = EmailMessage()

            msg["Subject"] = subject
            msg["From"] = settings.from_email
            msg["To"] = settings.owner_email

            msg.set_content(body)

            with smtplib.SMTP(
                    settings.smtp_host,
                    settings.smtp_port,
            ) as smtp:
                # Uncomment IFs if using MailPit for test
                # if settings.smtp_use_tls:
                smtp.starttls()
                # if settings.smtp_username and settings.smtp_password:
                smtp.login(
                        settings.smtp_username,
                        settings.smtp_password,
                )

                smtp.send_message(msg)

        except Exception:

            logger.exception(
                "Owner email sending failed"
            )
            raise


    async def send_confirmation(
            self,
            email: str,
            subject: str,
            body: str,
    ):
        try:

            msg = EmailMessage()

            msg["Subject"] = subject
            msg["From"] = settings.from_email
            msg["To"] = email

            msg.set_content(body)

            with smtplib.SMTP(
                    settings.smtp_host,
                    settings.smtp_port,
            ) as smtp:
                # MailPit setup
                # if settings.smtp_use_tls:
                #     smtp.starttls()
                smtp.starttls()
                # if settings.smtp_username and settings.smtp_password:
                #     smtp.login(
                #         settings.smtp_username,
                #         settings.smtp_password,
                #     )
                smtp.login(
                    settings.smtp_username,
                    settings.smtp_password,
                )

                smtp.send_message(msg)

        except Exception:

            logger.exception(
                "Confirmation email failed"
            )

            raise
