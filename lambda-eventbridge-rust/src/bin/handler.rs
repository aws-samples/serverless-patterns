use aws_sdk_eventbridge::model::PutEventsRequestEntry;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde::{Deserialize, Serialize};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    let config = aws_config::load_from_env().await;
    let eventbridge_client = aws_sdk_eventbridge::Client::new(&config);

    run(service_fn(|event: LambdaEvent<Value>| {
        function_handler(&eventbridge_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_eventbridge::Client,
    event: LambdaEvent<Value>,
) -> Result<(), Error> {
    println!("{:?}", event);

    let event_bus_name = std::env::var("EVENT_BUS_NAME").expect("EVENT_BUS_NAME must be set");

    let message = MyMessage {
        message: "Hello from publisher".to_string(),
        state: "new".to_string(),
    };

    let params = PutEventsRequestEntry::builder()
        .event_bus_name(event_bus_name)
        .source("demo.event")
        .detail_type("Message")
        .detail(serde_json::to_string(&message)?)
        .build();

    let result = client.put_events().entries(params).send().await?;

    println!("{:?}", result);

    Ok(())
}

#[derive(Deserialize, Serialize, Debug)]
pub struct MyMessage {
    pub message: String,
    pub state: String,
}
