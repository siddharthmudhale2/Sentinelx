from passlib.context import CryptContext

from jose import jwt
from jose import JWTError

from datetime import datetime, timedelta

from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# JWT configuration
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(
    os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES")
)

# Password hashing config
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

# Hash password
def hash_password(password: str):
    return pwd_context.hash(password)

# Verify password
def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )

# Generate JWT token
def create_access_token(data: dict):

    to_encode = data.copy()

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt