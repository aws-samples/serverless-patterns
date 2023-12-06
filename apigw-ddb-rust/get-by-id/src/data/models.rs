use aws_sdk_dynamodb::{error::SdkError, types::AttributeValue};
use display_json::DisplayAsJsonPretty;
use serde::{Deserialize, Serialize};
use serde_json::Value;
use std::collections::HashMap;
use thiserror::Error;

#[derive(Serialize, Deserialize, Debug, DisplayAsJsonPretty)]
pub struct Item {
    pk: String,
    sk: String,
}

impl Item {
    fn new(pk: String, sk: String) -> Self {
        Item { pk: pk, sk: sk }
    }
}

#[derive(Error, Debug)]
pub enum ItemError {
    #[error("failed to parse serde_json::Value into Item {0}")]
    FromValue(&'static Value),

    #[error("failed to parse response into items: {0}")]
    FromSerde(serde_dynamo::Error),

    #[error("aws_sdk_dynamodb error: {0}")]
    Dynamo(aws_sdk_dynamodb::Error),

    #[error("item not found")]
    NotFound,

    #[error("unknown DynamoDB item error: {0}")]
    Unknown(String),
}

impl From<aws_sdk_dynamodb::Error> for ItemError {
    fn from(err: aws_sdk_dynamodb::Error) -> Self {
        ItemError::Dynamo(err)
    }
}

impl From<serde_dynamo::Error> for ItemError {
    fn from(err: serde_dynamo::Error) -> Self {
        ItemError::FromSerde(err)
    }
}

impl<E, R> From<SdkError<E, R>> for ItemError
where
    E: std::fmt::Debug,
    R: std::fmt::Debug,
{
    fn from(err: SdkError<E, R>) -> Self {
        ItemError::Unknown(format!("{err:?}"))
    }
}
