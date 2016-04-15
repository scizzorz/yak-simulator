import db
import time

from base import client
from base import config
from base import session

def get_new_yaks():
  yaks = client.get_new_yaks(config['lat'], config['long'])
  for yak in yaks:
    cur_yak = session.query(db.Yak).filter_by(yid=yak.message_id).first()
    if not cur_yak:
      cur_yak = db.Yak(yid=yak.message_id, time=yak.time, text=yak.message, score=yak.number_of_likes, handle=yak.nickname or '')
      print(' NEW:', repr(cur_yak))
      session.add(cur_yak)
    else:
      if cur_yak.score != yak.number_of_likes:
        diff = yak.number_of_likes - cur_yak.score
        cur_yak.score = yak.number_of_likes
        print('{: =+4}:'.format(diff), repr(cur_yak))

  session.commit()

while True:
  get_new_yaks()
  client.refresh_token()
  time.sleep(300);
