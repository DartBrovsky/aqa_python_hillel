from pony.orm import Database


class PonyOfDbClient:

    __db: Database

    def __init__(self, provider: str, name: str, password: str, host: str, database: str):
        self.__db = Database(provider=provider, name=name, password=password, host=host, database=database)

    @property
    def db(self) -> Database:
        return self.__db

