// AgentCore Gateway Lambda tool target handler
// The Gateway routes MCP tool calls to this Lambda. The event holds the tool arguments and
// context.clientContext.custom.bedrockAgentCoreToolName holds the invoked tool as
// "<target name>___<tool name>" (for example "city-tools___get_time").
exports.handler = async (event, context) => {
  const fullName = context.clientContext?.custom?.bedrockAgentCoreToolName ?? "";
  const toolName = fullName.split("___").pop();
  const city = typeof event.city === "string"
    ? event.city.slice(0, 100).replace(/[^\w\s-]/g, "")
    : "";
  const text = (obj, isError = false) => ({
    content: [{ type: "text", text: JSON.stringify(obj) }],
    ...(isError && { isError: true }),
  });

  if (!city) return text({ error: "city is required" }, true);

  if (toolName === "get_time") {
    return text({ city, utcTime: new Date().toISOString() });
  }
  if (toolName === "get_weather") {
    return text({
      city,
      temperature: `${Math.floor(Math.random() * 30 + 5)}°C`,
      condition: ["Sunny", "Cloudy", "Rainy", "Windy"][Math.floor(Math.random() * 4)],
      humidity: `${Math.floor(Math.random() * 60 + 30)}%`,
    });
  }
  return text({ error: `unknown tool: ${toolName}` }, true);
};
