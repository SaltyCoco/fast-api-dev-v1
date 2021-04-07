# api/jwt_token.py

from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
import os
from schema import jwt_token_schema
from configparser import ConfigParser


dir = os.path.dirname(__file__)
cfg = ConfigParser()
cfg.read(os.path.join(dir, 'azure_envs.ini'))
# to get a string like this run:
# openssl rand -hex 32
FASTAPI_SECRET_KEY = cfg.get('envs', 'FASTAPI_SECRET_KEY')
FASTAPI_ALGORITHM = cfg.get('envs', 'FASTAPI_ALGORITHM')
FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES = cfg.get('envs', 'FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES')


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=FASTAPI_ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, FASTAPI_SECRET_KEY, algorithm=FASTAPI_ALGORITHM)
    return encoded_jwt


def verify_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, FASTAPI_SECRET_KEY, algorithms=[FASTAPI_ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = jwt_token_schema.TokenData(email=email)
    except JWTError:
        raise credentials_exception

