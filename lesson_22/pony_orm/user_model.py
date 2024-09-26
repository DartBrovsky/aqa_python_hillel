from pony.orm import Required, Set

from lesson_22.pony_orm.pony_client import PonyOfDbClient

db = PonyOfDbClient("postgresql", "admin", "password", "127.0.0.1:5432", "aqa_db").db


class User(db.Entity):
    name = Required(str)
    department = Required('Department')


class Department(db.Entity):
    name = Required(str)
    users = Set('User')
