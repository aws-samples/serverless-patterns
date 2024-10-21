use aws_lambda_events::s3::S3Entity;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    let config = aws_config::load_from_env().await;
    let s3_client = aws_sdk_s3::Client::new(&config);

    run(service_fn(|event: LambdaEvent<S3Entity>| {
        function_handler(&s3_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_s3::Client,
    event: LambdaEvent<S3Entity>,
) -> Result<(), Error> {
    println!("{:?}", event);

    let bucket_name = event
        .payload
        .bucket
        .name
        .as_ref()
        .ok_or("Bucket name is missing")?;
    let object_key = event
        .payload
        .object
        .key
        .as_ref()
        .ok_or("Object key is missing")?;

    let resp = client
        .get_object()
        .bucket(bucket_name)
        .key(object_key)
        .send()
        .await?;

    let data = resp.body.collect().await;
    println!("data: {:?}", data.unwrap().into_bytes());

    Ok(())
}
