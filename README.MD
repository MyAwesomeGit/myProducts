# myProducts

* Python
* FastAPI
* Pytest

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


3. Authorization:
```bash
/authorization
```
This endpoint uses HTTP Basic Authentication to securely authenticate users and generate JWT tokens for authorized access to protected resources.

Upon successful authentication, the endpoint returns a JSON object containing the JWT access token and the user's access level.

If the credentials are invalid, the endpoint returns a 401 Unauthorized status code with a message indicating the error.

4. Protected resource:
```bash
/protected_resource
```
This endpoint is a protected resource that requires a valid JWT token to access. The endpoint checks the user's access level and permissions to ensure they have the necessary permissions to access the resource.

It returns a personalized message to the authenticated user, including their username, access level, and permissions.



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

## Testing with Pytest
This project includes tests for both successful and failed scenarios for the get_product and search_products endpoints.
The test case uses mock data to simulate a set of products. 


```bash
pytest -v tests
```


The ProductManager class is responsible for managing product data, including fetching product details based on a given product ID and searching for products based on the provided keyword, category and limit.
This functionality is tested using pytest and pytest-asyncio, which allows for the testing of asynchronous code in Python.

The **test_get_product_success** function is an asynchronous test case that verifies the ProductManager can successfully retrieve a product by its ID.


The **test_get_product_fail** verifies the behavior of the ProductManager when attempting to retrieve a product that does not exist in the provided product data.


The **test_search_products_success** function is an asynchronous test case that checks if the ProductManager class can successfully search for products based on the provided keyword, category, and limit.


The **test_search_products_fail** function is an asynchronous test case that verifies the behavior of the ProductManager class when attempting to search for products that do not match the specified criteria. It uses the pytest framework with the pytest-asyncio plugin to facilitate testing of asynchronous code.


## Authors
* <https://github.com/MyAwesomeGit>
* <https://www.phind.com/>

