# from company_logger import logger
from company_logger_fake import info

info(
    "this_is_not_company_logging",
    password="Secret123",
)

# # Test 1: Normal approved logging
# logger.info(
#     "user_logged_in",
#     user_id=12345,
#     login_method="password",
# )


# # Test 2: Exception logging
# try:
#     result = 10 / 0

# except Exception:
#     logger.exception(
#         "payment_failed",
#         user_id=12345,
#         order_id="ORD-1001",
#     )


# # Test 3: Sensitive data
# logger.info(
#     "user_login",
#     username="niharika",
#     password="MyPassword123",
#     access_token="abc123-secret-token",
# )


