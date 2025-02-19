import secrets

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

print("Generated SECRET_KEY:", SECRET_KEY)
