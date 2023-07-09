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
    let sqs_client = aws_sdk_sqs::Client::new(&config);

    run(service_fn(|event: LambdaEvent<Value>| {
        function_handler(&sqs_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_sqs::Client,
    _event: LambdaEvent<Value>,
) -> Result<(), Error> {
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
