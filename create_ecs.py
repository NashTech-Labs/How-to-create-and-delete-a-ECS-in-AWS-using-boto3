# import the boto3 which will use to interact  with the aws

import boto3
import json
REGION = input("Enter the REGION Name: ")
CLUSTER_NAME = input("Enter the Cluster Name:  ")

ECS_client = boto3.client("ecs", region_name=REGION)

res = ECS_client.create_cluster(clusterName=CLUSTER_NAME)

print(json.dumps(res, indent=4))