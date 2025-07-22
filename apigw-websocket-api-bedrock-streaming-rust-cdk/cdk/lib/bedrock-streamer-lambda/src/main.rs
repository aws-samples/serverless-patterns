// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

use aws_config::{meta::region::RegionProviderChain, BehaviorVersion, SdkConfig};
use aws_lambda_events::apigw::ApiGatewayWebsocketProxyRequest;
use aws_sdk_apigatewaymanagement::{
    config::Builder, primitives::Blob as ApiGatewayBlob, Client as ApiGatewayManagementClient,
};
use aws_sdk_bedrockruntime::{
    types::{ContentBlock, ConversationRole, ConverseStreamOutput, Message},
    Client,
};
use http::Uri;
use lambda_runtime::{service_fn, Error as LambdaError, LambdaEvent};
use serde::{Deserialize, Serialize};
use tokio::sync::mpsc;
use tracing::{error, info};

const MODEL_ID: &str = "anthropic.claude-3-haiku-20240307-v1:0";

const WS_CONNECT: &str = "$connect";
const WS_DISCONNECT: &str = "$disconnect";
const WS_DEFAULT: &str = "$default";

/// Bedrock story
#[derive(Debug, Deserialize)]
struct StoryRequest {
    #[serde(rename = "storyType")]
    story_type: String,
}

/// Amazon API Gateway response
#[derive(serde::Serialize)]
struct ApiGatewayResponse {
    #[serde(rename = "statusCode")]
    status_code: u16,
    body: String,
}

/// Response for each stream record sent from Amazon Bedrock
#[derive(Debug, Serialize)]
struct BedrockResponse {
    #[serde(rename = "type")]
    response_type: String,
    message: Option<String>,
}

/// Main Lambda handler here...
async fn function_handler(
    event: LambdaEvent<ApiGatewayWebsocketProxyRequest>,
) -> Result<ApiGatewayResponse, LambdaError> {
    let region_provider = RegionProviderChain::default_provider().or_else("us-east-1");
    let config = aws_config::defaults(BehaviorVersion::latest())
        .region(region_provider)
        .load()
        .await;

    let connection_id = event
        .payload
        .request_context
        .connection_id
        .as_deref()
        .ok_or_else(|| LambdaError::from("Missing connection_id"))?;
    let domain_name = event
        .payload
        .request_context
        .domain_name
        .as_deref()
        .ok_or_else(|| LambdaError::from("Missing domain_name"))?;
    let stage = event
        .payload
        .request_context
        .stage
        .as_deref()
        .ok_or_else(|| LambdaError::from("Missing stage"))?;

    match event.payload.request_context.route_key.as_deref() {
        Some(WS_CONNECT) => handle_connect(connection_id).await,
        Some(WS_DISCONNECT) => handle_disconnect(connection_id).await,
        Some(WS_DEFAULT) => {
            let bedrock_client = Client::new(&config);
            let apigw_client = api_gateway_config(domain_name, stage, &config)?;
            let request_body = event.payload.body;

            handle_default(bedrock_client, apigw_client, connection_id, request_body).await
        }
        Some(_) | None => Ok(ApiGatewayResponse {
            status_code: 400,
            body: "Unknown route".into(),
        }),
    }
}

fn api_gateway_config(
    domain_name: &str,
    stage: &str,
    config: &SdkConfig,
) -> Result<ApiGatewayManagementClient, LambdaError> {
    let endpoint = format!("https://{}/{}", domain_name, stage);
    let uri = match endpoint.parse::<Uri>() {
        Ok(uri) => uri,
        Err(e) => {
            return Err(LambdaError::from(format!(
                "Failed to parse endpoint URI: {:?}",
                e
            )))
        }
    };
    let apigw_client = ApiGatewayManagementClient::from_conf(
        Builder::from(config).endpoint_url(uri.to_string()).build(),
    );
    Ok(apigw_client)
}

/// Handle WebSocket connection
async fn handle_connect(connection_id: &str) -> Result<ApiGatewayResponse, LambdaError> {
    info!("Handle $connect: {}", connection_id);
    Ok(ApiGatewayResponse {
        status_code: 200,
        body: "Connected...: $connect".into(),
    })
}

/// Handle WebSocket disconnect
async fn handle_disconnect(connection_id: &str) -> Result<ApiGatewayResponse, LambdaError> {
    info!("Handle $disconnect: {}", connection_id);
    Ok(ApiGatewayResponse {
        status_code: 200,
        body: "Disconnected...: $disconnect".into(),
    })
}

/// Handle WebSocket default message
async fn handle_default(
    bedrock_client: Client,
    apigw_client: ApiGatewayManagementClient,
    connection_id: &str,
    request_body: Option<String>,
) -> Result<ApiGatewayResponse, LambdaError> {
    info!("Handle $default: {}", connection_id);

    // Parse the incoming JSON payload
    let story_request: StoryRequest = match request_body {
        Some(body) => serde_json::from_str(&body)
            .map_err(|e| LambdaError::from(format!("Failed to parse request body: {:?}", e)))?,
        None => Err(LambdaError::from("Missing request body"))?,
    };

    // Construct the prompt based on the type of story to create
    let prompt: String = format!(
        "Tell me a very short story about: {}",
        story_request.story_type
    );
    info!("Bedrock story prompt...: {}", prompt);

    // Start reading from Bedrock & writing the API GW
    bedrock_websocket_pipeline(
        prompt,
        bedrock_client,
        apigw_client,
        connection_id.to_string(),
    )
    .await?;

    Ok(ApiGatewayResponse {
        status_code: 200,
        body: "Message processed...: $default".into(),
    })
}

/// Start the Bedrock + Websocket threads
async fn bedrock_websocket_pipeline(
    prompt: String,
    bedrock_client: Client,
    apigw_client: ApiGatewayManagementClient,
    connection_id: String,
) -> Result<(), LambdaError> {
    info!("Starting Bedrock + WebSocket pipeline...");

    let (sender, receiver) = mpsc::channel(32); // Adjust buffer size as needed

    let bedrock_task =
        tokio::spawn(async move { process_bedrock_stream(sender, prompt, bedrock_client).await });

    let websocket_task =
        tokio::spawn(async move { send_to_websocket(receiver, apigw_client, connection_id).await });

    // Wait for both tasks to complete
    let (bedrock_result, websocket_result) = tokio::try_join!(bedrock_task, websocket_task)
        .map_err(|e| LambdaError::from(format!("Task join error: {:?}", e)))?;

    // Propagate errors from the tasks
    bedrock_result?;
    websocket_result?;

    Ok(())
}

/// Process the Bedrock stream
#[tracing::instrument]
async fn process_bedrock_stream(
    sender: mpsc::Sender<BedrockResponse>,
    prompt: String,
    bedrock_client: Client,
) -> Result<(), LambdaError> {
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
            Err(LambdaError::from("Error in Bedrock response"))
        }
    }?;

    loop {
        let token = converse_stream.recv().await;
        match token {
            Ok(Some(output)) => {
                info!("Bedrock response: {:?}", output);
                let response = get_response(output).map_err(LambdaError::from)?;
                if let Err(e) = sender.send(response).await {
                    error!("Receiver dropped error: {:?}", e);
                    return Err(LambdaError::from(
                        "Receiver dropped error. Bedrock proccessing stopped.",
                    ));
                }
            }
            Ok(None) => break,
            Err(e) => {
                error!("Error receiving stream: {:?}", e);
                return Err(LambdaError::from("Error receiving stream"));
            }
        }
    }

    info!("Bedrock stream processing complete...");
    Ok(())
}

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

/// Process incoming Bedrock messages and send to WebSocket
#[tracing::instrument]
async fn send_to_websocket(
    mut reciever: mpsc::Receiver<BedrockResponse>,
    apigw_client: ApiGatewayManagementClient,
    connection_id: String,
) -> Result<(), LambdaError> {
    while let Some(response) = reciever.recv().await {
        info!("Sending to WebSocket: {:?}", response);
        apigw_client
            .post_to_connection()
            .connection_id(&connection_id)
            .data(ApiGatewayBlob::new(
                serde_json::to_vec(&response).map_err(|e| LambdaError::from(e.to_string()))?,
            ))
            .send()
            .await
            .map_err(LambdaError::from)?;
    }

    info!("WebSocket sender complete...");
    Ok(())
}

/// Lambda Entry
#[tokio::main]
async fn main() -> Result<(), LambdaError> {
    tracing_subscriber::fmt()
        .with_max_level(tracing::Level::INFO)
        .with_target(false)
        .without_time()
        .init();

    lambda_runtime::run(service_fn(function_handler)).await
}
