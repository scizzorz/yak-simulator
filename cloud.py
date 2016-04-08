import re
from collections import Counter

chars = re.compile('[^a-z0-9]')

words = open('yaks.txt').read().split()
uniq = Counter()

for word in words:
  uniq[chars.sub('', word)] += 1

for word, count in sorted(uniq.items(), key=lambda x: x[1]):
  print(word, count)

print('UNIQ', len(uniq))
print('TOTAL', sum(uniq.values()))
