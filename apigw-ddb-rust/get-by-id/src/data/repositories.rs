use std::collections::HashMap;

use super::models::{Item, ItemError};
use aws_sdk_dynamodb::{types::AttributeValue, Client};
use serde_dynamo::aws_sdk_dynamodb_1::from_item;

pub async fn fetch_item(client: &Client, table_name: &str, id: &str) -> Result<Item, ItemError> {
    let key_map: HashMap<String, AttributeValue> = [
        ("pk".to_string(), AttributeValue::S(id.to_string())),
        ("sk".to_string(), AttributeValue::S(id.to_string())),
    ]
    .iter()
    .cloned()
    .collect();

    match client
        .get_item()
        .table_name(table_name)
        .set_key(Some(key_map))
        .send()
        .await
    {
        Ok(result) => {
            match result.item {
                None => return Err(ItemError::NotFound),
                Some(item) => {
                    let i: Item = from_item(item)?;
                    Ok(i)
                }
            }

            //let i: Item = from_item(result.item.unwrap())?;
            //Ok(i)
        }
        Err(e) => Err(e.into()),
    }
}
