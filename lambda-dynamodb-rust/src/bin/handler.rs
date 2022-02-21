use aws_sdk_dynamodb::model::AttributeValue;
use chrono::Utc;
use lambda_runtime::{handler_fn, Context, Error};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let dynamodb_client = aws_sdk_dynamodb::Client::new(&config);

    lambda_runtime::run(handler_fn(|event: Value, ctx: Context| {
        execute(&dynamodb_client, event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(client: &aws_sdk_dynamodb::Client, _event: Value, _ctx: Context,) -> Result<(), Error> {
    let table = std::env::var("TABLE_NAME").expect("TABLE_NAME must be set");

    let metadata = serde_json::to_string(&_event).unwrap();

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

