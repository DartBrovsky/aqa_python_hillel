from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Department(Base):
    __tablename__ = "department"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    users = relationship("users", back_populates="department")
