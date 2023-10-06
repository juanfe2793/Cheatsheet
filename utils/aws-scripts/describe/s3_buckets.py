# This python script will describe all EC2 buckets in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")



def check_list_buckets_permission(region_name):
    s3conn = boto3.client("s3", region_name=region_name)
    try:
        s3conn.list_buckets()["Buckets"]
    except s3conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to list S3 buckets")
            return False
    return True

# Describe EC2 buckets in a region
def list_s3_buckets_by_region(region_name):
    try:
        s3conn = boto3.client("s3", region_name=region_name)
        buckets = s3conn.list_buckets()["Buckets"]
        print(f"Found {len(buckets)} buckets in region {region_name}")

        # Create a table with the following columns: Instance ID, Instance Type, Region
        table = PrettyTable(["Bucket Name", "Region"])

        for bucket in buckets:
            bucket_name = bucket['Name']
            
            # Add a row to the table for each instance
            table.add_row([bucket_name, region_name])

        print(table)
        
        return buckets
    except Exception as e:
        print(f"The following error occurs trying to listing S3 buckets in region: {region_name}: {e}")
        return []


def list_s3_buckets():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_list_buckets_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(list_s3_buckets_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                buckets = future.result()
        
        print(f"Summary: Found {len(buckets)} buckets across all regions")

if __name__ == "__main__":
    list_s3_buckets()