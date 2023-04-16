import json
import boto3

def lambda_handler(event, context):
    vegetables = event['body'].get('vegetables')
    
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('VegetableInventoryTable')
    
    for veg in vegetables:
        table.put_item(Item={'veges_item': veg})
    return {
        'statusCode': 200,
        'body': json.dumps('Vegetables uploaded successfully')
    }