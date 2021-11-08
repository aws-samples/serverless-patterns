const AWS = require('aws-sdk')
const cloudwatch = new AWS.CloudWatch({apiVersion: '2010-08-01'})

exports.lambdaHandler = async (event, context) => {

    let params = {
        MetricData: [],
        Namespace: 'ExampleNamespace'
    }

    params.MetricData.push({
        'MetricName': 'ExampleMetric',
        'Dimensions': [
            { 'Name': 'Type', 'Value': event.type }
        ],
        'Unit': 'Count',
        'Value': event.value
    })

    console.log(await cloudwatch.putMetricData(params).promise())
    
};
