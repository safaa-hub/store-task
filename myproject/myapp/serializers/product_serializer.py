from ..models.product_model import Product
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


class ProductSerializer(SQLAlchemySchema):
    class Meta:
        Model = Product
        load_instance = True

    id = auto_field(column_name="id", model=Product)
    name = auto_field(column_name="name", model=Product)
    price = auto_field(column_name="price", model=Product)
    quantity = auto_field(column_name="quantity", model=Product)
    status = auto_field(column_name="status", model=Product)
    detail = auto_field(column_name="detail", model=Product)
