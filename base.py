import db
import json

from yikyak import yikyak

with open('config.json') as fd:
  config = json.loads(fd.read())

client = yikyak.YikYak();
if 'id' in config:
  client.login_id(config['country'], config['phone'], config['id'])
else:
  pin = input('PIN? ')
  client.login(config['country'], config['phone'], pin)
  print('Your user ID is:', client.yakker.userID)

engine = db.create_engine(config['db'])
session = db.create_session(engine)
