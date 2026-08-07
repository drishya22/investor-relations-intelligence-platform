from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base

class Company(Base):
    __tablename__="companies"

    id: Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    name: Mapped[str]=mapped_column(String(100),unique=True,nullable=False)
    ticker: Mapped[str]=mapped_column(String(20),unique=True,nullable=False,index=True)
    ir_url: Mapped[str]=mapped_column(String(500),nullable=False) #investor relations page
    created_at: Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    documents=relationship("Document",back_populates="company",cascade="all, delete-orphan")