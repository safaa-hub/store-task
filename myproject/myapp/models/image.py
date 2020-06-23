from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from .product_model import Product
from sqlalchemy import ForeignKey
from ..models.main_model import MY_MAIN_MODEL


class Image(MY_MAIN_MODEL):

    __tablename__ = 'image'

    uid = Column(Integer)
    uuid = Column(Integer)
    path = Column(String)
    product_id = Column(Integer, ForeignKey('product.id'))
    # product = relationship("Product", back_populates="image")

    # Product.image = relationship("ProductImage", back_populates="product")
