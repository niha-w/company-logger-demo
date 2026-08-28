import os

import structlog


SERVICE_NAME = os.getenv(
    "SERVICE_NAME",
    "unknown-service",
)

ENVIRONMENT = os.getenv(
    "ENVIRONMENT",
    "development",
)


SENSITIVE_FIELDS = {
    "password",
    "passwd",
    "pwd",
    "access_token",
    "refresh_token",
    "api_key",
    "apikey",
    "secret",
    "authorization",
    "credit_card",
    "card_number",
}


def redact_sensitive_data(logger, method_name, event_dict):
    """
    Replace sensitive values with [REDACTED].
    """

    for field in SENSITIVE_FIELDS:
        if field in event_dict:
            event_dict[field] = "[REDACTED]"

    return event_dict


structlog.configure(
    processors=[
        redact_sensitive_data,
        structlog.processors.TimeStamper(fmt="iso", utc=True),
        structlog.processors.add_log_level,
        structlog.processors.format_exc_info,
        structlog.processors.JSONRenderer(),
    ]
)


logger = structlog.get_logger().bind(
    service=SERVICE_NAME,
    environment=ENVIRONMENT,
)