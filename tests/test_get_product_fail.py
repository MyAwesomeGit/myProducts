import pytest
from controllers.product_manager import ProductManager

products = {2: {"product_id": 123, "name": "Keyboard Keychron Q1", "category": "Electronics", "price": 112.99}}


@pytest.mark.asyncio
async def test_get_product_fail():
    product_id = 99
    product_manager = ProductManager(product_id=product_id,
                                     products=products,
                                     keyword=None,
                                     category=None,
                                     limit=None)
    result = await product_manager.get_product()
    assert result is None
