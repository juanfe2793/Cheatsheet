# This python script will describe all EC2 instances in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

# Before describing the EC2 instances, we need to check if we have permission to describe EC2 instances in all regions.
# If we don't have permission to describe EC2 instances in a region, we will get the following error:
# botocore.exceptions.ClientError: An error occurred (UnauthorizedOperation) when calling the DescribeInstances operation: You are not authorized to perform this operation.

def check_describe_instances_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_instances()
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe EC2 instances")
            return False
    return True

# Describe EC2 instances in a region
def describe_ec2_instances_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        instances = ec2conn.describe_instances()["Reservations"]
        print(f"Found {len(instances)} instances in region {region_name}")

        # Create a table with the following columns: Instance ID, Instance Type, Region
        table = PrettyTable(["Instance ID", "Instance Type", "Region"])

        for instance in instances:
            instance_id = instance['Instances'][0]['InstanceId']
            instance_type = instance['Instances'][0]['InstanceType']
            
            # Add a row to the table for each instance
            table.add_row([instance_id, instance_type, region_name])

        print(table)
        
        return instances
    except Exception as e:
        print(f"The following error occurs trying to describe EC2 instances in region: {region_name}: {e}")
        return []


def describe_ec2_instances():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_instances_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_ec2_instances_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                instances = future.result()
        
        print(f"Summary: Found {len(instances)} instances across all regions")

if __name__ == "__main__":
    describe_ec2_instances()