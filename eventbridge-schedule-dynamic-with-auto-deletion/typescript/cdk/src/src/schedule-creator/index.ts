import { SchedulerClient, CreateScheduleCommand, FlexibleTimeWindowMode, ActionAfterCompletion } from '@aws-sdk/client-scheduler';
import addMinutes from 'date-fns/addMinutes';
import addDays from 'date-fns/addDays';
import addMonths from 'date-fns/addMonths';

const client = new SchedulerClient({});

const createSchedule = ({ name, payload, description, time }: any) => {
  return client.send(
    new CreateScheduleCommand({
      Name: name,
      GroupName: process.env.SCHEDULE_GROUP_NAME,
      Target: {
        RoleArn: process.env.SCHEDULE_ROLE_ARN,
        Arn: process.env.EMAIL_SERVICE_ARN,
        Input: JSON.stringify({ ...payload }),
      },
      ActionAfterCompletion: ActionAfterCompletion.DELETE,
      FlexibleTimeWindow: {
        Mode: FlexibleTimeWindowMode.OFF,
      },
      Description: description,
      ScheduleExpression: time,
    })
  );
};

// Function that listens for new users, and schedules emails for them
export async function handler(event: any) {
  const userId = event.detail.userId;

  // Schedule for welcome email 2 minutes after sign up
  await createSchedule({
    name: `${userId}-24hr-after-signup`,
    description: `Welcome email for user:${userId}`,
    payload: { ...event.detail, context: '24hr' },
    time: `at(${addMinutes(new Date(), 2).toISOString().split('.')[0]})`,
  });

  // Schedule for 1 week after sign up
  await createSchedule({
    name: `${userId}-1wk-after-signup`,
    description: `Email 1 week after signup for user:${userId}`,
    payload: { ...event.detail, context: '1wk' },
    time: `at(${addDays(new Date(), 1).toISOString().split('.')[0]})`,
  });

  // Schedule for 1 month after sign up
  await createSchedule({
    name: `${userId}-1month-after-signup`,
    description: `Email 1 month after signup for user:${userId}`,
    payload: { ...event.detail, context: '1month' },
    time: `at(${addMonths(new Date(), 1).toISOString().split('.')[0]})`,
  });
}
