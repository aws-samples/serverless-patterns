use aws_sdk_rekognition::model::Image;
use lambda_runtime::{handler_fn, Context, Error};
use serde::{Deserialize, Serialize};

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let rekognition_client = aws_sdk_rekognition::Client::new(&config);

    lambda_runtime::run(handler_fn(|event: S3Event, ctx: Context| {
        execute(&rekognition_client, event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(client: &aws_sdk_rekognition::Client, event: S3Event, _ctx: Context) -> Result<(), Error> {
    println!("{:?}", event);

    let s3_object = aws_sdk_rekognition::model::S3Object::builder()
        .bucket(event.bucket.name)
        .name(event.object.key)
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
