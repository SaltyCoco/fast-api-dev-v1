# api/authentication.py

from fastapi import APIRouter
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from databases.database import get_db
from models import users_models
from api.hashing import Hash
from api.jwt_token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm



router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
async def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(users_models.User).filter(users_models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Invalid Credentials")
    if not Hash.verify(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Incorrect Credentials")
    # generate a jwt token and return
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
