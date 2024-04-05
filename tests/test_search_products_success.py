import pytest
from src.controllers.product_manager import ProductManager


@pytest.mark.asyncio
async def test_search_products_success(keyword="phone", category="Electronics", limit=5):
    mock_products = {
        1: {"product_id": 101, "name": "Keyboard", "category": "Electronics", "price": 112.99},
        2: {"product_id": 102, "name": "Phone case", "category": "Electronics", "price": 19.99},
        3: {"product_id": 103, "name": "Iphone data cable", "category": "Accessories", "price": 19.99},
        4: {"product_id": 104, "name": "Mobile phone", "category": "Electronics", "price": 999.99},
        5: {"product_id": 105, "name": "Smartwatch", "category": "Electronics", "price": 19.99}
    }

    product_manager = ProductManager(product_id=None,
                                     products=mock_products,
                                     keyword=keyword,
                                     category=category,
                                     limit=limit)
    result = await product_manager.search_products()
    expected_result = [
        {"product_id": 102, "name": "Phone case", "category": "Electronics", "price": 19.99},
        {"product_id": 104, "name": "Mobile phone", "category": "Electronics", "price": 999.99}
    ]
    assert result == expected_result
