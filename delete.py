# import the boto3 which will use to interact  with the aws

import boto3
import json

REGION = input("Enter the AWS REGION Name:  ")
CLUSTER_NAME = input("Enter the Cluster Name:  ")

ECS_client = boto3.client("ecs", region_name=REGION)
response = ECS_client.delete_cluster(cluster=CLUSTER_NAME)

print(json.dumps(response, indent=4))