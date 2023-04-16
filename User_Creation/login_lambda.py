import boto3
import hashlib
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)
salt = b'hello_world'

def lambda_handler(event, context):
    # TODO implement
    
    body = event['body']
    email = body['email']
    password = body['password']
    
    # Check if user exists and password is correct
    response = table.get_item(Key={'email': email})
    if 'Item' not in response:
        return {'statusCode': 400, 'body': 'Invalid username or password'}
    else:
        user = response['Item']
        if (user['email'] == email) and (user['password'] == hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000).hex()):    # Inline Reference 1
            table.update_item(
                Key={'email': email},
                UpdateExpression='SET loggedin = :val',
                ExpressionAttributeValues={':val': True}
            )
            return {'statusCode': 200, 'body': 'Login successful'}
        else:
            return {'statusCode': 400, 'body': 'Invalid username or password'}
        
#References:
# 1. https://stackoverflow.com/questions/72927860/hashing-and-salts-of-pickle-in-python