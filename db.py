from flask_sqlalchemy import SQLAlchemy
from config import Config

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

db = SQLAlchemy()


def create_db_session():
    engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
    return Session(engine)


def db_used(func):
    def wrapper(*args):
        session = create_db_session()
        try:
            result = func(*args, session=session)
            session.commit()
        finally:
            session.close()
        return result

    return wrapper
