import sqlalchemy
from sqlalchemy import create_engine, Engine, Connection
from sqlalchemy.orm import sessionmaker, Session

from lesson_22.sql_achemy.user_model import User


# db_url example postgresql://localhost:5432/aqa_python_db

class SqlAlchemyClient:
    __engine: Engine
    __session: Session

    def __init__(self, db_url: str, autocommit=False) -> None:
        self.__engine = create_engine(db_url, autocommit=autocommit)

        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def add_value(self, table_object):
        self.__session.add(table_object)
        self.__session.commit()

    def update_value(self):
        user = self.__session.query(User).filter(name='Maxim').first()
        user.age = 30
        self.__session.commit()

    def delete_value(self, user: User):
        self.__session.delete(user)
        self.__session.commit()

    def close_all_connections(self):
        self.__session.close()

