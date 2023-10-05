# This python script will describe all EC2 db_instance in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

def check_describe_db_instance_permission(region_name):
    rdsconn = boto3.client("rds", region_name=region_name)
    try:
        rdsconn.describe_db_instances()
    except rdsconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe RDS db_instances")
            return False
    return True

# Describe RDS db_instance in a region
def describe_db_instance_by_region(region_name):
    try:
        rdsconn = boto3.client("rds", region_name=region_name)
        db_instances = rdsconn.describe_db_instances()["DBInstances"]
        print(f"Found {len(db_instances)} RDS db_instances in region {region_name}")

         # Create a table with the following columns: DB Identifier, DB Instance Type, DB Engine, Region
        table = PrettyTable(["DB Identifier", "DB Instance Type", "DB Engine", "Region"])

        for instance in db_instances:
            db_identifier = instance["DBInstanceIdentifier"]
            db_instance_type = instance["DBInstanceClass"]
            db_engine = instance["Engine"]
            
            # Add a row to the table for each RDS instance
            table.add_row([db_identifier, db_instance_type, db_engine, region_name])

        print(table)
        
        return db_instances
    except Exception as e:
        print(f"The following error occurs trying to describe RDS db_instance in region: {region_name}: {e}")
        return []


def describe_rds_db_instance():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_db_instance_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_db_instance_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                db_instances = future.result()
        
        print(f"Summary: Found {len(db_instances)} RDS db_instance across all regions")

if __name__ == "__main__":
    describe_rds_db_instance()