from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base


class Main(object):
    id = Column(Integer, primary_key=True)
    created = Column(DateTime)
    updated = Column(DateTime)


MY_MAIN_MODEL = declarative_base(cls=Main)
