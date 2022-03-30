from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from server.models.user import (
    Token,
    User,
    authenticate_user,
    create_access_token,
    get_current_active_user,
    fake_users_db,
)
from fastapi.security import OAuth2PasswordRequestForm
from buko.config import ACCESS_TOKEN_EXPIRE_MINUTES


router = APIRouter()


@router.get("/me", response_description="User retrieved")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    return current_user


@router.post("/token", response_model=Token, response_description="Token retrieved")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
