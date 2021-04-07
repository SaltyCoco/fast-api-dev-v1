# api/oauth2.py

import os
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from jose import jwt, JWTError



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return token.verify_token(token, credentials_exception)