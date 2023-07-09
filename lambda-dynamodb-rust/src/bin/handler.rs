use aws_sdk_dynamodb::model::AttributeValue;
use chrono::Utc;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    let config = aws_config::load_from_env().await;
    let dynamodb_client = aws_sdk_dynamodb::Client::new(&config);

    run(service_fn(|event: LambdaEvent<Value>| {
        function_handler(&dynamodb_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_dynamodb::Client,
    event: LambdaEvent<Value>,
) -> Result<(), Error> {
    let table = std::env::var("TABLE_NAME").expect("TABLE_NAME must be set");

    let metadata = serde_json::to_string(&event.payload).unwrap();

    let result = client
        .put_item()
        .table_name(table)
        .item("ID", AttributeValue::S(Utc::now().timestamp().to_string()))
        .item("metadata", AttributeValue::S(metadata.into()))
        .send()
        .await?;

    println!("{:?}", result);

    Ok(())
}
