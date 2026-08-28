import structlog


SERVICE_NAME = "payment-service"
ENVIRONMENT = "development"


structlog.configure(
    processors=[
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


logger.info(
    "user_logged_in",
    user_id=12345,
    login_method="password"
)

logger.warning(
    "multiple_failed_logins",
    user_id=12345,
    failed_attempts=3
)

logger.error(
    "payment_failed",
    user_id=12345,
    order_id="ORD-1001",
    payment_method="card"
)

try:
    result = 10 / 0

except Exception:
    logger.exception(
        "payment_failed",
        user_id=12345,
        order_id="ORD-1001",
    )