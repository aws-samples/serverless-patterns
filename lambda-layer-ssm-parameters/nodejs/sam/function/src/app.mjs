// Use the "config" variable from the Lambda Layer.
// Create and sharing Lambda layers: https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html
// Lambda extracts the layer contents into the /opt directory when setting up the execution environment for the function.
import { config } from "/opt/nodejs/config.mjs";

export async function handler(event, context) {
  try {
    console.log("Config:\n", JSON.stringify(config));

    // Loop through each of the results in the Parameters array and output the Name, Type, and Value to CloudWatch Logs.
    config.Parameters.map((r, i) => {
      console.log(`Parameter ${i} Name: `, r.Name);
      console.log(`Parameter ${i} Type: `, r.Type);
      console.log(`Parameter ${i} Value: `, r.Value);
    });

    const response = {
      statusCode: 200,
      body: JSON.stringify(config),
    };
    return response;
  } catch (error) {
    console.error(error);
    throw new Error(error);
  }
}