exports.handler = async (event) => {
  const { events } = event;

  if (!events || !Array.isArray(events)) {
    return { error: 'No events received' };
  }

  console.log(`OnPublish interceptor invoked for ${events.length} event(s)`);

  // AppSync Events OnPublish (REQUEST_RESPONSE) expects { events: [{ id, payload }] }.
  // payload must be a JSON value (object), not a re-stringified string, and each
  // outgoing event must echo back the original event id.
  const outgoing = events.map((e) => {
    let payload = e.payload;
    if (typeof payload === 'string') {
      try {
        payload = JSON.parse(payload);
      } catch (err) {
        return { id: e.id, payload: { error: 'Invalid JSON payload' } };
      }
    }
    return {
      id: e.id,
      payload: {
        ...payload,
        processedAt: new Date().toISOString(),
        enriched: true,
        messageId: `msg-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`,
      },
    };
  });

  return { events: outgoing };
};
