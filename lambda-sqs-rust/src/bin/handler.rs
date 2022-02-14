use lambda_runtime::{handler_fn, Context, Error};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let sqs_client = aws_sdk_sqs::Client::new(&config);

    lambda_runtime::run(handler_fn(|event: Value, ctx: Context| {
        execute(&sqs_client, event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(client: &aws_sdk_sqs::Client, _event: Value, _ctx: Context,) -> Result<(), Error> {
    let sqs_url = std::env::var("SQS_QUEUE_NAME").expect("SQS_QUEUE_NAME must be set");

    let result = client
        .send_message()
        .queue_url(sqs_url)
        .message_body("hello from my queue")
        .send()
        .await?;

    println!("{:?}", result);

    Ok(())
}
