import boto3

def lambda_handler(event, context):
    return start()
    



def start():
    client = boto3.client('ec2')
    response = client.describe_instances(
    Filters=[{
            'Name': 'tag:StartUp',
            'Values': [
                'True',
            ]
        },
    ])
    id= []
    for r in response['Reservations']:
        for i in r['Instances']:
            id.append(i['InstanceId'])
        
    response = client.start_instances(
    InstanceIds=id
    )
