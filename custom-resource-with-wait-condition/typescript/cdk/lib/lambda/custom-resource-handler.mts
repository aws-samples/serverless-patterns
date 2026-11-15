import { CloudFormationCustomResourceEvent, CloudFormationCustomResourceHandler, CloudFormationCustomResourceResponse, Context } from "aws-lambda";
import { SFNClient, StartExecutionCommand } from "@aws-sdk/client-sfn";
import { randomUUID } from "node:crypto";

const sfnClient = new SFNClient({});

//#region Local TypeScript version of the cfn-response package
type Status = 'SUCCESS' | 'FAILED';

/**
 * Creates a CloudFormation custom resource response template
 */
function responseTemplate(event: CloudFormationCustomResourceEvent, context: Context, physicalResourceId: string, reason?: string) {
    return {
        PhysicalResourceId: physicalResourceId,
        LogicalResourceId: event.LogicalResourceId,
        RequestId: event.RequestId,
        StackId: event.StackId,
        NoEcho: false,
        Reason: reason || (`See the details in CloudWatch Log Stream: ${context.logStreamName}`),
    };
};

/**
 * Sends response back to CloudFormation
 */
async function send(event: CloudFormationCustomResourceEvent, context: Context, status: Status, physicalResourceId: string, reason?: string): Promise<void> {
    const response: CloudFormationCustomResourceResponse = {
        ...responseTemplate(event, context, physicalResourceId, reason),
        Status: status,
    };
    const responseBody = JSON.stringify(response);
    const sendResult = await fetch(event.ResponseURL, {
        method: 'PUT',
        body: responseBody,
    });
    console.log(`${sendResult.status}: ${sendResult.statusText}`);
};
//#endregion 

/**
 * Custom resource handler that starts a Step Function for long-running processes.
 * Returns immediately after starting the execution - the Step Function handles completion signaling.
 */
export const handler: CloudFormationCustomResourceHandler = async (event, context) => {
    console.log(event);

    // Generate unique physical resource ID for new resources, reuse for updates/deletes
    const physicalResourceId = (event.RequestType === 'Update' || event.RequestType === 'Delete')
        ? event.PhysicalResourceId
        : randomUUID();

    try {
        // Extract required properties from custom resource
        const stateMachineArn = event.ResourceProperties.StateMachineArn;
        const waitConditionHandle = event.ResourceProperties.WaitConditionHandle;

        // Prepare payload for Step Function execution
        const stepFunctionInput = {
            RequestType: event.RequestType,
            WaitConditionHandle: waitConditionHandle,
            PhysicalResourceId: physicalResourceId,
            LogicalResourceId: event.LogicalResourceId,
            RequestId: event.RequestId,
            StackId: event.StackId
        };

        // Start Step Function execution asynchronously
        const startExecutionCommand = new StartExecutionCommand({
            stateMachineArn: stateMachineArn,
            input: JSON.stringify(stepFunctionInput)
        });

        const executionResult = await sfnClient.send(startExecutionCommand);
        console.log('Step Function execution started:', executionResult.executionArn);

        // Return success immediately - Step Function will signal completion via wait condition
        await send(event, context, 'SUCCESS', physicalResourceId, 'Step Function execution started successfully');
    }
    catch (e: any) {
        console.error(e.message);
        await send(event, context, 'FAILED', physicalResourceId, e.message);
    }
}