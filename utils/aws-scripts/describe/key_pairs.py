# This python script will describe all EC2 key_pairs in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

# Before describing the Key Pairs, we need to check if we have permission to describe the Key pairs in all regions.
# If we don't have permission to describe the key pairs  in a region, we will get the following error:
# botocore.exceptions.ClientError: An error occurred (UnauthorizedOperation) when calling the DescribeKeyPairs operation: You are not authorized to perform this operation.

def check_describe_key_pairs_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_key_pairs()
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe Key Pairs key_pairs")
            return False
    return True

# Describe Key pairs in a region
def describe_key_pairs_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        key_pairs = ec2conn.describe_key_pairs()["KeyPairs"]
        print(f"Found {len(key_pairs)} key pairs in region {region_name}")

        # Create a table with the following columns: Key Pair ID, Key Pair Name, Region
        table = PrettyTable(["Key Pair ID", "Key Pair Name", "Region"])

        for key_pair in key_pairs:
            kp_id = key_pair["KeyPairId"]
            kp_name = key_pair["KeyName"]
            
            # Add a row to the table for each Key Pair
            table.add_row([kp_id, kp_name, region_name])

        print(table)
        
        return key_pairs
    except Exception as e:
        print(f"The following error occurs trying to describe EC2 key_pairs in region: {region_name}: {e}")
        return []


def describe_ec2_key_pairs():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_key_pairs_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_key_pairs_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                key_pairs = future.result()
        
        print(f"Summary: Found {len(key_pairs)} key pairs across all regions")

if __name__ == "__main__":
    describe_ec2_key_pairs()