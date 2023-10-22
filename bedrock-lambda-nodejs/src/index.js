const {
  BedrockRuntimeClient,
  InvokeModelCommand

} = require("@aws-sdk/client-bedrock-runtime")

// a client can be shared by different commands.
const client = new BedrockRuntimeClient({ region: "us-west-2" })

exports.handler = async event => {

  const { text } = event

  const body = {
    "prompt": `provide a summary of the following text in 5 bulletpoints; 
    extract 5 tags to categorize the article in a CMS;
    provide output as a json object with properties :
    "summary" as a list of bulletpoints and "tags" as a list of tags;
    <text>${text}</text>
    `,
    "maxTokens": 1600,
    "temperature": 0.3,
    "topP": 1.0,
    "stopSequences": [],
    "countPenalty": { "scale": 0 },
    "presencePenalty": { "scale": 0 },
    "frequencyPenalty": { "scale": 0 }
  }

  const params = {
    "modelId": "ai21.j2-ultra-v1",
    "contentType": "application/json",
    "accept": "application/json",
    "body": JSON.stringify(body)
  }

  const command = new InvokeModelCommand(params)
  
  let data, completions

  try {
    data = await client.send(command)

    completions = JSON.parse(new TextDecoder().decode(data.body)).completions
    console.log(JSON.parse(completions[0].data.text))

    
  }
  catch (error) {
    console.error(error)
  }

  const response = {
    statusCode: 200,
    body: JSON.stringify(completions[0].data.text),
  }

  return response
}
