from yikyak.yikyak import YikYak
import db
import json
import time

with open('config.json') as fd:
  config = json.loads(fd.read())

client = YikYak()
client.login_id(config['country'], config['phone'], config['id'])

engine = db.create_engine(config['db'])
session = db.create_session(engine)

def get_new_yaks():
  yaks = client.get_new_yaks(config['lat'], config['long'])
  for yak in yaks:
    cur_yak = session.query(db.Yak).filter_by(yid=yak.message_id).first()
    if not cur_yak:
      cur_yak = db.Yak(yid=yak.message_id, time=yak.time, text=yak.message, score=yak.number_of_likes, handle=yak.nickname or '')
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
