use lambda_runtime::{run, service_fn, Error, LambdaEvent};
use serde::{Deserialize, Serialize};
use serde_json::Value;
use std::collections::HashMap;
use std::sync::Mutex;

#[macro_use]
extern crate lazy_static;

lazy_static! {
    static ref CONFIG: Mutex<HashMap<String, MyConfig>> = Mutex::new(HashMap::new());
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    tracing_subscriber::fmt()
        .with_ansi(false)
        .without_time()
        .with_max_level(tracing_subscriber::filter::LevelFilter::INFO)
        .init();

    run(service_fn(|event: LambdaEvent<Value>| {
        function_handler(event)
    }))
    .await
}

pub async fn function_handler(_event: LambdaEvent<Value>) -> Result<(), Error> {
    // ASSUME that this profile is coming from some logic and not from the env variable
    let appconfig_profile =
        std::env::var("AWS_APPCONFIG_PROFILE").expect("AWS_APPCONFIG_PROFILE must be set");
    if CONFIG.lock().unwrap().contains_key(&appconfig_profile) {
        println!(
            "CONFIG FROM HASHMAP{:?}",
            CONFIG.lock().unwrap().get(&appconfig_profile).unwrap()
        );
    } else {
        let config = fetch_config(&appconfig_profile).await?;
        println!("ADDED INTO HASHMAP{:?}", appconfig_profile);
        CONFIG.lock().unwrap().insert(appconfig_profile, config);
    }

    Ok(())
}

async fn fetch_config(appconfig_profile: &str) -> Result<MyConfig, Error> {
    let appconfig_name = std::env::var("APP_CONFIG_NAME").expect("APP_CONFIG_NAME must be set");
    let appconfig_env =
        std::env::var("AWS_APPCONFIG_ENVIRONMENT").expect("AWS_APPCONFIG_ENVIRONMENT must be set");
    let appconfig_port = std::env::var("AWS_APPCONFIG_EXTENSION_HTTP_PORT")
        .expect("AWS_APPCONFIG_EXTENSION_HTTP_PORT must be set");

    let url = format!(
        "http://localhost:{}/applications/{}/environments/{}/configurations/{}",
        appconfig_port, appconfig_name, appconfig_env, appconfig_profile
    );
    let response = reqwest::get(url).await?.json::<MyConfig>().await?;

    Ok(response)
}

#[derive(Debug, Deserialize, Serialize)]
pub struct MyConfig {
    pub id: u16,
    pub name: String,
    pub rank: u16,
}
