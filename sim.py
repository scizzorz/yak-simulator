from yikyak import yikyak
import json

auth = json.loads(open('config.json').read())
client = yikyak.YikYak();
client.login_id(auth['country'], auth['phone'], auth['id'])
