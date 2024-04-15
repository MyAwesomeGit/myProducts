from typing import Optional, Dict, Any
from fastapi import HTTPException


class ProductManager:
    def __init__(self, products: Optional[Dict[int, Dict[str, Any]]] = None,
                 product_id: Optional[int] = None,
                 keyword: Optional[str] = None,
                 category: Optional[str] = None,
                 limit: Optional[int] = None):
        self.products = products
        self.product_id = product_id
        self.keyword = keyword
        self.category = category
        self.limit = limit

    async def add_product(self):
        pass

    async def get_product(self):
        if not self.product_id:
            raise HTTPException(status_code=404, detail="Product not found")
        self.product_info = self.products.get(self.product_id)
        return self.product_info

    async def search_products(self):
        try:
            self.filtered_products = [product for product in self.products.values() if
                                      self.keyword.lower() in product["name"].lower()]
            if self.category:
                self.filtered_products = [product for product in self.filtered_products if
                                          product["category"].lower() == self.category.lower()]
        except Exception as e:
            raise HTTPException(status_code=400, detail=f"An error occurred while searching products: {str(e)}")
        else:
            return self.filtered_products[:self.limit]
