require 'aws-sdk-bedrockruntime'
require 'json'

def lambda_handler(event:, context:)
  client = Aws::BedrockRuntime::Client.new
  prompt = event['prompt'] || 'What are the benefits of serverless computing?'

  response = client.invoke_model(
    model_id: ENV['MODEL_ID'],
    content_type: 'application/json',
    accept: 'application/json',
    body: JSON.generate({
      anthropic_version: 'bedrock-2023-05-31',
      max_tokens: 512,
      messages: [{ role: 'user', content: prompt }]
    })
  )

  result = JSON.parse(response.body.read)
  {
    statusCode: 200,
    body: JSON.generate({
      response: result.dig('content', 0, 'text'),
      model: ENV['MODEL_ID'],
      runtime: "ruby#{RUBY_VERSION}"
    })
  }
end
