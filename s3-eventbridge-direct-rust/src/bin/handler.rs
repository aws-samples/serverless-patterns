use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde::{Deserialize, Serialize};

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    let config = aws_config::load_from_env().await;
    let s3_client = aws_sdk_s3::Client::new(&config);

    run(service_fn(|event: LambdaEvent<S3Event>| {
        function_handler(&s3_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_s3::Client,
    event: LambdaEvent<S3Event>,
) -> Result<(), Error> {
    println!("{:?}", event);

    let resp = client
        .get_object()
        .bucket(event.payload.bucket.name)
        .key(event.payload.object.key)
        .send()
        .await?;

    let data = resp.body.collect().await;
    println!("data: {:?}", data.unwrap().into_bytes());

    Ok(())
}

#[derive(Debug, Clone, PartialEq, Deserialize, Serialize)]
pub struct S3Event {
    pub bucket: S3Bucket,
    pub object: S3Object,
    pub reason: String,
}

#[derive(Debug, Clone, PartialEq, Deserialize, Serialize)]
pub struct S3Bucket {
    pub name: String,
}

#[derive(Debug, Clone, PartialEq, Deserialize, Serialize)]
pub struct S3Object {
    pub key: String,
    pub size: i64,
}
