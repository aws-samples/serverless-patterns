import { util } from '@aws-appsync/utils'

export function request(ctx) {
	const scheduleName =
		ctx.args.input.title.toLowerCase().split(' ').join('-') +
		util.time.nowISO8601()
	const id = util.autoId()

	ctx.stash.scheduleName = scheduleName
	ctx.stash.id = id

	return {
		method: 'POST',
		resourcePath: `/schedules/${scheduleName}`,
		params: {
			headers: { 'Content-Type': 'application/json' },
			body: {
				FlexibleTimeWindow: { Mode: 'OFF' },
				Target: {
					Arn: ctx.stash.SNS_TOPIC_ARN,
					RoleArn: ctx.stash.SCHEDULER_ROLE_ARN,
					Input: `
title: ${ctx.args.input.title}

message: ${ctx.args.input.message}
`,
				},
				ClientToken: id,
				// 'at(yyyy-mm-ddThh:mm:ss)'
				ScheduleExpression: `at(${ctx.args.input.deliveryTime})`,
				ScheduleExpressionTimezone: ctx.args.input.timezone,
			},
		},
	}
}

export function response(ctx) {
	// The ctx.result is set to the response from the EventBridge Scheduler service, but that's not very useful since it's just the Arn of the Scheduler. So instead, I'm returning my own response that matches the shape of a "Schedule" type in our schema.
	return {
		id: ctx.stash.id,
		title: ctx.args.input.title,
		message: ctx.args.input.message,
		timezone: ctx.args.input.timezone,
		deliveryTime: ctx.args.input.deliveryTime,
		scheduleName: ctx.stash.scheduleName,
	}
}
