import sqlalchemy

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
class Yak(Base):
  __tablename__ = 'yaks'
  id = Column(Integer, primary_key=True)
  yid = Column(String)
  time = Column(String)
  text = Column(String)
  score = Column(Integer)
  handle = Column(String)

  def __repr__(self):
    handle = self.handle
    if handle:
      handle = '@{}: '.format(handle)
    else:
      handle = ''

    return '<Yak {: >3} {}{}>'.format(self.score,handle, self.text)

def create_engine(db):
  return sqlalchemy.create_engine(db)

def create_session(engine):
  return sessionmaker(bind=engine)()
