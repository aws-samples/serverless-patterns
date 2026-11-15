const { CloudWatchClient, PutMetricDataCommand } = require('@aws-sdk/client-cloudwatch');
const cloudwatch = new CloudWatchClient({});

export async function main(event, context) {
    let params = {
        MetricData: [],
        Namespace: 'MyNamespace'
    }

    params.MetricData.push({
        'MetricName': 'MyMetric',
        'Dimensions': [
            { 'Name': 'Type', 'Value': event.type }
        ],
        'Unit': 'Count',
        'Value': event.value
    });

    console.log(await cloudwatch.send(new PutMetricDataCommand(params)));
};
