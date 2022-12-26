use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde::{Deserialize, Serialize};
use serde_json::Value;

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let sfn_client = aws_sdk_sfn::Client::new(&config);

    run(service_fn(|event: LambdaEvent<Value>| {
        function_handler(&sfn_client, event)
    }))
    .await
}

pub async fn function_handler(
    client: &aws_sdk_sfn::Client,
    event: LambdaEvent<Value>,
) -> Result<(), Error> {
    println!("{:?}", event);

    let state_machine_arn =
        std::env::var("STATE_MACHINE_ARN").expect("STATE_MACHINE_ARN must be set");

    let result = client
        .start_execution()
        .state_machine_arn(state_machine_arn)
        .input(serde_json::to_string(&event.payload).unwrap())
        .send()
        .await?;

    println!("{:?}", result);

    Ok(())
}

#[derive(Deserialize, Serialize, Debug, Default)]
pub struct PayLoad {
    pub is_hello_world_example: String,
}
