# This python script will describe all dms instances in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

def check_describe_dms_instance_permission(region_name):
    dmsconn = boto3.client("dms", region_name=region_name)
    try:
        dmsconn.describe_replication_instances()
    except dmsconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe dms replica instances")
            return False
    return True

# describe dms instances in a region
def describe_dms_instances_by_region(region_name):
    try:
        dmsconn = boto3.client("dms", region_name=region_name)
        instances = dmsconn.describe_replication_instances()["ReplicationInstances"]
        print(f"Found {len(instances)} dms replication instances in region {region_name}")

        # Create a table with the following columns: Name, Class, Engine Version, Region
        table = PrettyTable(["Name", "Class", "Engine Version", "Region"])

        for instance in instances:
            name = instance["ReplicationInstanceIdentifier"]
            instance_class = instance["ReplicationInstanceClass"]
            engine_version = instance["EngineVersion"]
            
            # Add a row to the table for each DMS replication instance
            table.add_row([name, instance_class, engine_version, region_name])

        print(table)
        
        return instances
    except Exception as e:
        print(f"The following error occurs trying to describe dms replication instances in region: {region_name}: {e}")
        return []


def describe_dms_instances():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_dms_instance_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_dms_instances_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                plans = future.result()
        
        print(f"Summary: Found {len(plans)} dms replication instances across all regions")

if __name__ == "__main__":
    describe_dms_instances()