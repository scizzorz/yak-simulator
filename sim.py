from yikyak import yikyak
import json

config = json.loads(open('config.json').read())
client = yikyak.YikYak();
client.login_id(config['country'], config['phone'], config['id'])

def compose(msg):
  return client.compose_yak(msg, config['lat'], config['long'], handle=True)
