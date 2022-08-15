import os, json, math, time, boto3, pyshorteners
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


def create_multipart_message(
        sender: str, recipients: list, title: str, text: str=None, html: str=None, attachment: str=None , attachment_type: str=None) \
        -> MIMEMultipart:
    """
    Creates a MIME multipart message object.
    Uses only the Python `email` standard library.
    Emails, both sender and recipients, can be just the email string or have the format 'The Name <the_email@host.com>'.

    :param sender: The sender.
    :param recipients: List of recipients. Needs to be a list, even if only one recipient.
    :param title: The title of the email.
    :param text: The text version of the email body (optional).
    :param html: The html version of the email body (optional).
    :param attachment: A file to attach in the email.
    :return: A `MIMEMultipart` to be used to send the email.
    """

    multipart_content_subtype = 'alternative' if text and html else 'mixed'
    msg = MIMEMultipart(multipart_content_subtype)
    msg['Subject'] = title
    msg['From'] = sender
    msg['To'] = ','.join(recipients)

    # Record the MIME types of both parts - text/plain and text/html.
    # According to RFC 2046, the last part of a multipart message, in this case the HTML message, is best and preferred.
    if text:
        part = MIMEText(text, 'plain')
        msg.attach(part)
    if html:
        part = MIMEText(html, 'html')
        msg.attach(part)
    
    if attachment_type == 'file':
        # Add attachments
        with open(attachment, 'rb') as f:
            part = MIMEApplication(f.read())
            part.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment))
            msg.attach(part)

    return msg

def object_size(size_bytes: int) -> bool:
    if size_bytes == 0:
       return "0B"
    size_name = ("B", "KB", "MB", "GB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    print("object size is {} {}".format(s,size_name[i]))
    if i > 2 or (i==2 and s > 25):
        print("object size is above greater than 25 MB with size being %s %s %s" % (s, size_name[i]," Will be using a presigned url instead on file as a attachment"))
        return False
    return True
    
def send_mail(
        sender: str, recipients: list, title: str, text: str=None, html: str=None, attachment: str=None, attachment_type: str=None) -> dict:
            
    """
    Send email to recipients. Sends one mail to all recipients.
    The sender needs to be a verified email in SES.
    """
    ses_client = boto3.client('ses')  # Use your settings here
    msg = create_multipart_message(sender, recipients, title, text, html, attachment, attachment_type)
    print('sending raw email')
    return ses_client.send_raw_email(
        Source=sender,
        Destinations=recipients,
        RawMessage={'Data': msg.as_string()}
    )

def create_presigned_url(bucket_name: str, object_name: str, expiration: int, s3_client: object) -> str:
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
                                                
    except ClientError as e:
        print(e)
        return None

    # The response contains the presigned URL
    return response

def shortenUrl(url: str) -> str:
    # Returns the shorten url of the generated pre-signed url
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

def fetchS3File(event: dict, expiration: int) -> str:
    
    """
    Downloads the file which was uploaded to S3 bucket to lambda function /tmp storage if file size is <= 25 MB or else presigned url will be returned.
    Returns the file location once the job completes.
    """
    s3_client = boto3.client("s3")
    payload_size = event['Records'][0]['s3']['object']['size']
    is_paylaod_under_limit = object_size(payload_size)
    bucket     = event['Records'][0]['s3']['bucket']['name'] #bucketname
    object_key = event['Records'][0]['s3']['object']['key']  #filename
    
    print('Bucket is {} and object {}'.format(bucket,object_key))

    tmp_filename = None

    if is_paylaod_under_limit:
        tmp_filename = '/tmp/' + object_key.split('/')[-1]  # fetching the filename
        print(tmp_filename)
        
        #Flush storage
        os.system('rm -rf /tmp/*')
        
        # print('tmp storage has been flushed listing directory /tmp to check if flush is successfull {}'.format(os.listdir('/tmp/')))
        s3_client.download_file(bucket, object_key, tmp_filename)

        print('Downloaded the {} and listing the directory /tmp directory {}'.format(tmp_filename[5:],os.listdir('/tmp/'))) # checking if the file is downloaded 
    else:
        print('Email attachment limit has been exceeded 25B Generating pre-signed url')
        url = create_presigned_url(bucket,object_key,time,s3_client)# setting expiary link to one week which is maximum
        url = shortenUrl(url)
        print('URL created is {} and the time of creation'.format(url,time.time()))

    return url if tmp_filename == None else tmp_filename

def lambda_handler(event,context):
    
    '''
    The logic is to once S3 triggers this function with object payload an email is send to the receivers if the payload size of file is <= 25MB
    If the payload is > 25MB program creates a pre-signed url and shortnes the url when sent to the client.
    '''
    print(event)
    
    unverified_payload = ['386', 'fon', 'ocx', 'ade', 'fxp', 'ops', 'adp', 'hlp', 'ov', 'adt', 'hta',
    'pcd', 'app', 'htr', 'pgm', 'asd', 'inf', 'pif', 'asp', 'ini', 'pl', 'asx', 'inp', 'pm', 'bas', 'ins', 'prg', 
    'bat', 'ispscr', 'bin', 'jar', 'sct', 'btm', 'jse', 'shsb', 'cab', 'keyreg', 'shs?', 'cbl', 'ksh', 'slb', 'cbt',
    'lib', 'smm', 'cgi', 'ink', 'swf', 'com', 'mda', 'swt', 'cil', 'mdb', 'sys', 'class', 'mde', 'vbe', 'cmd', 'mdt',
    'vbs', 'cpe', 'mdw', 'vbx', 'cpl', 'mhtm', 'vir', 'crt', 'mhtml', 'vmx', 'csc', 'msc', 'vxd', 'csh', 'msi', 'wmd', 'css', 
    'msp', 'wms', 'cvp', 'mst', 'wmz', 'dll', 'mp3', 'wsc', 'dot', 'nte', 'wsf', 'drv', 'nws', 'wsh', 'exe', 'obj', 'xms']
    
    key = event['Records'][0]['s3']['object']['key']
    
    if '.' in key and ((key.split('.')[-1]) in unverified_payload):
        print('payload is = '.format(key))
        return {
            'statusCode' : 500,
            'body' : 'unverified_payload cant be sent via email job is terminated'
        }

    sender_ = os.environ['SENDER_EMAIL'] # provide ses MAIL FROM domain reference here

    if (sender_ == None or sender_ == ''):
        print('Please provide sender email address to send the messages the provided sebder value is {}'.format(sender_))
        return
    
    recipients_ = os.environ['RECEIVER_EMAIL'].split(',')  # ex : ["foo@gmail.com","bar@gmail.com"]

    if (len(recipients_) == 0):
        print('Please provide receiver email address to send the email the provided receiver value is {}'.format(recipients_))
        return
    
    expiration_ = 129600 # setting duration for 36 hours
    title_ = 'Sending attechment from S3' # Do your customization here
    text_ = ''
    attachment = fetchS3File(event,expiration_)
    attachment_type = 'file' # Indicates that the attachment is file

    if attachment.startswith('https'):
        attachment_type = 'url' # Indicates that the attachment is url
    
    # For body you can customize the data according to your use-case 
    body_context = """
        <html><head>Dear ,</head>
        <br><br>
        <body>Please find the attached """ + attachment_type

    body_ = body_context + ' ' + attachment[5:] if attachment_type == 'file' else body_context + "<br> <br>" + attachment
    
    print(body_)
    
    try:
        response_ = send_mail(sender_, recipients_, title_, text_, body_, attachment, attachment_type)
        print(response_)
        return{
            "statusCode" : 200,
            "body" : json.dumps(response_)
        }
    except Exception as e:
        print(e)
        return{
            "statusCode" : 500
        }
# This code is provided on best effort basics.
# Kindly note this code is not tested on edge cases these may create issues if you deploy it over production environment.
# Use this code for referene purpose only.