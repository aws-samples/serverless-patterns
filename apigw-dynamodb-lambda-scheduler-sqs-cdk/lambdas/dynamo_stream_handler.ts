import {
  AttributeValue
} from "@aws-sdk/client-dynamodb";
import * as AWS from "@aws-sdk/client-scheduler";
import { unmarshall } from "@aws-sdk/util-dynamodb";
import { DynamoDBStreamEvent } from 'aws-lambda';
import { randomUUID } from "crypto";
import { messageBody } from './schemas/input-request-schema';
import { createSchedules } from "./utils/scheduler";


export const handler = async (event: DynamoDBStreamEvent): Promise<any> => {
  console.log(`Event: ${JSON.stringify(event, null, 2)}`);
  const Separator = "-";

  for (const record of event.Records) {
    if (record.dynamodb && record.dynamodb.NewImage) {
      const newImage = unmarshall(
        record.dynamodb.NewImage as { [key: string]: AttributeValue }
      );
      console.debug("New Image: %j", newImage);
      let messageData: messageBody = {
        id: newImage["id"],
        eventName: newImage["eventName"],
        eventType: newImage["eventType"],
        scheduleTime: newImage["scheduleTime"]
      };

      let scheduleWindow = getScheduleWindowInISOStringWithoutMillisecs(messageData.scheduleTime);

      const clientToken = randomUUID();
      const targetType = messageData.eventType || "default";
      const inputJson = {
        ...messageData,
        "clientToken": clientToken
      }
      const queueTarget: AWS.Target = {
        RoleArn: process.env.QUEUE_TARGET_ROLE_ARN!,
        Arn: process.env.QUEUE_TARGET_ARN!,
        RetryPolicy: {
          MaximumEventAgeInSeconds: 60,
          MaximumRetryAttempts: 3
        },
        Input: JSON.stringify(inputJson),
      };

      const lambdaTarget: AWS.Target = {
        RoleArn: process.env.LAMBDA_TARGET_ROLE_ARN!,
        Arn: process.env.LAMBDA_TARGET_ARN!,
        RetryPolicy: {
          MaximumEventAgeInSeconds: 60,
          MaximumRetryAttempts: 3
        },
        Input: JSON.stringify(inputJson),
      };

      const schedulerInput: any = {
        Name: messageData.eventName + Separator + messageData.id,
        FlexibleTimeWindow: {
          Mode: "OFF",
        },
        Target: (targetType==="Lambda")?lambdaTarget:queueTarget,
        ScheduleExpression: `at(${scheduleWindow})`,
        GroupName: targetType,
        scheduleExpressionTimezone: 'America/Los_Angeles', //Optional
        ClientToken: clientToken,
      };
      const result = await createSchedules(schedulerInput);

      if (result.$metadata.httpStatusCode == 200) {
        return {
          statusCode: 200,
          body: JSON.stringify({
            statusMessage: result.$metadata,
            message: 'Message Sent!',
          }),
        };
      } else {
        return {
          statusCode: result.$metadata.httpStatusCode || 400,
          body: JSON.stringify({
            statusMessage: result.$metadata,
            statusCode: result.$metadata.httpStatusCode,
          }),
        };
      }
    }
  }
};

function getScheduleWindowInISOStringWithoutMillisecs(epochTime: string) {
  let epochTimeInMiliSeconds = Number(epochTime) * 1000;
  const date = new Date(epochTimeInMiliSeconds);
  return date.toISOString().split('.')[0]
}
