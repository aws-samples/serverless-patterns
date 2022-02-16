use aws_sdk_eventbridge::model::PutEventsRequestEntry;
use lambda_runtime::{handler_fn, Context, Error};
use serde::{Deserialize, Serialize};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let eventbridge_client = aws_sdk_eventbridge::Client::new(&config);

    lambda_runtime::run(handler_fn(|event: Value, ctx: Context| {
        execute(&eventbridge_client, event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(client: &aws_sdk_eventbridge::Client, event: Value, _ctx: Context,) -> Result<(), Error> {
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
