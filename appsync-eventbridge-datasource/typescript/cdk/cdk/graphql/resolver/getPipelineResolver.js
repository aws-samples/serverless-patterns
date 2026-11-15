/**
 * AppSync resolver: implements before and after business logic for your pipeline
 * Find more samples and templates at https://github.com/aws-samples/aws-appsync-resolver-samples
 */
/**
 * Called before the request function of the first AppSync function in the pipeline.
 * @param ctx The context object that holds contextual information about the function invocation.
 */
export function request(ctx) {  
	return {}
}
/**
 * Called after the response function of the last AppSync function in the pipeline.
 * @param  ctx The context object that holds contextual information about the function invocation.
 */
export function response(ctx) {
	return ctx.prev.result;
}
