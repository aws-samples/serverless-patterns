import boto3, json, os

s3 = boto3.client('s3')
sns = boto3.client("sns")


def lambda_handler(event, context):
    topic_arn = os.environ['topic_arn']
    detail = event['detail']
    checkitemdetail = detail['check-item-detail']
    bucketname = checkitemdetail['Bucket Name']
    if checkitemdetail['ACL Allows List'] != 'No' or checkitemdetail['ACL Allows Upload/Delete'] != 'No':
        reset_bucket_acl(bucketname)
        msg = 'Removed Public access from bucket ACL for bucket: ' + bucketname
        print(msg)
        nofify_by_email(topic_arn,msg)
    if checkitemdetail['Policy Allows Access'] != 'No':
        original_bucket_policy = remove_bucket_policy(bucketname)
        msg = 'Removed S3 Bucket Policy for bucket: ' + bucketname
        print(msg)
        nofify_by_email(topic_arn,msg,original_bucket_policy)

    return {
        'statusCode': 200,
        'body': json.dumps('Bucket" ' + bucketname + ' has been set to private')
    }


def remove_bucket_policy(bucketname):
    result = s3.get_bucket_policy(Bucket=bucketname)
    original_bucket_policy = result['Policy']
    s3.delete_bucket_policy(Bucket=bucketname)
    print('Removed Bucket Policy: ' + original_bucket_policy)
    return original_bucket_policy


def reset_bucket_acl(bucketname):
    s3.put_bucket_acl(Bucket=bucketname, ACL='private')
    msg = 'Removed Public ACL on Bucket: ' + bucketname
    print(msg)

def nofify_by_email(topic_arn,msg,original_bucket_policy):
    subject = "Trusted Advisor Automation: "+msg
    if original_bucket_policy is not None:
        msg = msg + "\n\r\n\rOriginal Bucket Policy:\n\r"+original_bucket_policy
    sns.publish(TopicArn=topic_arn,
                Message=msg,
                Subject=subject)
