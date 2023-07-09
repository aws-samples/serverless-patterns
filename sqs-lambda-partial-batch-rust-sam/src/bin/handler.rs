use aws_lambda_events::event::sqs::SqsEvent;
use futures::future::join_all;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde::{Deserialize, Serialize};
use serde_json::Value;
use std::sync::{Arc, Mutex};

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

pub async fn function_handler(event: LambdaEvent<SqsEvent>) -> Result<Value, Error> {
    println!("Input {:?}", event);
    let failed_message: Arc<Mutex<Vec<String>>> = Arc::new(Mutex::new(Vec::new()));
    let mut tasks = Vec::with_capacity(event.payload.records.len());

    for record in event.payload.records.into_iter() {
        let failed_message = failed_message.clone();

        tasks.push(tokio::spawn(async move {
            if let Some(body) = &record.body {
                let request = serde_json::from_str::<MyStruct>(&body);
                if let Ok(request) = request {
                    do_something(&request).await.map_or_else(
                        |_e| {
                            failed_message
                                .lock()
                                .unwrap()
                                .push(record.message_id.unwrap().clone());
                        },
                        |_| (),
                    );
                } else {
                    failed_message
                        .lock()
                        .unwrap()
                        .push(record.message_id.unwrap().clone());
                }
            }
        }));
    }

    join_all(tasks).await;

    let response = BatchItemFailures {
        batch_item_failures: failed_message
            .lock()
            .unwrap()
            .clone()
            .into_iter()
            .map(|message_id| {
                return ItemIdentifier {
                    item_identifier: message_id,
                };
            })
            .collect(),
    };

    Ok(serde_json::to_value(response).unwrap())
}

async fn do_something(request: &MyStruct) -> Result<(), Error> {
    println!("do_something {:?}", request);
    Ok(())
}

#[derive(Deserialize, Debug, Clone, PartialEq, Eq)]
pub struct MyStruct {
    pub name: String,
    pub surname: String,
}

#[derive(Deserialize, Serialize, Debug, Clone, PartialEq, Eq)]
pub struct BatchItemFailures {
    #[serde(rename = "batchItemFailures")]
    pub batch_item_failures: Vec<ItemIdentifier>,
}

#[derive(Deserialize, Serialize, Debug, Clone, PartialEq, Eq)]
pub struct ItemIdentifier {
    #[serde(rename = "itemIdentifier")]
    pub item_identifier: String,
}
