from base import client
from base import config

def compose(msg):
  return client.compose_yak(msg, config['lat'], config['long'], handle=True)
