from sqlalchemy import Integer, String, Column, Float
from ..models.main_model import MY_MAIN_MODEL
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Product(MY_MAIN_MODEL):

    __tablename__ = 'product'

    name = Column(String)
    price = Column(Float)
    quantity = Column(Float)
    status = Column(String)
    detail = Column(String)
    image = Column(String)
    user_id = Column(Integer, ForeignKey('user_info.id'))

    user = relationship("User", back_populates="product")

    def __repr__(self):
        return "<Product(name = '%s', status = '%s')>" % (self.name, self.status)
