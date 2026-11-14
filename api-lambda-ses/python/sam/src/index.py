import os

import boto3
from botocore.exceptions import ClientError

# Both addresses must be verified identities in Amazon SES while the account is in the SES sandbox.
SENDER = os.environ['SENDER']
RECIPIENT = os.environ['RECIPIENT']

SUBJECT = "Amazon SES Test (SDK for Python)"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto3).")

# The HTML body of the email.
BODY_HTML = """<html>
<head></head>
<body>
  <h1>Amazon SES Test (SDK for Python)</h1>
  <p>This email was sent with
    <a href='https://aws.amazon.com/ses/'>Amazon SES</a> using the
    <a href='https://aws.amazon.com/sdk-for-python/'>AWS SDK for Python (Boto3)</a>.</p>
</body>
</html>"""

CHARSET = "UTF-8"

# The client uses the function's own Region.
client = boto3.client('ses')


def handler(event, context):
    try:
        response = client.send_email(
            Destination={'ToAddresses': [RECIPIENT]},
            Message={
                'Body': {
                    'Html': {'Charset': CHARSET, 'Data': BODY_HTML},
                    'Text': {'Charset': CHARSET, 'Data': BODY_TEXT},
                },
                'Subject': {'Charset': CHARSET, 'Data': SUBJECT},
            },
            Source=SENDER,
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        return {'statusCode': 500, 'body': "Email not sent: " + e.response['Error']['Code']}

    print("Email sent! Message ID: " + response['MessageId'])
    return {'statusCode': 200, 'body': "Email sent! Message ID: " + response['MessageId']}
