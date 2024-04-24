from models.products_user import ProductsUser


class ProductsUserDB:
    database = [
        ProductsUser(username="test", password="123", access_level="administrator"),
        ProductsUser(username="hello", password="111", access_level="guest"),
        ProductsUser(username="iamuser", password="012", access_level="user")
    ]
