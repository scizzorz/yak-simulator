import db
import re

from base import session
from collections import Counter

chars = re.compile('[^a-z0-9]')

uniq = Counter()
yaks = session.query(db.Yak).all()

for yak in yaks:
  words = yak.text.split()
  for word in words:
    uniq[chars.sub('', word.lower())] += 1

for word, count in sorted(uniq.items(), key=lambda x: x[1]):
  print(word, count)

print('UNIQ', len(uniq))
print('TOTAL', sum(uniq.values()))
