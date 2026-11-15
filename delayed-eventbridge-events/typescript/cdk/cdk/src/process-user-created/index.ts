import { EventBridgeEvent } from 'aws-lambda';
import { SchedulerClient, CreateScheduleCommand, FlexibleTimeWindowMode, CreateScheduleGroupCommand } from '@aws-sdk/client-scheduler';
import addMinutes from 'date-fns/addMinutes';

const client = new SchedulerClient({});
const minutesInTheFuture = parseInt(process.env.TRIGGER_IN_FUTURE_IN_MINUTES || '2');

interface UserCreated {
  id: string;
  firstName: string;
  lastName: string;
}

export async function handler(event: EventBridgeEvent<'UserCreated', UserCreated>) {

  try {
    // Create the schedule group for now, this would be done in CDK when we can
    await client.send(
      new CreateScheduleGroupCommand({
        Name: 'SchedulesForUsers24HoursAfterCreation',
      })
    );
  } catch (error) {}

  try {
    await client.send(
      new CreateScheduleCommand({
        Name: `${event.detail.id}-24hr`,
        GroupName: 'SchedulesForUsers24HoursAfterCreation',
        Target: {
          RoleArn: process.env.SCHEDULE_ROLE_ARN,
          Arn: process.env.EVENTBUS_ARN,
          EventBridgeParameters: {
            DetailType: 'UserCreated24HoursAgo',
            // let's define a bounded context/scope for these types of events
            Source: 'scheduler.notifications',
          },
          // This is the detail of the event
          Input: JSON.stringify({ ...event.detail }),
        },
        FlexibleTimeWindow: {
          Mode: FlexibleTimeWindowMode.OFF,
        },
        Description: `24 hours after user ${event.detail.id} was created`,
        // Take off the ms in the date timestamp
        ScheduleExpression: `at(${addMinutes(new Date(), minutesInTheFuture).toISOString().split('.')[0]})`,
      })
    );
  } catch (error) {
    console.log('failed', error);
  }
}
