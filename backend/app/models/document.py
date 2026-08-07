from datetime import datetime
from sqlalchemy import DateTime,ForeignKey,Integer,String
from sqlalchemy.orm import Mapped,mapped_column,relationship

from app.database.base import Base

class Document(Base):
    __tablename__="documents"
    id: Mapped[int]=mapped_column(Integer,primary_key=True,index=True)
    company_id:Mapped[int]=mapped_column(ForeignKey("companies.id"))
    title: Mapped[str]=mapped_column(String(500),nullable=False)
    report_type: Mapped[str]=mapped_column(String(500))
    year: Mapped[int]=mapped_column()
    pdf_url: Mapped[str]=mapped_column(String(1000))
    local_path: Mapped[str]=mapped_column(String(500))
    pages:Mapped[int]=mapped_column(default=0)
    file_size:Mapped[int]=mapped_column(default=0)
    created_at:Mapped[datetime]=mapped_column(DateTime,default=datetime.utcnow)
    company=relationship("Company",back_populates="documents")

