from sqlalchemy import Integer, Column
from ..models.main_model import MY_MAIN_MODEL
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from ..models.user_model import User
from ..models.product_model import Product


class Cart(MY_MAIN_MODEL):
    __tablename__ = "cart"

    user_id = Column(Integer, ForeignKey('user_info.id'))
    product_id = Column(Integer, ForeignKey('product.id'))
    user_ = relationship("User", back_populates="cart")
    product = relationship("Product", back_populates="cart")

    User.cart = relationship("Cart", back_populates="user")
    Product.cart = relationship("Cart", back_populates="product")
