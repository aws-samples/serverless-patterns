exports.handler = async (event) => {
  // AppSync Events handler - processes published messages
  const { events } = event;

  if (!events || !Array.isArray(events)) {
    return { events: [{ payload: { error: 'No events received' } }] };
  }

  const processed = events.map(e => {
    const payload = JSON.parse(e.payload);
    return {
      payload: JSON.stringify({
        ...payload,
        processedAt: new Date().toISOString(),
        enriched: true,
        messageId: `msg-${Date.now()}-${Math.random().toString(36).slice(2, 8)}`
      })
    };
  });

  return { events: processed };
};
