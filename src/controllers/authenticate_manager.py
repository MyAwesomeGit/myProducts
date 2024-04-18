import secrets
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials, HTTPBasic
from models.products_user_db import ProductsUserDB


class AuthenticateManager:
    def __init__(self, credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
        self.credentials = credentials

    def get_user_from_db(self):
        for user in ProductsUserDB.database:
            if user.username == self.credentials.username:
                return user
        return None

    def authenticate_user(self):
        user = self.get_user_from_db()
        if user is None or not secrets.compare_digest(user.password, self.credentials.password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        return user

