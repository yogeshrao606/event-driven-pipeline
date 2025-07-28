import boto3
import csv
import io

def lambda_handler(event, context):
    print("Event received: ")
    print(event)

    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get the file object
    response = s3.get_object(Bucket=bucket, Key=key)
    content = response['Body'].read().decode('utf-8')

    # Read CSV content
    reader = csv.DictReader(io.StringIO(content))
    for row in reader:
        print("Row data:", row)

    return {
        'statusCode': 200,
        'body': 'CSV file processed successfully!'
    }
