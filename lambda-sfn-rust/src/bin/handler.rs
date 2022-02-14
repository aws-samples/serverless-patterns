use lambda_runtime::{handler_fn, Context, Error};
use serde::{Serialize, Deserialize};

#[tokio::main]
async fn main() -> Result<(), Error> {
    let config = aws_config::load_from_env().await;
    let sfn_client = aws_sdk_sfn::Client::new(&config);

    lambda_runtime::run(handler_fn(|event: PayLoad, ctx: Context| {
        execute(&sfn_client, event, ctx)
    }))
    .await?;

    Ok(())
}

pub async fn execute(client: &aws_sdk_sfn::Client, event: PayLoad, _ctx: Context,) -> Result<(), Error> {
  println!("{:?}", event);

    let state_machine_arn = std::env::var("STATE_MACHINE_ARN").expect("STATE_MACHINE_ARN must be set");

    let result = client
        .start_execution()
        .state_machine_arn(state_machine_arn)
        .input(serde_json::to_string(&event).unwrap())
        .send()
        .await?;

    println!("{:?}", result);

    Ok(())
}

#[derive(Deserialize, Serialize, Debug, Default)]
pub struct PayLoad {
  pub is_hello_world_example: String,
}