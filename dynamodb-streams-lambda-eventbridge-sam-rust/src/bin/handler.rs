use aws_lambda_events::dynamodb::Event;
use aws_sdk_eventbridge::model::PutEventsRequestEntry;
use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use std::sync::Arc;
use tokio::task::JoinSet;
use typed_builder::TypedBuilder as Builder;

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    let config = aws_config::from_env().load().await;

    let eb_client = aws_sdk_eventbridge::Client::new(&config);
    let bus_name = std::env::var("BUS_NAME").expect("BUS_NAME must be set");

    let app_client = AppClient::builder()
        .bus_name(bus_name)
        .eb_client(eb_client)
        .build();

    run(service_fn(|event: LambdaEvent<Event>| {
        function_handler(&app_client, event)
    }))
    .await
}

pub async fn function_handler(
    app_client: &AppClient,
    event: LambdaEvent<Event>,
) -> Result<(), Error> {
    println!("{event:?}");
    let entries: Vec<Vec<PutEventsRequestEntry>> = event
        .payload
        .records
        .chunks(10)
        .map(|chunk| {
            chunk
                .iter()
                .map(|record| {
                    let new_image =
                        serde_json::to_string(&record.clone().change.new_image).unwrap();
                    PutEventsRequestEntry::builder()
                        .event_bus_name(&app_client.bus_name)
                        .source("demo.event")
                        .detail_type("INSERTED")
                        .detail(new_image)
                        .build()
                })
                .collect::<Vec<_>>()
        })
        .collect();

    let mut set = JoinSet::new();
    let shared_client = Arc::from(app_client.clone());
    for entry in entries.into_iter() {
        let shared_client = shared_client.clone();
        set.spawn(async move {
            shared_client
                .eb_client
                .put_events()
                .set_entries(Some(entry))
                .send()
                .await
                .map_or_else(
                    |e| {
                        println!("{e:?}");
                    },
                    |result| {
                        println!("{result:?}");
                    },
                );
        });
    }

    while let Some(res) = set.join_next().await {
        if let Err(e) = res {
            println!("{e:?}");
        }
    }

    Ok(())
}

#[derive(Debug, Clone, Builder)]
pub struct AppClient {
    #[builder(setter(into))]
    pub bus_name: String,

    #[builder(setter(into))]
    pub eb_client: aws_sdk_eventbridge::Client,
}
