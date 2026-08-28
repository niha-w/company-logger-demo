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