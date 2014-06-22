import sqlalchemy
from sqlalchemy import orm
from sqlalchemy.ext import declarative


Base = declarative.declarative_base()


def init(path):
    engine = sqlalchemy.create_engine(path, convert_unicode=True)
    db_session = orm.scoped_session(orm.sessionmaker(autocommit=False, autoflush=False, bind=engine))
    Base.query = db_session.query_property()
    return db_session

def init_db():
    from compliment import Compliment
    Base.metadata.create_all(bind=engine)
