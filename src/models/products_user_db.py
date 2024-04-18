from models.products_user import ProductsUser


class ProductsUserDB:
    database = [
        ProductsUser(username="test", password="123", access_permission="administrator"),
        ProductsUser(username="hello", password="111", access_permission="guest"),
        ProductsUser(username="iamuser", password="012", access_permission="user")
    ]
