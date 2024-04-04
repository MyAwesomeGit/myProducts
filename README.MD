# myProducts

* Python
* FastAPI
* pytest

This project is a simple FastAPI application designed to serve as a foundation for building a product management API. It utilises Uvicorn to run the application, showcasing the integration of FastAPI with Uvicorn for efficient web application deployment.

The application is structured around several endpoints:
1. Product retrieval by ID:
```bash
/get_product/{product_id}
```
Endpoint allows users to retrieve product details by providing a specific product ID. This endpoint is designed to be asynchronous, leveraging FastAPI's capabilities to handle concurrent requests.

2. Products search:
```bash
/search_products
```
Endpoint is intended for searching products based on certain criteria. This endpoint is also asynchronous, enabling the application to handle multiple search requests simultaneously.

The application is configured to run on the local machine (127.0.0.1) at port 8080, making it accessible for local development and testing.

This project serves as a starting point and demonstrates the basic setup required to create a FastAPI application, including defining routes, handling requests asynchronously, and running the application with Uvicorn.


## Getting Started
These instructions will help you set up the project on your local machine for development and testing purposes.

## Cloning the Repository
Clone the repository by running the following command:
```bash
git clone https://github.com/MyAwesomeGit/myProducts.git
```

## Setting Up a Virtual Environment
Create a virtual environment for this project to manage dependencies. Here's how to do it:
1. Navigate to the project directory in your terminal:
```bash
cd ~/Documents
```
2. Create a virtual environment named env using the following command:

```bash
python -m venv env
```

## Installing packages
You can install packages using [pip](https://pip.pypa.io/en/stable/):
```bash
pip install -r requirements.txt
```

## Authors
* <https://github.com/MyAwesomeGit>
* <https://www.phind.com/>

