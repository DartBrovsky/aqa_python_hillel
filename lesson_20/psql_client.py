from typing import Any

import psycopg2
from psycopg2._psycopg import connection, cursor


class PSQLClient:
    __connection: connection
    __cursor: cursor

    def __init__(self, dbname: str, user: str, password: str, host: str, port: int):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.__init_connection(self.dbname, self.user, self.password, self.host, self.port)

        self.__cursor = self.__connection.cursor()

    def __del__(self):
        self.__cursor.close()
        self.__connection.close()

    def __init_connection(self, dbname: str, user: str, password: str, host: str, port: int) -> None:
        try:
            self.__connection = psycopg2.connect(
                dbname=dbname, user=user, password=password, host=host, port=port
            )
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

    @property
    def cursor(self) -> cursor:
        return self.__cursor

    @property
    def connection(self) -> connection:
        return self.__connection

    def get_data_from_db(self, query: str) -> list[Any]:
        self.__cursor.execute(query)

        return self.__cursor.fetchall()

    def close_connection(self):
        self.__cursor.close()
        self.__connection.close()
