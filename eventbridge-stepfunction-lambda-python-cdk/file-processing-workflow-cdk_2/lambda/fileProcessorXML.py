import boto3
import xml.etree.ElementTree as ET
import os



def lambda_handler(event, context):
    destination_bucket_name = os.getenv("destination_bucket_name", default=None)
    print(destination_bucket_name)
    # Extract bucket name and object name from the Lambda event
    print("XML handler invoked")
    try:
        bucket_name = event['body']['bucket_name']
        object_key = event['body']['object_key']
        print("-----"+object_key)
        print("---"+bucket_name)
    except KeyError as e:
        print("Invalid event payload. Missing key: "+str(e))

   

    # Initialize S3 client
    s3_client = boto3.client('s3')

    # Fetch the XML file from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    xml_data = response['Body'].read().decode('ISO-8859-1')
    print("xml_data"+xml_data)

    # Parse the XML data
    root = ET.fromstring(xml_data)

    # Find the DEPARTMENT_ID element
    department_id = root.find(".//DEPARTMENT_ID").text
    print("department_id"+department_id);

    # Create a new DEPARTMENT_NAME element based on DEPARTMENT_ID value
    department_name = "Management" if department_id == "5346" else "Finance"
    department_name_elem = ET.Element("DEPARTMENT_NAME")
    department_name_elem.text = department_name

    # Append the new DEPARTMENT_NAME element to the TRANSACTION element
    transaction_elem = root.find(".//TRANSACTION")
    transaction_elem.append(department_name_elem)

    
    # Serialize the modified XML
    modified_xml = ET.tostring(root, encoding='ISO-8859-1')
    # Print the modified XML
    modified_xml_str = modified_xml.decode('ISO-8859-1')
    print(modified_xml_str)
    

    # Upload the modified XML back to S3
   # modified_object_key = 'modified_' + object_name
    s3_client.put_object(Bucket=destination_bucket_name, Key=object_key, Body=modified_xml)

    return {
        'statusCode': 200,
        #'body': f'Modified XML uploaded as {modified_object_key} in {bucket_name}'
        'body': 'Modified XML uploaded'
    }
