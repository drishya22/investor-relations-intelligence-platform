# modern SQLAlchemly. Every model will inherit from Base and SQLAlchemy will know which tables belong to application
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from app.models.company import Company
from app.models.document import Document