from collections import Counter
from yikyak import yikyak
import json

auth = json.loads(open('sim.json').read())
client = yikyak.YikYak();
client.login_id(auth['country'], auth['phone'], auth['id'])
