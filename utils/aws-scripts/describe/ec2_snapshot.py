# This python script will describe all EC2 snapshot in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

def check_describe_snapshot_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_snapshots()
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe EC2 snapshot")
            return False
    return True

# Describe EC2 snapshot in a region
def describe_ec2_snapshot_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        snapshots = ec2conn.describe_snapshots(OwnerIds=["self"])["Snapshots"]
        print(f"Found {len(snapshots)} EC2 snapshots in region {region_name}")

        # Create a table with the following columns: Snapshot ID, Snapshot Name, Volume Size, Region
        table = PrettyTable(["Snapshot ID", "Snapshot Name", "Volume Size", "Region"])

        for snapshot in snapshots:
            snapshot_id = snapshot["SnapshotId"]
            snapshot_name = ""
            volume_size = snapshot["VolumeSize"]
            for tag in snapshot["Tags"]:
                if tag["Key"] == "Name":
                    snapshot_name = tag["Value"]
                    break
            
            # Add a row to the table for each snapshot
            table.add_row([snapshot_id, snapshot_name, volume_size, region_name])

        print(table)
        
        return snapshots
    except Exception as e:
        print(f"The following error occurs trying to describe EC2 snapshot in region: {region_name}: {e}")
        return []


def describe_ec2_snapshot():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_snapshot_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_ec2_snapshot_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                snapshots = future.result()
        
        print(f"Summary: Found {len(snapshots)} snapshot across all regions")

if __name__ == "__main__":
    describe_ec2_snapshot()