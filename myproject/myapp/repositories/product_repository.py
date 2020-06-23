from ..common_file import Session
from ..models.product_model import Product
from ..serializers.product_serializer import ProductSerializer


class ProductRepository:
    def add_product(self, name, price, quantity, status, detail, user_id):
        product = Product(name=name, price=price, quantity=quantity, status=status, detail=detail, user_id=user_id)
        Session.add(product)
        Session.commit()
        Session.close()

    def get_product(self, id):
        product_serializer = ProductSerializer()
        product = Session.query(Product).filter_by(id=id).all()
        if len(product) > 0:
            dump_data = product_serializer.dump(product[0])
            return dump_data
        else:
            return None

    def get_all_products(self):
        products = Session.query(Product).all()
        product_serializer = ProductSerializer()
        if len(products) > 0:
            dump_data = product_serializer.dump(products, many=True)
            return dump_data

    def update_product(self, id, name, price, quantity, status, detail):
        product = Session.query(Product).filter_by(id=id).one()
        product.name = name
        product.price = price
        product.quantity = quantity
        product.status = status
        product.detail = detail
        Session.commit()
