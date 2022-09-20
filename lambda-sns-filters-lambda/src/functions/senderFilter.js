const AWS = require('aws-sdk');
const sns = new AWS.SNS();

exports.handler = async (event) => {
	const color = event.color;

	const text = `The color is ${color}`;

	const params = {
		Message: text,
		TopicArn: process.env.TOPIC_ARN,
		MessageAttributes: {
			color: {
				DataType: 'String',
				StringValue: color,
			},
		},
	};

	const result = await sns.publish(params).promise();
	console.log(result);
};
