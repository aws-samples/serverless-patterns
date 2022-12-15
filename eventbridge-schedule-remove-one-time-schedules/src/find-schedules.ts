import { SchedulerClient, ListSchedulesCommand } from '@aws-sdk/client-scheduler';
import { SendMessageBatchCommand, SQSClient } from '@aws-sdk/client-sqs';
import { v4 as uuid } from 'uuid';

const client = new SchedulerClient({});
const sqsClient = new SQSClient({});

const getSchedulesToProcess = async (token?: string) => {
    return client.send(
        new ListSchedulesCommand({
            State: 'ENABLED',
            NextToken: token,
        }),
    );
};

export const handler = async (event: any): Promise<any> => {
    let { Schedules, NextToken } = await getSchedulesToProcess();

    // Find all schedules
    do {
        const data = await getSchedulesToProcess(NextToken);
        NextToken = data.NextToken;
        Schedules = data.Schedules ? Schedules?.concat(data.Schedules) : Schedules;
    } while (NextToken);

    // Write all schedules onto SQS queue for processing
    const sqsMessages = Schedules?.map((schedule) => {
        return {
            Id: uuid(),
            MessageBody: JSON.stringify({
                ARN: schedule.Arn,
                Name: schedule.Name,
                GroupName: schedule.GroupName,
            }),
        };
    });

    if (sqsMessages) {
        console.log(`Sending ${sqsMessages.length} messages...`);
        const sqsBatches = [];
        const size = 10;

        while (sqsMessages.length > 0) sqsBatches.push(sqsMessages.splice(0, size));

        // batch up to 10 messages at a time to send to SQS, so we process them downstream in batches
        const sendMessageBatchCommands = sqsBatches.map((batch) =>
            sqsClient.send(
                new SendMessageBatchCommand({
                    Entries: batch,
                    QueueUrl: process.env.QUEUE_URL,
                }),
            ),
        );

        await Promise.all(sendMessageBatchCommands);
    }
};
