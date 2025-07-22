// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

use aws_config::{meta::region::RegionProviderChain, BehaviorVersion};
use aws_sdk_bedrockruntime::{
    types::{ContentBlock, ConversationRole, ConverseStreamOutput, Message},
    Client,
};
use bytes::Bytes;
use lambda_runtime::{
    service_fn,
    streaming::{channel, Body, Response},
    Error as LambdaError, LambdaEvent,
};
use serde::{Deserialize, Serialize};
use serde_json::Value;
use tracing::{error, info};

const MODEL_ID: &str = "anthropic.claude-3-haiku-20240307-v1:0";

/// Bedrock story
#[derive(Debug, Deserialize)]
struct StoryRequest {
    #[serde(rename = "storyType")]
    story_type: String,
}

/// Response for each stream record sent from Amazon Bedrock
#[derive(Debug, Serialize)]
struct BedrockResponse {
    #[serde(rename = "type")]
    response_type: String,
    message: Option<String>,
}

/// Main Lambda handler here...
async fn function_handler(event: LambdaEvent<Value>) -> Result<Response<Body>, LambdaError> {
    let region_provider = RegionProviderChain::default_provider().or_else("us-east-1");
    let config = aws_config::defaults(BehaviorVersion::latest())
        .region(region_provider)
        .load()
        .await;

    info!("Received event...: {:?}", event);

    let body = event.payload
        .get("body")
        .and_then(Value::as_str)
        .ok_or_else(|| LambdaError::from("Failed to parse request body"))?;

    match serde_json::from_str::<StoryRequest>(body) {
        Ok(request) => {
            info!("Received request...: {:?}", request);
            let bedrock_client = Client::new(&config);
            handle_story_request(bedrock_client, request).await
        }
        Err(e) => Err(LambdaError::from(format!(
            "Failed to parse request body: {:?}",
            e
        ))),
    }
}

/// Handle the incoming story request
async fn handle_story_request(
    bedrock_client: Client,
    request: StoryRequest,
) -> Result<Response<Body>, LambdaError> {
    // Construct the prompt based on the type of story to create
    let prompt: String = format!("Tell me a very short story about: {}", request.story_type);
    info!("Bedrock story prompt...: {}", prompt);

    // Invoke Bedrock with prompt - process the stream
    process_bedrock_stream(prompt, bedrock_client).await
}

/// Process the Bedrock stream
async fn process_bedrock_stream(
    prompt: String,
    bedrock_client: Client,
) -> Result<Response<Body>, LambdaError> {
    // Create a communication channel between transmitter & receiver
    let (mut tx, rx) = channel();

    // Create a response using the Converse API
    let bedrock_response = bedrock_client
        .converse_stream()
        .model_id(MODEL_ID)
        .messages(
            Message::builder()
                .role(ConversationRole::User)
                .content(ContentBlock::Text(prompt))
                .build()
                .map_err(|_| LambdaError::from("failed to build message"))?,
        )
        .send()
        .await;

    let mut converse_stream = match bedrock_response {
        Ok(output) => Ok(output.stream),
        Err(e) => {
            error!("Error in Bedrock response: {:?}", e);
            Err(LambdaError::from(format!(
                "Error in Bedrock response: {:?}",
                e
            )))
        }
    }?;

    // Spawn a task to process the Bedrock stream
    tokio::spawn(async move {
        info!("Bedrock stream processing started...");
        loop {
            let token = converse_stream.recv().await;
            match token {
                Ok(Some(output)) => {
                    info!("Bedrock response: {:?}", output);
                    let response = get_response(output).map_err(LambdaError::from)?;
                    let bytes = Bytes::from(serde_json::to_vec(&response).map_err(|e| {
                        LambdaError::from(format!("Failed to serialize response: {:?}", e))
                    })?);
                    if let Err(e) = tx.send_data(bytes).await {
                        error!("Receiver dropped error: {:?}", e);
                        return Err(LambdaError::from(
                            "Receiver dropped error. Bedrock proccessing stopped.",
                        ));
                    }
                }
                Ok(None) => break Ok(()),
                Err(e) => {
                    error!("Error receiving stream: {:?}", e);
                    return Err(LambdaError::from("Error receiving stream"));
                }
            }
        }
    });

    info!("Bedrock stream processing complete...");
    Ok(Response::from(rx))
}

/// Process an output token from the Bedrock response stream
fn get_response(output: ConverseStreamOutput) -> Result<BedrockResponse, LambdaError> {
    match output {
        ConverseStreamOutput::ContentBlockDelta(event) => match event.delta() {
            Some(delta) => {
                let text = delta.as_text().map_err(|e| {
                    LambdaError::from(format!("Failed to get text from delta: {:?}", e))
                })?;
                Ok(BedrockResponse {
                    response_type: "text".into(),
                    message: Some(text.to_string()),
                })
            }
            None => Ok(BedrockResponse {
                response_type: "message".into(),
                message: Some("".into()),
            }),
        },
        _ => Ok(BedrockResponse {
            response_type: "other".into(),
            message: None,
        }),
    }
}

/// Lambda Entry
#[tokio::main]
async fn main() -> Result<(), LambdaError> {
    tracing_subscriber::fmt()
        .with_max_level(tracing::Level::INFO)
        .with_target(false)
        .without_time()
        .init();

    lambda_runtime::run(service_fn(function_handler)).await?;
    Ok(())
}
