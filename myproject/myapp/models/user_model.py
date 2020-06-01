from sqlalchemy import Column, String
from ..models.main_model import MY_MAIN_MODEL


class User(MY_MAIN_MODEL):
    __tablename__ = 'user_info'

    name = Column(String)
    email = Column(String)
    password = Column(String)
    type = Column(String)

    def __repr__(self):
        return "<User(name = '%s', type = '%s')>" % (self.name, self.type)
