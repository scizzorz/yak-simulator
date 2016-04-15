import db

from base import session

with open('yaks.txt', 'w') as fd:
  for yak in session.query(db.Yak).filter(db.Yak.score > 0).all():
    fd.write(yak.text + '\n')

