from collections import Counter
from yikyak import yikyak
import json
import re
import time

chars = re.compile('[^a-z0-9]')
uniq = Counter()

auth = json.loads(open('auth.json').read())
pin = input('PIN? ')

client = yikyak.YikYak();
client.login(auth['country'], auth['phone'], pin)

all_yaks = {}

def get_new_yaks():
  yaks = client.get_new_yaks(auth['lat'], auth['long'])
  for yak in yaks:
    if yak.message_id not in all_yaks:
      print(yak.message)
      all_yaks[yak.message_id] = yak
      for word in yak.message.split():
        uniq[chars.sub('', word)] += 1

  with open('yaks.txt', 'w') as output:
    for yid, yak in all_yaks.items():
      output.write(yak.message.lower() + '\n')


while True:
  get_new_yaks()
  print('TOTAL YAKS:', len(all_yaks))
  print('TOTAL UNIQUE WORDS:', len(uniq))
  print('TOTAL WORDS:', sum(uniq.values()))

  client.refresh_token()
  time.sleep(300);
