import sys
from twython import Twython
CONSUMER_KEY = 'consumerkeyhere'
CONSUMER_SECRET = 'consumersecrethere'
ACCESS_KEY = 'accesskeyhere'
ACCESS_SECRET = 'acesssecrethere'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)

api.update_status(status=sys.argv[1])
