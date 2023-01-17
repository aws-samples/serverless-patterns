use aws_lambda_events::event::{sns::SnsMessage, sqs::SqsEvent};
use futures::future::join_all;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde::Deserialize;

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    run(service_fn(|event: LambdaEvent<SqsEvent>| {
        function_handler(event)
    }))
    .await
}

pub async fn function_handler(event: LambdaEvent<SqsEvent>) -> Result<(), Error> {
    println!("Input {:?}", event);

    let mut tasks = Vec::with_capacity(event.payload.records.len());
    for record in event.payload.records.into_iter() {
        tasks.push(tokio::spawn(async move {
            if let Some(body) = &record.body {
                let sns_message = serde_json::from_str::<SnsMessage>(&body).unwrap();
                let sns_message = sns_message.message;
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
