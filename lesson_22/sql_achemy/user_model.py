from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)

    department_id = Column(Integer, ForeignKey('departments.id'))

    department = relationship("department", back_populates="users")


desired_user: User = User(name="Maxim", age=50)

