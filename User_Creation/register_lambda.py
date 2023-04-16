import boto3
import hashlib
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']
table = dynamodb.Table(table_name)
salt = b'hello_world'
sns_client = boto3.client('sns')

def lambda_handler(event, context):
    # TODO implement
    
    body = event['body']
    username = body['username']
    email = body['email']
    password = body['password']
    
    # Check if Email id is already exists
    response = table.get_item(Key={'email': email})
    if 'Item' in response:
        return {'statusCode': 400, 'body': 'Email id is already exists'}

    response = sns_client.subscribe(TopicArn=TOPIC_ARN,
        Protocol='email',
        Endpoint=email
    )
    
    # Hashes the password and storing into DB as well as the Users storing into Dynamo DB User Table
    dk = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)    # Inline Reference 1
    hashed_password = dk.hex()
    
    table.put_item(Item={'username': username, 'email': email, 'password': hashed_password, 'loggedin': False})
    
    return {
        'statusCode': 200,
        'body': 'User Registration Successfully Done!!',
        'message' : 'Please Confirm Your Email!!'
    }

#References:
# 1. https://stackoverflow.com/questions/72927860/hashing-and-salts-of-pickle-in-python