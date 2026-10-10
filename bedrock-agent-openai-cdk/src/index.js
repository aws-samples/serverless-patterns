// Bedrock Agent action group handler — returns mock city info
const VALID_PATHS = new Set(["/getWeather", "/getTime"]);

exports.handler = async (event) => {
  const actionGroup = event.actionGroup;
  const apiPath = event.apiPath;
  const params = event.parameters || [];
  const city = (params.find((p) => p.name === "city")?.value || "").slice(0, 100).replace(/[^\w\s-]/g, "");

  if (!city) {
    return response(actionGroup, apiPath, event.httpMethod, 400, { error: "city parameter is required" });
  }

  if (apiPath === "/getWeather") {
    return response(actionGroup, apiPath, event.httpMethod, 200, {
      city,
      temperature: `${Math.floor(Math.random() * 30 + 5)}°C`,
      condition: ["Sunny", "Cloudy", "Rainy", "Windy"][Math.floor(Math.random() * 4)],
      humidity: `${Math.floor(Math.random() * 60 + 30)}%`,
    });
  }

  if (apiPath === "/getTime") {
    const now = new Date();
    return response(actionGroup, apiPath, event.httpMethod, 200, {
      city,
      utcTime: now.toISOString(),
      localNote: `Current UTC time is ${now.toUTCString()}. Adjust for ${city} timezone.`,
    });
  }

  return response(actionGroup, apiPath, event.httpMethod, 400, { error: "Unknown action" });
};

function response(actionGroup, apiPath, httpMethod, statusCode, body) {
  return {
    messageVersion: "1.0",
    response: {
      actionGroup,
      apiPath,
      httpMethod,
      httpStatusCode: statusCode,
      responseBody: { "application/json": { body: JSON.stringify(body) } },
    },
  };
}
