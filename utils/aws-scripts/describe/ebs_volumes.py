# This python script will describe all EC2 volumes in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

def check_describe_volumes_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_volumes()
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe EBS volumes")
            return False
    return True

# Describe EBS volumes in a region
def describe_ebs_volumes_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        volumes = ec2conn.describe_volumes()["Volumes"]
        print(f"Found {len(volumes)} EBS volumes in region {region_name}")

        # Create a table with the following columns: Volume ID, Volume Name, Volume Type and Region
        table = PrettyTable(["Volume ID", "Volume Name", "Volume Type", "Region"])

        for volume in volumes:
            volume_id = volume["VolumeId"]
            volume_type = volume["VolumeType"]
            volume_name = ""
            if "Tags" in volume:
                for tag in volume["Tags"]:
                    if tag["Key"] == "Name":
                        volume_name = tag["Value"]
                        break
            
            # Add a row to the table for each volume
            table.add_row([volume_id, volume_name, volume_type, region_name])

        print(table)
        
        return volumes
    except Exception as e:
        print(f"The following error occurs trying to describe EC2 volumes in region: {region_name}: {e}")
        return []


def describe_ebs_volumes():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_volumes_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_ebs_volumes_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                volumes = future.result()
        
        print(f"Summary: Found {len(volumes)} EBS volumes across all regions")

if __name__ == "__main__":
    describe_ebs_volumes()