import os
import json
import boto3

dynamodb_table_name = os.environ.get("DYNAMO_DB_TABLE")
dynamodb = boto3.resource("dynamodb")


def lambda_handler(event, context):
    print("Begin Event *************")
    try:
        event_source = event.get("eventSource", "")
        event_source_arn = event.get("eventSourceArn", "")
        print(f"EventSource = {event_source}")
        print(f"EventSourceARN = {event_source_arn}")

        events = event.get("events", [])
        for event_element in events:
            print("Starting a new message **************")
            event_event = event_element.get("event", {})

            event_id_data = event_event.get("_id", {}).get("_data", "")
            operation_type = event_event.get("operationType", "")
            ns = event_event.get("ns", {})
            database = ns.get("db", "")
            collection = ns.get("coll", "")
            document_key_id = event_event.get("documentKey", {}).get("_id", "")
            cluster_time = event_event.get("clusterTime", {}).get("$timestamp", {})
            cluster_time_t = cluster_time.get("t", 0)
            cluster_time_i = cluster_time.get("i", 0)

            full_document = event_event.get("fullDocument", {})
            customer_id = full_document.get("_id", "")
            firstname = full_document.get("Firstname", "")
            lastname = full_document.get("Lastname", "")
            street = full_document.get("Street", "")
            city = full_document.get("City", "")
            county = full_document.get("County", "")
            state = full_document.get("State", "")
            zip_code = full_document.get("Zip", "")
            home_phone = full_document.get("HomePhone", "")
            cell_phone = full_document.get("CellPhone", "")
            email = full_document.get("Email", "")
            company = full_document.get("Company", "")
            website = full_document.get("Website", "")

            print(f"EventIDData = {event_id_data}")
            print(f"OperationType = {operation_type}")
            print(f"Database = {database}")
            print(f"Collection = {collection}")
            print(f"DocumentKeyID = {document_key_id}")
            print(f"ClusterTimeTimeStampT = {cluster_time_t}")
            print(f"ClusterTimeTimeStampI = {cluster_time_i}")
            print(f"CustomerID = {customer_id}")
            print(f"CustomerFirstname = {firstname}")
            print(f"CustomerLastname = {lastname}")
            print(f"CustomerStreet = {street}")
            print(f"CustomerCity = {city}")
            print(f"CustomerCounty = {county}")
            print(f"CustomerState = {state}")
            print(f"CustomerZip = {zip_code}")
            print(f"CustomerHomePhone = {home_phone}")
            print(f"CustomerCellPhone = {cell_phone}")
            print(f"CustomerEmail = {email}")
            print(f"CustomerCompany = {company}")
            print(f"CustomerWebsite = {website}")
            print("Finishing a new message **************")

            aws_sam_local = os.environ.get("AWS_SAM_LOCAL")
            if aws_sam_local is None and dynamodb_table_name:
                insert_into_dynamodb(
                    event_event, event_source, event_source_arn
                )

    except Exception as e:
        print(f"Error: {str(e)}")

    print("End Event ***************")


def insert_into_dynamodb(event_event, event_source, event_source_arn):
    table = dynamodb.Table(dynamodb_table_name)
    full_document = event_event.get("fullDocument", {})
    message_id = full_document.get("_id", "")

    print(f"Now inserting a row in DynamoDB for messageID = {message_id}")

    item = {
        "MessageID": message_id,
        "EventSource": event_source,
        "EventSourceARN": event_source_arn,
        "EventIDData": event_event.get("_id", {}).get("_data", ""),
        "OperationType": event_event.get("operationType", ""),
        "DocumentDBDatabase": event_event.get("ns", {}).get("db", ""),
        "DocumentDBCollection": event_event.get("ns", {}).get("coll", ""),
        "DocumentKeyID": event_event.get("documentKey", {}).get("_id", ""),
        "ClusterTimeTimeStampT": event_event.get("clusterTime", {}).get("$timestamp", {}).get("t", 0),
        "ClusterTimeTimeStampI": event_event.get("clusterTime", {}).get("$timestamp", {}).get("i", 0),
        "CustomerID": full_document.get("_id", ""),
        "CustomerFirstname": full_document.get("Firstname", ""),
        "CustomerLastname": full_document.get("Lastname", ""),
        "CustomerStreet": full_document.get("Street", ""),
        "CustomerCity": full_document.get("City", ""),
        "CustomerCounty": full_document.get("County", ""),
        "CustomerState": full_document.get("State", ""),
        "CustomerZip": full_document.get("Zip", ""),
        "CustomerHomePhone": full_document.get("HomePhone", ""),
        "CustomerCellPhone": full_document.get("CellPhone", ""),
        "CustomerEmail": full_document.get("Email", ""),
        "CustomerCompany": full_document.get("Company", ""),
        "CustomerWebsite": full_document.get("Website", ""),
    }

    table.put_item(Item=item)
    print(f"Now done inserting a row in DynamoDB for messageID = {message_id}")
