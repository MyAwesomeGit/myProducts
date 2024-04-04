import uvicorn
from fastapi import FastAPI
from controllers.product_manager import ProductManager
from models.products import products

app = FastAPI()


@app.get("/product/{product_id}")
async def get_product(product_id: int):
    product_manager = ProductManager(product_id=product_id,
                                     products=products)
    return await product_manager.get_product()


@app.get("/products_search")
async def products_search():
    pass


if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)
