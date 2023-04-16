import json
import base64
import boto3
import uuid
import os

s3_client = boto3.client('s3')
region_name = os.environ['REGION_NAME']
bucket_name = os.environ['BUCKET_NAME']
STEP_FUNCTION_ARN = os.environ['STEP_FUNCTION_ARN']
textract_client = boto3.client('textract', region_name=region_name)

def lambda_handler(event, context):

    data = event['content']

    if 'fileName' in data:
        file_name = data['fileName']
    else:
        # extract file extension from base63 content and create fileName
        file_extension = extract_file_extension(data)
        file_name = f"{str(uuid.uuid1())}.{file_extension}"

    image = data[data.find(",") + 1:]
    img_str = base64.b64decode(bytearray(image, encoding="utf8"))

    response = s3_client.put_object(
        Bucket=bucket_name, Key=file_name, Body=img_str)

    my_dict = {"Key_Name": file_name, "Message": "SuccessFully uploaded to S3"}

    response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
    step_function_arn = STEP_FUNCTION_ARN
    step_function_input = {
        "Comment": {
            "content": data
        }
    }

    step_function_response = boto3.client('stepfunctions').start_execution(
        stateMachineArn=step_function_arn,
        input=json.dumps(step_function_input)
    )

    if response['ResponseMetadata']['HTTPStatusCode'] == 200:
        return {
            "statusCode": 200,
            "body": json.dumps(my_dict),
            "message": json.dumps({
                'message': 'Step Function execution started',
                'executionArn': step_function_response['executionArn']
            })
        }
    else:
        return {
            "statusCode": 400,
            "body": json.dumps("Bad Request")
        }

# Code for extracting the file extension from the encoded string data [1]
def extract_file_extension(base64_encoded_file):
    if base64_encoded_file.find(';') > -1:
        extension = base64_encoded_file.split(';')[0]
        return extension[extension.find('/') + 1:]
    return 'png'

# References:
# 1. https://stackoverflow.com/questions/10501247/best-way-to-generate-random-file-names-in-python

