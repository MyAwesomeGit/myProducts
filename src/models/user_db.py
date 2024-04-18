from models.products_user import ProductsUser


products_user_db = [
    ProductsUser(username="test", password="123", access_permission="administrator"),
    ProductsUser(username="hello", password="111", access_permission="guest"),
    ProductsUser(username="iamuser", password="012", access_permission="user")
]
