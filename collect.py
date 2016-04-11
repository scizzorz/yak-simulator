from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from yikyak.yikyak import YikYak
import json
import time

with open('config.json') as fd:
  config = json.loads(fd.read())

client = YikYak()
client.login_id(config['country'], config['phone'], config['id'])

engine = create_engine(config['db'])
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

    return '<Yak {} {}{}>'.format(self.score,handle, self.text)

Session = sessionmaker(bind=engine)

session = Session()

def get_new_yaks():
  yaks = client.get_new_yaks(config['lat'], config['long'])
  for yak in yaks:
    cur_yak = session.query(Yak).filter_by(yid=yak.message_id).first()
    if not cur_yak:
      cur_yak = Yak(yid=yak.message_id, time=yak.time, text=yak.message, score=yak.number_of_likes, handle=yak.nickname or '')
      print('NEW:', repr(cur_yak))
      session.add(cur_yak)
    else:
      if cur_yak.score != yak.number_of_likes:
        cur_yak.score = yak.number_of_likes
        print('MOD:', repr(cur_yak))

  session.commit()

while True:
  get_new_yaks()
  client.refresh_token()
  time.sleep(300);
