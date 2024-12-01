use aws_lambda_events::s3::S3Entity;
use aws_sdk_rekognition::types::Image;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    let config = aws_config::load_from_env().await;
    let rekognition_client = aws_sdk_rekognition::Client::new(&config);

    run(service_fn(|event: LambdaEvent<S3Entity>| {
        function_handler(&rekognition_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_rekognition::Client,
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

    let s3_object = aws_sdk_rekognition::types::S3Object::builder()
        .bucket(bucket_name)
        .name(object_key)
        .build();

    let params = Image::builder().s3_object(s3_object).build();

    let result = client.detect_text().image(params).send().await?;

    let text_detections = result.text_detections();

    for text_detection in text_detections.iter().filter(|x| x.parent_id.is_none()) {
        println!("{:?}", text_detection);
    }

    if text_detections.is_empty() {
        println!("No text detected");
    }

    Ok(())
}
