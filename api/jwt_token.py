# api/jwt_token.py

from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
import os
from schema import jwt_token_schema
from fastapi import Depends, status, HTTPException

# to get a string like this run:
# openssl rand -hex 32
FASTAPI_SECRET_KEY = os.getenv('FASTAPI_SECRET_KEY')
FASTAPI_ALGORITHM = os.getenv('FASTAPI_ALGORITHM')
FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES = os.getenv('FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES')


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, FASTAPI_SECRET_KEY, algorithm=FASTAPI_ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, os.getenv('FASTAPI_SECRET_KEY'), algorithms=[os.getenv('FASTAPI_ALGORITHM')])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = jwt_token_schema.TokenData(email=email)
    except JWTError:
        raise credentials_exception

