List of endpoints:
- POST /api/v1/token -> log in and generate a token, send username and password
- POST /api/v1/token/refresh -> refresh tokens, send access token
- POST /api/v1/account/register -> user registration, send username, password and email
- PUT /api/v1/account/change-password -> change password, send old_password and new_password
- POST /api/v1/account/password-reset/ -> request a reset password token by using the email parameter
- POST /api/v1/account/password-reset/confirm/ -> using a valid token, the users password is set to the provided password
- POST /api/v1/account/password-reset/validate_token/ -> will return a 200 if a given token is valid