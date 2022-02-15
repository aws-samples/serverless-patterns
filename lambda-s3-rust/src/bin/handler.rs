use aws_sdk_s3::ByteStream;
use lambda_runtime::{handler_fn, Context, Error};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let s3_client = aws_sdk_s3::Client::new(&config);

    lambda_runtime::run(handler_fn(|event: Value, ctx: Context| {
        execute(&s3_client, event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(client: &aws_sdk_s3::Client, event: Value, _ctx: Context,) -> Result<(), Error> {
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
