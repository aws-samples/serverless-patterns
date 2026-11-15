import { SchedulerClient, CreateScheduleCommand, FlexibleTimeWindowMode } from '@aws-sdk/client-scheduler';

const client = new SchedulerClient({});
const minutesInTheFuture = parseInt(process.env.TRIGGER_IN_FUTURE_IN_MINUTES || '2');


export const handler = async (event) => {
  
  // Received event upon user creation
  console.log('Received event:', JSON.stringify(event, null, 2));
  
    try {
    await client.send(
      new CreateScheduleCommand({
        Name: `${event.detail.id}-24hr`,
        GroupName: 'SchedulesForUsers24HoursAfterCreation',
        ActionAfterCompletion: 'DELETE',
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
        ScheduleExpression: `at(${new Date((new Date()).getTime() + (minutesInTheFuture * 60000)).toISOString().split('.')[0]})`,
      })
    );
  } catch (error) {
    console.log('failed', error);
  }
};
