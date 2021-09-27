import json
import boto3

def lambda_handler(event, context):
    glue=boto3.client('glue')
    
    # give your crwler name here
    glue.start_crawler(Name='remoteclazz-emr-crawler')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successfully Executed')
    }