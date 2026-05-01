from __future__ import annotations

import mimetypes
import os
import smtplib
from dataclasses import dataclass
from email.message import EmailMessage
from pathlib import Path


class EmailConfigError(ValueError):
    pass


@dataclass(frozen=True)
class EmailSettings:
    host: str
    port: int
    username: str
    password: str
    sender: str
    recipients: list[str]
    starttls: bool = True
    ssl: bool = False

    @classmethod
    def from_args_env(cls, args, require_server: bool = True) -> "EmailSettings":
        host = args.smtp_host or os.getenv("IAR_DRP_SMTP_HOST", "")
        port_value = args.smtp_port or os.getenv("IAR_DRP_SMTP_PORT") or "587"
        username = args.smtp_user or os.getenv("IAR_DRP_SMTP_USERNAME", "")
        password = args.smtp_password or os.getenv("IAR_DRP_SMTP_PASSWORD", "")
        sender = args.smtp_from or os.getenv("IAR_DRP_SMTP_FROM", "")
        recipients = _split_recipients(args.smtp_to or os.getenv("IAR_DRP_SMTP_TO", ""))
        ssl = _truthy(os.getenv("IAR_DRP_SMTP_SSL", "false"))
        starttls = not args.no_starttls and not ssl

        if require_server:
            missing = []
            if not host:
                missing.append("IAR_DRP_SMTP_HOST")
            if not sender:
                missing.append("IAR_DRP_SMTP_FROM")
            if not recipients:
                missing.append("IAR_DRP_SMTP_TO")
            if missing:
                raise EmailConfigError(
                    "Missing required email configuration: " + ", ".join(missing)
                )

        try:
            port = int(port_value)
        except ValueError as exc:
            raise EmailConfigError("IAR_DRP_SMTP_PORT must be an integer.") from exc

        return cls(
            host=host,
            port=port,
            username=username,
            password=password,
            sender=sender,
            recipients=recipients,
            starttls=starttls,
            ssl=ssl,
        )


def send_email(
    settings: EmailSettings,
    subject: str,
    body: str,
    attachments: list[Path] | None = None,
    dry_run: bool = False,
) -> None:
    attachments = attachments or []
    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = settings.sender
    message["To"] = ", ".join(settings.recipients)
    message.set_content(body)

    for attachment in attachments:
        _attach_file(message, attachment)

    if dry_run:
        print("Dry run: email not sent.")
        print(f"From: {settings.sender}")
        print(f"To: {', '.join(settings.recipients)}")
        print(f"Subject: {subject}")
        for attachment in attachments:
            print(f"Attachment: {attachment}")
        return

    if settings.ssl:
        with smtplib.SMTP_SSL(settings.host, settings.port, timeout=60) as server:
            _login_if_needed(server, settings)
            server.send_message(message)
        return

    with smtplib.SMTP(settings.host, settings.port, timeout=60) as server:
        if settings.starttls:
            server.starttls()
        _login_if_needed(server, settings)
        server.send_message(message)


def _attach_file(message: EmailMessage, path: Path) -> None:
    if not path.exists():
        return
    content_type, _ = mimetypes.guess_type(path.name)
    if content_type:
        maintype, subtype = content_type.split("/", 1)
    else:
        maintype, subtype = "application", "octet-stream"
    message.add_attachment(
        path.read_bytes(),
        maintype=maintype,
        subtype=subtype,
        filename=path.name,
    )


def _login_if_needed(server, settings: EmailSettings) -> None:
    if settings.username or settings.password:
        server.login(settings.username, settings.password)


def _split_recipients(value: str) -> list[str]:
    normalized = value.replace(";", ",")
    return [part.strip() for part in normalized.split(",") if part.strip()]


def _truthy(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "y"}
