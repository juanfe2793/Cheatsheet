# This python script will describe all EC2 amis in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

# Check if we have permission to describe AMIs in a region
def check_describe_amis_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_images(Owners=["self"])
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe EC2 AMIs")
            return False
    return True

# Describe EC2 amis in a region
def describe_ec2_amis_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        amis = ec2conn.describe_images(Owners=["self"])["Images"]
        print(f"Found {len(amis)} AMIs in region {region_name}")

        # Create a table with the following columns: AMI ID, AMI Name, Region
        table = PrettyTable(["AMI ID", "AMI Name", "Region"])

        for ami in amis:
            ami_id = ami["ImageId"]
            ami_name = ami["Name"]
            
            # Add a row to the table for each AMI
            table.add_row([ami_id, ami_name, region_name])

        print(table)
        
        return amis
    except Exception as e:
        print(f"The following error occurs trying to describe EC2 AMIs in region: {region_name}: {e}")
        return []


def describe_ec2_amis():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_amis_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_ec2_amis_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                amis = future.result()
        
        print(f"Summary: Found {len(amis)} AMIs across all regions")

if __name__ == "__main__":
    describe_ec2_amis()