const { SNSClient, PublishCommand } = require('@aws-sdk/client-sns');
const sns = new SNSClient({});

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

	const result = await sns.send(new PublishCommand(params));
	console.log(result);
};
