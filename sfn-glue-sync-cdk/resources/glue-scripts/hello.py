import sys
from awsglue.utils import getResolvedOptions
import time

args = getResolvedOptions(sys.argv,
                          ['message'])
message =args['message']
time.sleep(60)
print('python-shell glue job message - {}'.format(message))

