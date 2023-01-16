use aws_sdk_s3::types::ByteStream;
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
    let s3_client = aws_sdk_s3::Client::new(&config);

    run(service_fn(|event: LambdaEvent<Value>| {
        function_handler(&s3_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_s3::Client,
    event: LambdaEvent<Value>,
) -> Result<(), Error> {
    println!("{:?}", event);

    let bucket = std::env::var("BUCKET_NAME").expect("BUCKET_NAME must be set");

    let result = client
        .put_object()
        .bucket(bucket)
        .key("filename.txt")
        .body(ByteStream::from(String::from("ciao").into_bytes()))
        .send()
        .await?;

    println!("{:?}", result);

    Ok(())
}
