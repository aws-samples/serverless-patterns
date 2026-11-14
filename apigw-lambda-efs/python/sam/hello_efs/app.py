import os
import fcntl
import json 


# You can reference EFS files by including your local mount path, and then
# treat them like any other file. Local invokes may not work with this, however,
# as the file/folders may not be present in the container.


MSG_FILE_PATH = '/mnt/msg/content'

def get_messages():
    try:
        with open(MSG_FILE_PATH, 'r') as msg_file:
            fcntl.flock(msg_file, fcntl.LOCK_SH)
            messages = msg_file.read()
            fcntl.flock(msg_file, fcntl.LOCK_UN)
    except:
        messages = None
        
    return messages

def add_message(new_message):
    with open(MSG_FILE_PATH, 'a') as msg_file:
        fcntl.flock(msg_file, fcntl.LOCK_EX)
        msg_file.write(new_message + "\n")
        fcntl.flock(msg_file, fcntl.LOCK_UN)

def delete_messages():
    try:
        os.remove(MSG_FILE_PATH)
    except:
        pass

def lambda_handler(event, context):
    
    # The files in EFS are not only persistent across executions, but if multiple
    # Lambda functions are mounted to the same EFS file system, you can read and
    # write files from either function.
    
    method = event['requestContext']['http']['method']
    delete_flag = False
    
    if method == 'GET':
        messages = get_messages()
    elif method == 'POST':
        new_message = event['body']
        add_message(new_message)
        messages = get_messages()
    elif method == 'DELETE':
        delete_messages()
        delete_flag = True
        messages = 'Messages deleted.\n'
    else:
        messages = 'Method unsupported.\n'

    return messages