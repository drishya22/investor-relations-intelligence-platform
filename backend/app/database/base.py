# modern SQLAlchemly. Every model will inherit from Base and SQLAlchemy will know which tables belong to application
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass