from ..common_file import Session
from ..models.product_model import Product


class ProductRepository:
    def add_product(self, name, price, quantity, status_, detail):
        product = Product(name=name, price=price, quantity=quantity, status=status_, detail=detail)
        Session.add(product)
        Session.commit()
        Session.close()
