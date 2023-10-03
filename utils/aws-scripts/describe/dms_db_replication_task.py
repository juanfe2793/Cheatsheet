# This python script will describe all dms db_replication_tasks in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

def check_describe_dms_db_replication_task_permission(region_name):
    dmsconn = boto3.client("dms", region_name=region_name)
    try:
        dmsconn.describe_replication_tasks()
    except dmsconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe dms db_replication_tasks")
            return False
    return True

# describe dms db_replication_tasks in a region
def describe_dms_db_replication_tasks_by_region(region_name):
    try:
        dmsconn = boto3.client("dms", region_name=region_name)
        tasks = dmsconn.describe_replication_tasks()["ReplicationTasks"]
        print(f"Found {len(tasks)} dms replication db_replication_tasks in region {region_name}")

        # Create a table with the following columns: Identifier, Status, Region
        table = PrettyTable(["Identifier", "Status", "Region"])

        for task in tasks:
            identifier = task["ReplicationTaskIdentifier"]
            status = task["Status"]
            
            # Add a row to the table for each DMS replication task
            table.add_row([identifier, status, region_name])

        print(table)
        
        return tasks
    except Exception as e:
        print(f"The following error occurs trying to describe dms replication db_replication_tasks in region: {region_name}: {e}")
        return []


def describe_dms_db_replication_tasks():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_dms_db_replication_task_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_dms_db_replication_tasks_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                tasks = future.result()
        
        print(f"Summary: Found {len(tasks)} dms replication db_replication_tasks across all regions")

if __name__ == "__main__":
    describe_dms_db_replication_tasks()