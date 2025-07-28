import json
import boto3

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))
    for record in event.get('Records', []):
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        print(f"New object in bucket {bucket}: {key}")
    return {"statusCode": 200, "body": "Processed."}
