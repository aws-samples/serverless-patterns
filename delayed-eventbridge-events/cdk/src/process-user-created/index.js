"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.handler = void 0;
const client_scheduler_1 = require("@aws-sdk/client-scheduler");
const addMinutes_1 = require("date-fns/addMinutes");
const client = new client_scheduler_1.SchedulerClient({});
async function handler(event) {
    try {
        // Create the schedule group for now, this would be done in CDK when we can
        await client.send(new client_scheduler_1.CreateScheduleGroupCommand({
            Name: 'SchedulesForUsers24HoursAfterCreation',
        }));
    }
    catch (error) { }
    try {
        await client.send(new client_scheduler_1.CreateScheduleCommand({
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
                Mode: client_scheduler_1.FlexibleTimeWindowMode.OFF,
            },
            Description: `24 hours after user ${event.detail.id} was created`,
            // Take off the ms in the date timestamp
            ScheduleExpression: `at(${addMinutes_1.default(new Date(), 2).toISOString().split('.')[0]})`,
        }));
    }
    catch (error) {
        console.log('failed', error);
    }
}
exports.handler = handler;
//# sourceMappingURL=data:application/json;base64,eyJ2ZXJzaW9uIjozLCJmaWxlIjoiaW5kZXguanMiLCJzb3VyY2VSb290IjoiIiwic291cmNlcyI6WyJpbmRleC50cyJdLCJuYW1lcyI6W10sIm1hcHBpbmdzIjoiOzs7QUFDQSxnRUFBdUk7QUFDdkksb0RBQTZDO0FBRTdDLE1BQU0sTUFBTSxHQUFHLElBQUksa0NBQWUsQ0FBQyxFQUFFLENBQUMsQ0FBQztBQVFoQyxLQUFLLFVBQVUsT0FBTyxDQUFDLEtBQW1EO0lBRS9FLElBQUk7UUFDRiwyRUFBMkU7UUFDM0UsTUFBTSxNQUFNLENBQUMsSUFBSSxDQUNmLElBQUksNkNBQTBCLENBQUM7WUFDN0IsSUFBSSxFQUFFLHVDQUF1QztTQUM5QyxDQUFDLENBQ0gsQ0FBQztLQUNIO0lBQUMsT0FBTyxLQUFLLEVBQUUsR0FBRTtJQUVsQixJQUFJO1FBQ0YsTUFBTSxNQUFNLENBQUMsSUFBSSxDQUNmLElBQUksd0NBQXFCLENBQUM7WUFDeEIsSUFBSSxFQUFFLEdBQUcsS0FBSyxDQUFDLE1BQU0sQ0FBQyxFQUFFLE9BQU87WUFDL0IsU0FBUyxFQUFFLHVDQUF1QztZQUNsRCxNQUFNLEVBQUU7Z0JBQ04sT0FBTyxFQUFFLE9BQU8sQ0FBQyxHQUFHLENBQUMsaUJBQWlCO2dCQUN0QyxHQUFHLEVBQUUsT0FBTyxDQUFDLEdBQUcsQ0FBQyxZQUFZO2dCQUM3QixxQkFBcUIsRUFBRTtvQkFDckIsVUFBVSxFQUFFLHVCQUF1QjtvQkFFbkMsaUVBQWlFO29CQUNqRSxNQUFNLEVBQUUseUJBQXlCO2lCQUNsQztnQkFDRCxrQ0FBa0M7Z0JBQ2xDLEtBQUssRUFBRSxJQUFJLENBQUMsU0FBUyxDQUFDLEVBQUUsR0FBRyxLQUFLLENBQUMsTUFBTSxFQUFFLENBQUM7YUFDM0M7WUFDRCxrQkFBa0IsRUFBRTtnQkFDbEIsSUFBSSxFQUFFLHlDQUFzQixDQUFDLEdBQUc7YUFDakM7WUFDRCxXQUFXLEVBQUUsdUJBQXVCLEtBQUssQ0FBQyxNQUFNLENBQUMsRUFBRSxjQUFjO1lBQ2pFLHdDQUF3QztZQUN4QyxrQkFBa0IsRUFBRSxNQUFNLG9CQUFVLENBQUMsSUFBSSxJQUFJLEVBQUUsRUFBRSxDQUFDLENBQUMsQ0FBQyxXQUFXLEVBQUUsQ0FBQyxLQUFLLENBQUMsR0FBRyxDQUFDLENBQUMsQ0FBQyxDQUFDLEdBQUc7U0FDbkYsQ0FBQyxDQUNILENBQUM7S0FDSDtJQUFDLE9BQU8sS0FBSyxFQUFFO1FBQ2QsT0FBTyxDQUFDLEdBQUcsQ0FBQyxRQUFRLEVBQUUsS0FBSyxDQUFDLENBQUM7S0FDOUI7QUFDSCxDQUFDO0FBdkNELDBCQXVDQyIsInNvdXJjZXNDb250ZW50IjpbImltcG9ydCB7IEV2ZW50QnJpZGdlRXZlbnQgfSBmcm9tICdhd3MtbGFtYmRhJztcbmltcG9ydCB7IFNjaGVkdWxlckNsaWVudCwgQ3JlYXRlU2NoZWR1bGVDb21tYW5kLCBGbGV4aWJsZVRpbWVXaW5kb3dNb2RlLCBDcmVhdGVTY2hlZHVsZUdyb3VwQ29tbWFuZCB9IGZyb20gJ0Bhd3Mtc2RrL2NsaWVudC1zY2hlZHVsZXInO1xuaW1wb3J0IGFkZE1pbnV0ZXMgZnJvbSAnZGF0ZS1mbnMvYWRkTWludXRlcyc7XG5cbmNvbnN0IGNsaWVudCA9IG5ldyBTY2hlZHVsZXJDbGllbnQoe30pO1xuXG5pbnRlcmZhY2UgVXNlckNyZWF0ZWQge1xuICBpZDogc3RyaW5nO1xuICBmaXJzdE5hbWU6IHN0cmluZztcbiAgbGFzdE5hbWU6IHN0cmluZztcbn1cblxuZXhwb3J0IGFzeW5jIGZ1bmN0aW9uIGhhbmRsZXIoZXZlbnQ6IEV2ZW50QnJpZGdlRXZlbnQ8J1VzZXJDcmVhdGVkJywgVXNlckNyZWF0ZWQ+KSB7XG5cbiAgdHJ5IHtcbiAgICAvLyBDcmVhdGUgdGhlIHNjaGVkdWxlIGdyb3VwIGZvciBub3csIHRoaXMgd291bGQgYmUgZG9uZSBpbiBDREsgd2hlbiB3ZSBjYW5cbiAgICBhd2FpdCBjbGllbnQuc2VuZChcbiAgICAgIG5ldyBDcmVhdGVTY2hlZHVsZUdyb3VwQ29tbWFuZCh7XG4gICAgICAgIE5hbWU6ICdTY2hlZHVsZXNGb3JVc2VyczI0SG91cnNBZnRlckNyZWF0aW9uJyxcbiAgICAgIH0pXG4gICAgKTtcbiAgfSBjYXRjaCAoZXJyb3IpIHt9XG5cbiAgdHJ5IHtcbiAgICBhd2FpdCBjbGllbnQuc2VuZChcbiAgICAgIG5ldyBDcmVhdGVTY2hlZHVsZUNvbW1hbmQoe1xuICAgICAgICBOYW1lOiBgJHtldmVudC5kZXRhaWwuaWR9LTI0aHJgLFxuICAgICAgICBHcm91cE5hbWU6ICdTY2hlZHVsZXNGb3JVc2VyczI0SG91cnNBZnRlckNyZWF0aW9uJyxcbiAgICAgICAgVGFyZ2V0OiB7XG4gICAgICAgICAgUm9sZUFybjogcHJvY2Vzcy5lbnYuU0NIRURVTEVfUk9MRV9BUk4sXG4gICAgICAgICAgQXJuOiBwcm9jZXNzLmVudi5FVkVOVEJVU19BUk4sXG4gICAgICAgICAgRXZlbnRCcmlkZ2VQYXJhbWV0ZXJzOiB7XG4gICAgICAgICAgICBEZXRhaWxUeXBlOiAnVXNlckNyZWF0ZWQyNEhvdXJzQWdvJyxcblxuICAgICAgICAgICAgLy8gbGV0J3MgZGVmaW5lIGEgYm91bmRlZCBjb250ZXh0L3Njb3BlIGZvciB0aGVzZSB0eXBlcyBvZiBldmVudHNcbiAgICAgICAgICAgIFNvdXJjZTogJ3NjaGVkdWxlci5ub3RpZmljYXRpb25zJyxcbiAgICAgICAgICB9LFxuICAgICAgICAgIC8vIFRoaXMgaXMgdGhlIGRldGFpbCBvZiB0aGUgZXZlbnRcbiAgICAgICAgICBJbnB1dDogSlNPTi5zdHJpbmdpZnkoeyAuLi5ldmVudC5kZXRhaWwgfSksXG4gICAgICAgIH0sXG4gICAgICAgIEZsZXhpYmxlVGltZVdpbmRvdzoge1xuICAgICAgICAgIE1vZGU6IEZsZXhpYmxlVGltZVdpbmRvd01vZGUuT0ZGLFxuICAgICAgICB9LFxuICAgICAgICBEZXNjcmlwdGlvbjogYDI0IGhvdXJzIGFmdGVyIHVzZXIgJHtldmVudC5kZXRhaWwuaWR9IHdhcyBjcmVhdGVkYCxcbiAgICAgICAgLy8gVGFrZSBvZmYgdGhlIG1zIGluIHRoZSBkYXRlIHRpbWVzdGFtcFxuICAgICAgICBTY2hlZHVsZUV4cHJlc3Npb246IGBhdCgke2FkZE1pbnV0ZXMobmV3IERhdGUoKSwgMikudG9JU09TdHJpbmcoKS5zcGxpdCgnLicpWzBdfSlgLFxuICAgICAgfSlcbiAgICApO1xuICB9IGNhdGNoIChlcnJvcikge1xuICAgIGNvbnNvbGUubG9nKCdmYWlsZWQnLCBlcnJvcik7XG4gIH1cbn1cbiJdfQ==