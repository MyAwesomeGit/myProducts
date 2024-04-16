from typing import Optional
import secrets
import uvicorn
from fastapi import FastAPI, HTTPException, status, Cookie, Response, Body, Depends
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from controllers.product_manager import ProductManager
from models.products import products

app = FastAPI()


@app.get("/get_product/{product_id}")
async def get_product(product_id: int):
    product_manager = ProductManager(product_id=product_id,
                                     products=products)
    return await product_manager.get_product()


@app.get("/search_products")
async def search_products(keyword: str, category: Optional[str] = None, limit: Optional[int] = 10):
    product_manager = ProductManager(product_id=None,
                                     products=products,
                                     keyword=keyword,
                                     category=category,
                                     limit=limit)
    return await product_manager.search_products()


# TODO: Remove User to separate class
class User(BaseModel):
    username: str
    password: str


# TODO: Remove sample_db to separate entity
sample_db = [
    User(username="test", password="123"),
    User(username="hello", password="111")
]

sessions: dict = {}


@app.post("/login")
async def login(user: User = Body(...), response: Response = Response()):
    for person in sample_db:
        if person.username == user.username and person.password == user.password:
            session_token = secrets.token_hex(16)
            sessions[session_token] = user
            response.set_cookie(key="session_token", value=session_token, httponly=True)
            return {"detail": "Login successful"}, status.HTTP_200_OK, response
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.get('/user')
async def user_info(session_token: str = Cookie(None)):
    if session_token:
        return {"session_token": session_token}
    return {"message": "Unauthorized"}


security = HTTPBasic()


def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    user = get_user_from_db(credentials.username)
    if user is None or user.password != credentials.password:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user


def get_user_from_db(username: str):
    for user in sample_db:
        if user.username == username:
            return user
    return None


@app.post('/login_with_basic_auth')
def login_with_basic_auth(user: User = Depends(authenticate_user)):
    return {"message": "Login successful", "user_info": user}


if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)
