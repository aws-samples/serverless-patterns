exports.handler = async (event, context, callback) => {
	console.log(event);

	const message = {
		MessageBody: `Message at ${Date()}`,
	};

	if (event.test === 'fail') {
		console.log('error');
		throw new Error('ERROR!');
	} else {
		console.log(message);
		return { message };
	}
};
