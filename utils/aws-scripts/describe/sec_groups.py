# This python script will describe all EC2 security_groups in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")



def check_describe_sec_group_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_security_groups()["SecurityGroups"]
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe Security Groups")
            return False
    return True

# Describe EC2 security_groups in a region
def describe_sec_group_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        security_groups = ec2conn.describe_security_groups()["SecurityGroups"]
        print(f"Found {len(security_groups)} security groups in region {region_name}")

        # Create a table with the following columns: Security Group ID, Region
        table = PrettyTable(["Security Group ID", "Region"])

        for security_group in security_groups:
            security_group_id = security_group['GroupId']
            
            # Add a row to the table for each security group
            table.add_row([security_group_id, region_name])

        print(table)
        
        return security_groups
    except Exception as e:
        print(f"The following error occurs trying to describe Security Groups in region: {region_name}: {e}")
        return []


def describe_sec_groups():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_sec_group_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_sec_group_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                security_groups = future.result()
        
        print(f"Summary: Found {len(security_groups)} security_groups across all regions")

if __name__ == "__main__":
    describe_sec_groups()