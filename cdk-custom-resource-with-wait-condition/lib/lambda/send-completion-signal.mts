import { Handler } from "aws-lambda";

/**
 * Status values for wait condition signals
 */
enum Status {
    SUCCESS = 'SUCCESS',
    FAILURE = 'FAILURE',
}

/**
 * Event payload for task completion signaling
 */
interface TaskCompletionEvent {
    readonly waitConditionHandle: string;
    readonly status: Status;
    readonly uniqueId: string;
    readonly data: string;
    readonly reason: string;
}

/**
 * Sends completion signal to CloudFormation wait condition handle
 */
async function send(responseURL: string, status: Status, reason: string, uniqueId: string, data: string): Promise<void> {
    const response = {
        Status: status,
        Reason: reason,
        UniqueId: uniqueId,
        Data: data,
    };
    const responseBody = JSON.stringify(response);
    const sendResult = await fetch(responseURL, {
        method: 'PUT',
        body: responseBody,
    });
    console.log(`${sendResult.status}: ${sendResult.statusText}`);
};

/**
 * Lambda handler that sends completion signals to wait condition handles.
 * Called by Step Functions when long-running processes complete.
 */
export const handler: Handler<TaskCompletionEvent> = async (event) => {
    console.log(event);
    const { waitConditionHandle, status, uniqueId, data, reason } = event;
    await send(waitConditionHandle, status, reason, uniqueId, data);
}