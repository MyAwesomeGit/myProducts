from typing import Optional, Dict, Any
from fastapi import HTTPException


class ProductManager:
    def __init__(self, products: Optional[Dict[int, Dict[str, Any]]] = None,
                 product_id: Optional[int] = None):
        self.products = products
        self.product_id = product_id

    def __init_(self):
        pass

    async def add_product(self):
        pass

    async def get_product(self):
        if not self.product_id:
            raise HTTPException(status_code=404, detail="Product not found")
        self.product_info = self.products.get(self.product_id)
        return self.product_info

    async def search_products(self):
        pass
