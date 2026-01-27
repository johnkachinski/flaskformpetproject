from sqlalchemy.exc import IntegrityError
from psycopg2 import errors

from src.db.baseconnection import session

def adding_person(person):
    try:
        with session() as sess:
            sess.add(person)
            sess.commit()
            return 200
    except IntegrityError as error:
        if isinstance(error.orig,errors.UniqueViolation):
            return error



