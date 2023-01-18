use aws_sdk_rekognition::model::Image;
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
    let rekognition_client = aws_sdk_rekognition::Client::new(&config);

    run(service_fn(|event: LambdaEvent<S3Event>| {
        function_handler(&rekognition_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_rekognition::Client,
    event: LambdaEvent<S3Event>,
) -> Result<(), Error> {
    println!("{:?}", event);

    let s3_object = aws_sdk_rekognition::model::S3Object::builder()
        .bucket(event.payload.bucket.name)
        .name(event.payload.object.key)
        .build();

    let params = Image::builder().s3_object(s3_object).build();

    let result = client.detect_text().image(params).send().await?;

    if let Some(text_detections) = result.text_detections() {
        for text_detection in text_detections.into_iter().filter(|x| x.parent_id == None) {
            println!("{:?}", text_detection);
        }
    } else {
        println!("No text detected");
    }

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
