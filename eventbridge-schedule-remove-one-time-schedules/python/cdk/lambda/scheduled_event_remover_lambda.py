import json
import logging
import boto3
import os



import datetime
from dateutil import parser

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.info('Loading function')
sns=boto3.client('sns')
def lambda_handler(event, context):
    mysnstopicarn=os.environ['TOPIC_ARN']
    print(mysnstopicarn)

    scheduler=boto3.client('scheduler')
    response = scheduler.list_schedules()
    for schedule in response['Schedules']:
        print(schedule)
        print(schedule['Name'])    
        if "myscheduleonetime" in schedule['Name']:
            print("###############################scheduler###############################")
            print(scheduler.get_schedule(Name=schedule['Name']))
            scheduleinfo=json.loads(json.dumps(scheduler.get_schedule(Name=schedule['Name']),indent=2, sort_keys=True, default=str))
            print(scheduleinfo['ScheduleExpression'])
            scheduleinfostr=json.dumps(scheduleinfo['ScheduleExpression'])
            print(scheduleinfostr)
            if "at" in scheduleinfostr:
                scheduleinfostr=scheduleinfostr[4:23]
                print(scheduleinfostr)
                date1 = parser.parse(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S"))
                date2 = parser.parse(scheduleinfostr)
                diff = date1 - date2
                print(diff)
                print(diff.days)
                if diff.days > 7:           
                     print("schedule is past the scheduled date by 7 seven days and criteria fullfilled to delete")
                     scheduler.delete_schedule(Name=schedule['Name'])
                     sns.publish(TopicArn=mysnstopicarn,Message="scheduler event is deleted")

    return {
         'statusCode': 200,
         'body': json.dumps('Completed Eventbridge Schedules with past date removed successfully using Lambda!')
    }
    
    

