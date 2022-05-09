use aws_lambda_events::event::{sns::SnsEntity, sqs::SqsEvent};
use futures::future::join_all;
use lambda_runtime::{service_fn, Error, LambdaEvent};
use serde::Deserialize;

#[tokio::main]
async fn main() -> Result<(), Error> {
    // required to enable CloudWatch error logging by the runtime
    tracing_subscriber::fmt()
        // this needs to be set to false, otherwise ANSI color codes will
        // show up in a confusing manner in CloudWatch logs.
        .with_ansi(false)
        // disabling time is handy because CloudWatch will add the ingestion time.
        .without_time()
        .init();

    lambda_runtime::run(service_fn(|event: LambdaEvent<SqsEvent>| execute(event))).await?;

    Ok(())
}

pub async fn execute(event: LambdaEvent<SqsEvent>) -> Result<(), Error> {
    println!("Input {:?}", event);

    let mut tasks = Vec::with_capacity(event.payload.records.len());
    for record in event.payload.records.into_iter() {
        tasks.push(tokio::spawn(async move {
            if let Some(body) = &record.body {
                let sns_message = serde_json::from_str::<SnsEntity>(&body).unwrap();
                let sns_message = sns_message.message.unwrap();
                let request = serde_json::from_str::<MyStruct>(&sns_message);
                if let Ok(request) = request {
                    // Do something
                    println!("Request {:?}", request);
                }
            }
        }));
    }

    join_all(tasks).await;

    Ok(())
}

#[derive(Deserialize, Debug, Clone, PartialEq, Eq)]
pub struct MyStruct {
    pub name: String,
    pub surname: String,
}
