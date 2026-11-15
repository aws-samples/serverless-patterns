import { SchedulerClient, DeleteScheduleCommand, GetScheduleCommand } from '@aws-sdk/client-scheduler';
import { SQSEvent } from 'aws-lambda';
import { differenceInDays } from 'date-fns';

// Will delete one-time schedules that happened more than 2 days ago.
const AGE_IN_DAYS_TO_DELETE_SCHEDULES_FROM = 2;

const client = new SchedulerClient({});

interface Schedule {
    Arn: string;
    Name: string;
    GroupName: string;
}

const processSchedules = async (scheduleList: Schedule[]) => {
    const info = scheduleList.map((schedule) =>
        client.send(
            new GetScheduleCommand({
                Name: schedule.Name,
                GroupName: schedule.GroupName,
            }),
        ),
    );

    const schedules = await Promise.all(info);

    // only get schedules that are one time schedules (we look at at property)
    const oneTimeSchedules = schedules.filter((schedule) => schedule.ScheduleExpression?.match(/^at\(*.*\)/));

    // loop around one time schedules and only remove them if they are after the desired TTL
    const oneTimeSchedulesToRemoved = oneTimeSchedules.filter((schedule) => {
        const { ScheduleExpression } = schedule;
        const regex = ScheduleExpression?.match(/(?<=\().+?(?=\))/);
        const dateOfSchedule = regex ? regex[0] : null;

        if (dateOfSchedule) {
            // const today = new Date('2022-12-19T23:50:00');
            const today = new Date();
            const numberOfDaysOld = differenceInDays(today, new Date(dateOfSchedule));
            return numberOfDaysOld >= AGE_IN_DAYS_TO_DELETE_SCHEDULES_FROM;
        }

        return false;
    });

    // We have schedules that match our critera, let's remove them
    const removeSchedules = oneTimeSchedulesToRemoved.map((schedule) => {
        console.log(`Removing schedule: ${schedule.Name} from group ${schedule.GroupName}`);
        return client.send(
            new DeleteScheduleCommand({
                Name: schedule.Name,
                GroupName: schedule.GroupName,
            }),
        );
    });

    console.log(`Removed ${removeSchedules.length} one time schedules.`);
};

/**
 * Process schedule removal in batches of 10 from SQS.
 */
export const handler = async (event: SQSEvent): Promise<any> => {
    const { Records: schedules } = event;

    const schedulesToProcess = schedules.map((schedule) => JSON.parse(schedule.body));

    try {
        await processSchedules(schedulesToProcess);
    } catch (error) {
        console.log(error);
        throw Error('Failed to process');
    }
};
