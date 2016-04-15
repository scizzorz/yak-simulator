import db
import json

from yikyak import yikyak

with open('config.json') as fd:
  config = json.loads(fd.read())

client = yikyak.YikYak();
client.login_id(config['country'], config['phone'], config['id'])

engine = db.create_engine(config['db'])
session = db.create_session(engine)
