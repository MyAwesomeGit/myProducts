from typing import Optional

import uvicorn
from fastapi import FastAPI
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


if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)
