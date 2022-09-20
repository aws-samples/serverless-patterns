const AWS = require('aws-sdk');
const sns = new AWS.SNS();

exports.handler = async (event) => {
	const date = new Date();
	const text = `Message sent at:${date.toString()}`;

	const params = {
		Message: text,
		TopicArn: process.env.TOPIC_ARN,
	};

	const result = await sns.publish(params).promise();
	console.log(result);
};
