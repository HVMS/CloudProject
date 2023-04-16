import json
import base64
import boto3
import os
from difflib import SequenceMatcher

s3_client = boto3.client('s3')
REGION_NAME = os.environ['REGION_NAME']
BUCKET_NAME = os.environ['BUCKET_NAME']
textract_client = boto3.client('textract',region_name = REGION_NAME)
table_client = boto3.client('dynamodb', region_name = REGION_NAME)

def lambda_handler(event,context):
    
    data = event['content']
    
    image = data[data.find(",") + 1:]
    img_str = base64.b64decode(bytearray(image, encoding="utf8"))
    
    response = textract_client.detect_document_text(
                                    Document={'Bytes': img_str,'S3Object': {
                                    'Bucket': BUCKET_NAME,
                                    'Name': 'order' + data[0:4]}})
    
    file_content = []
    
    for block in response['Blocks']:
            if block['BlockType'] == 'LINE':
                file_content.append(block['Text'])
    
    table_scan_response = table_client.scan(TableName='VegetableInventoryTable')
    inventory_vegetables = table_scan_response['Items']
    
    inventory_veges_available = []
    for veges in inventory_vegetables:
        inventory_veges_available.append(veges['veges_item']['S'])
    
    matched_order = []
    for checking_item in file_content:
        for inventory_item in inventory_veges_available:
            if is_almost_matched(checking_item, inventory_item):
                matched_order.append(checking_item)

    print(matched_order)
    print(len(matched_order))
    
    if len(matched_order) == len(file_content):
        return {
            "statusCode": 200,
            "message" : "Fully Order Completed!!",
            "body": json.dumps(matched_order)
        }
    else:
        return {
            "statusCode": 200,
            "message" : "Partial Order Completed!!",
            "body": json.dumps(matched_order)
        }

# Code for matching the sequence for string 1 and string 2 [1]    
def is_almost_matched(string1, string2, threshold=0.8):
    matcher = SequenceMatcher(None, string1, string2)
    ratio = matcher.ratio()
    # Compare the similarity ratio with the threshold value
    if ratio >= threshold:
        return True
    else:
        return False

# References:
# 1. https://towardsdatascience.com/sequencematcher-in-python-6b1e6f3915fc