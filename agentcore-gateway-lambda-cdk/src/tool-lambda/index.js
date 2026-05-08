// AgentCore Gateway Lambda tool target handler
// The Gateway routes MCP tool calls to this Lambda, passing only the arguments.
exports.handler = async (event) => {
  const city = typeof event.city === "string"
    ? event.city.slice(0, 100).replace(/[^\w\s-]/g, "")
    : "";

  if (!city) {
    return {
      content: [{ type: "text", text: JSON.stringify({ error: "city is required" }) }],
      isError: true,
    };
  }

  return {
    content: [
      {
        type: "text",
        text: JSON.stringify({
          city,
          temperature: `${Math.floor(Math.random() * 30 + 5)}°C`,
          condition: ["Sunny", "Cloudy", "Rainy", "Windy"][Math.floor(Math.random() * 4)],
          humidity: `${Math.floor(Math.random() * 60 + 30)}%`,
          utcTime: new Date().toISOString(),
        }),
      },
    ],
  };
};
