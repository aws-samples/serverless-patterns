import sys
from awsglue.utils import getResolvedOptions
import time

args = getResolvedOptions(sys.argv, ['message'])
message =args['message']
print('Test Message from the Python script - {}'.format(message))