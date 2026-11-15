import { util, extensions, Context, AppSyncIdentityIAM } from '@aws-appsync/utils';

export function request(ctx: Context) {
	return { payload: null };
}

export function response(ctx: Context) {
    // This demo code uses IAM authorization model only, thus it is safe to hardcode the type here
    const identity = ctx.identity as AppSyncIdentityIAM;

	const filter = { userId: { eq: identity.username } };
    
	extensions.setSubscriptionFilter(util.transform.toSubscriptionFilter(filter));

    // Null response is required!!!
	return null;
}