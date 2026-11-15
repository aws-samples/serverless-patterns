const { SNSClient, PublishCommand } = require('@aws-sdk/client-sns');
const sns = new SNSClient({});

exports.handler = async (event) => {
	const date = new Date();
	const text = `Message sent at:${date.toString()}`;

	const params = {
		Message: text,
		TopicArn: process.env.TOPIC_ARN,
	};

	const result = await sns.send(new PublishCommand(params));
	console.log(result);
};
