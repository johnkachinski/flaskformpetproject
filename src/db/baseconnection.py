from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import sessionmaker
from src.db.dbconfig import setting
from src.db.dbmodels import Base, Person

engine = create_engine(
    url = setting.url,
    echo = True
)
try:
    with engine.connect() as conn:
        result = conn.execute(text('SELECT VERSION()'))
        print(result.all())
except OperationalError as error:
    print(f'Ошибка подключения к БД: {error}')
session = sessionmaker(engine)