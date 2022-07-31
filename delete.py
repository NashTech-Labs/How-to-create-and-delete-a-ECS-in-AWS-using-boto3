# import the boto3 which will use to interact  with the aws

import boto3
import json

AWS_REGION = input("Enter the AWS_REGION Name")
CLUSTER_NAME = input("Enter the AWS_REGION Name")

client = boto3.client("ecs", region_name=AWS_REGION)
response = client.delete_cluster(cluster=CLUSTER_NAME)

print(json.dumps(response, indent=4))