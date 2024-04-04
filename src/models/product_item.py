from pydantic import BaseModel


class ProductItem(BaseModel):
    product_id: int
    name: str
    category: str
    price: float
