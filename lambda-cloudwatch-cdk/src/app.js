const AWS = require('aws-sdk');
const cloudwatch = new AWS.CloudWatch({ apiVersion: '2010-08-01' });

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

    console.log(await cloudwatch.putMetricData(params).promise());
};
