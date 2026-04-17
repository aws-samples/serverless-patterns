exports.handler = async (event) => {
  for (const record of event.Records) {
    const body = JSON.parse(record.body);
    const detail = body.detail || {};

    console.log(
      JSON.stringify({
        tenantId: detail.tenantId,
        orderId: detail.orderId,
        amount: detail.amount,
        messageGroupId: record.attributes?.MessageGroupId,
        messageId: record.messageId,
        timestamp: new Date().toISOString(),
      })
    );
  }

  return { batchItemFailures: [] };
};
