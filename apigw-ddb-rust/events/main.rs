use std::env;

// use aws_config::meta::region::RegionProviderChain;
use aws_lambda_events::apigw::{ApiGatewayProxyRequest, ApiGatewayProxyResponse};
use aws_sdk_dynamodb::Client;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde_json::json;

use crate::data::{
    models::{Item, ItemError},
    repositories::fetch_item,
};

mod data;

async fn function_handler(
    client: &Client,
    table_name: &str,
    event: LambdaEvent<ApiGatewayProxyRequest>,
) -> Result<ApiGatewayProxyResponse, Error> {
    let mut resp = ApiGatewayProxyResponse {
        status_code: 200,
        is_base64_encoded: Some(false),
        body: Some("".into()),
        multi_value_headers: Default::default(),
        headers: Default::default(),
    };

    match event.payload.path_parameters.get("id") {
        Some(value) => {
            tracing::info!("(Value)={}", value);
            let item: Result<Item, ItemError> = fetch_item(client, table_name, value).await;
            tracing::info!("Item retrieved now");
            tracing::info!("(Item)={:?}", item);
            match item {
                Ok(item) => {
                    let body = json!(item).to_string();
                    resp.body = Some(body.into());
                }
                Err(error) => {
                    tracing::error!("{}", error);
                    resp.status_code = 404;
                }
            }
        }
        None => {
            tracing::error!("Key doesn't exist");
            resp.status_code = 404;
        }
    }

    Ok(resp)
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .json()
        .with_max_level(tracing::Level::INFO)
        .with_target(false)
        .init();

    let stream = env::var("TABLE_NAME").unwrap();
    let str_pointer = stream.as_str();

    let config = aws_config::from_env().profile_name("personal").load().await;
    let client = Client::new(&config);
    let shared_client = &client;

    run(service_fn(
        move |event: LambdaEvent<ApiGatewayProxyRequest>| async move {
            function_handler(&shared_client, str_pointer, event).await
        },
    ))
    .await
}
