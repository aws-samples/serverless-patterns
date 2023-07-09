exports.handler = async (event) => {
	console.log('Consumer RED');
	console.log(JSON.stringify(event, 2, null));
};
