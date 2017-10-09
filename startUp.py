import re
import boto3

def lambda_handler(event, context):
    # TODO implement
    return hello()
    



def hello():
   client = boto3.client('ec2')
   response = client.start_instances(
    InstanceIds=[
        'i-0b778eea36b4f77b1',
    ]
    )

   return response
