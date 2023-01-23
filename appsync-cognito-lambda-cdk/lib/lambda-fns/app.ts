type AppSyncEvent = {
	info: {
		fieldName: string
	}
	arguments: {
		id: string
	}
}

exports.handler = async (event: AppSyncEvent) => {
	console.log(JSON.stringify(event))
	return {
		id: event.arguments.id,
		email: 'test@sample.com',
		profilePicUrl: 'https://catpic.com',
		username: 'Serverless Cat',
	}
}
