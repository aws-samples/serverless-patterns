import boto3
import os
from changeAlarmToLocalTimeZone import *

#Get SNS Topic ARN from Environment variables
NotificationSNSTopic = os.environ['NotificationSNSTopic']

#Get timezone corresponding to your localTimezone from Environment variables 
timezoneCode = os.environ['TimeZoneCode']

#Get Your local timezone Initials, E.g UTC+2, IST, AEST...etc from Environment variables 
localTimezoneInitial=os.environ['TimezoneInitial']

#Get SNS resource using boto3
SNS = boto3.resource('sns')

#Specify the SNS topic to push message to by ARN
platform_endpoint = SNS.PlatformEndpoint(NotificationSNSTopic)

def lambda_handler(event, context):
    #Call Main function
    changeAlarmToLocalTimeZone(event,timezoneCode,localTimezoneInitial,platform_endpoint)
    
    #Print All Available timezones
    #getAllAvailableTimezones()
               
    #search if Timezone/Country exist
    #searchAvailableTimezones('sy')