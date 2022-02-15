use lambda_runtime::{handler_fn, Context, Error};
use serde::{Deserialize, Serialize};

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let s3_client = aws_sdk_s3::Client::new(&config);

    lambda_runtime::run(handler_fn(|event: S3Event, ctx: Context| {
        execute(&s3_client, event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(client: &aws_sdk_s3::Client, event: S3Event, _ctx: Context) -> Result<(), Error> {
    println!("{:?}", event);

    let resp = client
        .get_object()
        .bucket(event.bucket.name)
        .key(event.object.key)
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