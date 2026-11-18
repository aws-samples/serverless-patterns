exports.handler = async (event) => {
  const detail = event.detail || {};
  // A single object argument is written as nested JSON fields when the function's log format is JSON.
  console.info({
    summary: 'EventBridge data plane API call detected',
    eventName: detail.eventName,
    eventSource: detail.eventSource,
    sourceIPAddress: detail.sourceIPAddress,
    userAgent: detail.userAgent,
    userIdentity: detail.userIdentity?.arn,
    eventBusName: detail.requestParameters?.entries?.[0]?.eventBusName || 'default',
    entryCount: detail.requestParameters?.entries?.length || 0,
    eventTime: detail.eventTime,
  });
};
