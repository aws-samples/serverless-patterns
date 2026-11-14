const { CloudWatchClient, PutMetricDataCommand } = require('@aws-sdk/client-cloudwatch')
const cloudwatch = new CloudWatchClient()

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

    console.log(await cloudwatch.send(new PutMetricDataCommand(params)))
    
};
