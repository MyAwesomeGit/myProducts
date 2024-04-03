import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/product/{product_id}")
async def get_product():
    pass


@app.get("/products_search")
async def products_search():
    pass


if __name__ == "__main__":
    uvicorn.run(app,
                host='127.0.0.1',
                port=8080)







