# This python script will list all backup instances in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2","us-east-1")

def check_list_backup_plan_permission(region_name):
    backupconn = boto3.client("backup", region_name=region_name)
    try:
        backupconn.list_backup_plans()
    except backupconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to list backup plans")
            return False
    return True

# list backup instances in a region
def list_backup_plans_by_region(region_name):
    try:
        backupconn = boto3.client("backup", region_name=region_name)
        plans = backupconn.list_backup_plans()["BackupPlansList"]
        print(f"Found {len(plans)} Backup plans in region {region_name}")

        # Create a table with the following columns: Backup Plan Name, Last Runtime, Region
        table = PrettyTable(["Backup Plan Name", "Last Runtime", "Region"])

        for plan in plans:
            plan_name = plan["BackupPlanName"]
            last_runtime = backupconn.list_backup_runs(BackupPlanId=plan["BackupPlanId"])["BackupRuns"][0]["CreationTime"]
            
            # Add a row to the table for each backup plan
            table.add_row([plan_name, last_runtime, region_name])

        print(table)
        
        return plans
    except Exception as e:
        print(f"The following error occurs trying to list backup plans in region: {region_name}: {e}")
        return []


def list_backup_plans():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_list_backup_plan_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(list_backup_plans_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                plans = future.result()
        
        print(f"Summary: Found {len(plans)} backup plans across all regions")

if __name__ == "__main__":
    list_backup_plans()