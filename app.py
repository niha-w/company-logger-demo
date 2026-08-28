from company_logger import logger


logger.info(
    "user_logged_in",
    user_id=12345,
    login_method="password",
)


try:
    result = 10 / 0

except Exception:
    logger.exception(
        "payment_failed",
        user_id=12345,
        order_id="ORD-1001",
    )

logger.info(
    "user_login",
    username="niharika",
    password="MyPassword123",
    access_token="abc123-secret-token",
)