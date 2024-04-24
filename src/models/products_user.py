from pydantic import BaseModel


class ProductsUser(BaseModel):
    username: str
    password: str
    access_level: str
