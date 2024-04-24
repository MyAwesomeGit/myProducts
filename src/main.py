import datetime
from typing import Optional
import secrets
import jwt
import uvicorn
from fastapi import FastAPI, HTTPException, status, Cookie, Response, Body, Depends, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from controllers.product_manager import ProductManager
from controllers.authenticate_manager import AuthenticateManager
from models.products import products
from models.products_sessions import products_sessions
from models.products_user import ProductsUser
from models.products_user_db import ProductsUserDB

app = FastAPI()
security = HTTPBasic()


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


@app.post("/create_session_token")
async def create_session_token(user: ProductsUser = Body(...), response: Response = Response()):
    for person in ProductsUserDB.database:
        if person.username == user.username and person.password == user.password and person.access_permission is not None:
            session_token = secrets.token_hex(16)
            products_sessions[session_token] = user
            response.set_cookie(key="session_token", value=session_token)
            return {"detail": "Login successful"}, status.HTTP_200_OK, response
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )


@app.get('/user_session_token')
async def user_session_token(session_token: str = Cookie(None)):
    if session_token:
        return {"session_token": session_token}
    return {"message": "Unauthorized"}


"""Authentication with basic info"""


@app.post('/login_with_basic_auth')
def login_with_basic_auth(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    response_data = {}
    try:
        authenticate_manager = AuthenticateManager(credentials=credentials)
        user = authenticate_manager.authenticate_user()
        response_data = {
            "message": "Login successful",
            "user_info": user
        }
    except Exception as e:
        exception_message = str(e)
        response_data = {
            "message": "Login error",
            "user_info": exception_message
        }
    finally:
        return response_data


"""Authentication with JWT"""
SECRET_KEY = "my_secret_key"
ALGORITHM = "HS256"


# TODO: Remove to separate entity
def create_access_token(data: dict, expires_delta: datetime.timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.datetime.utcnow() + expires_delta
    else:
        expire = datetime.datetime.utcnow() + datetime.timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post('/authorization')
async def authorization(credentials: HTTPBasicCredentials = Depends(HTTPBasic())):
    response_data = {}
    try:
        authenticate_manager = AuthenticateManager(credentials=credentials)
        user = authenticate_manager.authenticate_user()
        if user:
            access_token = create_access_token(data={"sub": credentials.username,
                                                     "access_level": user.access_level})
            response_data = {
                "access_token": access_token,
                "user_access_level": user.access_level
            }
        else:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
    except Exception as e:
        exception_message = str(e)
        response_data = {
            "message": exception_message
        }
    finally:
        return response_data


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# TODO: Remove to separate entity
async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        access_level: str = payload.get("access_level")
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials",
            )
        permissions = ProductsUserDB.get_permissions(access_level)
        return {
            "username": username,
            "access_level": access_level,
            "permissions": permissions
        }
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )


@app.get("/protected_resource")
async def protected_resource(user_info: dict = Depends(get_current_user)):
    current_user = user_info["username"]
    access_level = user_info["access_level"]
    permissions = user_info["permissions"]

    return {"message": f"Hello, {current_user}! "
                       f"Your role is: {access_level}. "
                       f"Your permissions are: {', '.join(permissions)}."
            }


@app.get('/header_info')
async def header_info(request: Request):
    try:
        user_agent = request.headers.get("user-agent")
        accept_language = request.headers.get("accept-language")
        if user_agent is None:
            raise HTTPException(status_code=400, detail="Missing required headers")
        response_data = {
            "User-Agent": user_agent,
            "Accept-Language": accept_language
        }
    except Exception as e:
        exception_message = str(e)
        response_data = {
            "message": exception_message
        }
    return response_data


if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)
