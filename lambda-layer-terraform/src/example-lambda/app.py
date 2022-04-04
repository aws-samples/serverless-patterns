from mysql import connector
from mysql.connector import Error
from os import listdir
from os import path, walk

def lambda_handler(event, context):
  '''lists the files in the /opt directory

  Lambda extracts the layer contents into the /opt directory when
  setting up the execution environment for the function. Reference:
  https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html

  Returns
  -------
  list
    a list of files in the /opt directory
  '''
  target_dir = "/opt"
  target_dir_files = []
  for (dirpath, _, filenames) in walk(target_dir):
    target_dir_files += [path.join(dirpath, file) for file in filenames]
  return target_dir_files