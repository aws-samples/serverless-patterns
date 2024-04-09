import { CloudFormationCustomResourceEvent, CloudFormationCustomResourceResponse, Context, SQSHandler } from "aws-lambda";

type Status = 'SUCCESS' | 'FAILED';

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

async function send(event: CloudFormationCustomResourceEvent, context: Context, status: Status, physicalResourceId: string, reason?: string): Promise<void> {
    const response: CloudFormationCustomResourceResponse = {
        ...responseTemplate(event, context, physicalResourceId, reason),
        Status: status,
    };
    const responseBody = JSON.stringify(response);
    await fetch(event.ResponseURL, {
        method: 'PUT',
        body: responseBody,
    });
};

export const handler: SQSHandler  = async (event, context) => {
    console.log('Custom Resource Finalizer');
    console.log(event);

    const resourceInfo = JSON.parse(event.Records[0].body) as CloudFormationCustomResourceEvent;
    console.log(resourceInfo);

    const physicalResourceId = (resourceInfo.RequestType === 'Update' || resourceInfo.RequestType === 'Delete')
        ? resourceInfo.PhysicalResourceId
        : 'InternallyCreatedPhysicalResourceId'; // It is expected to create a unique Physical Resource Id when creating a new Custom Resource.

    try {
        //
        // Optionally: add additional business logic here
        //

        await send(resourceInfo, context, 'SUCCESS', physicalResourceId, undefined);
    }
    catch (e: any) {
        console.error(e.message);
        await send(resourceInfo, context, 'FAILED', physicalResourceId, e.message);
    }
}