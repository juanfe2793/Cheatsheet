# This python script will list all dynamodb tables in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

def check_list_dynamodb_table_permission(region_name):
    dynamodbconn = boto3.client("dynamodb", region_name=region_name)
    try:
        dynamodbconn.list_tables()
    except dynamodbconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to list dynamodb tables")
            return False
    return True

# list dynamodb tables in a region
def list_dynamodb_tables_by_region(region_name):
    try:
        dynamodbconn = boto3.client("dynamodb", region_name=region_name)
        tables = dynamodbconn.list_tables()["TableNames"]
        print(f"Found {len(tables)} dynamodb tables in region {region_name}")

        # Create a table with the following columns: Name, Status, Total Size, Region
        table = PrettyTable(["Name", "Status", "Total Size", "Region"])

        for table in tables:
            table_description = dynamodbconn.describe_table(TableName=table)["Table"]
            name = table_description["TableName"]
            status = table_description["TableStatus"]
            total_size = table_description["TableSizeBytes"]
            
            # Add a row to the table for each DynamoDB table
            table.add_row([name, status, total_size, region_name])

        print(table)
        
        return tables
    except Exception as e:
        print(f"The following error occurs trying to list dynamodb tables in region: {region_name}: {e}")
        return []


def list_dynamodb_tables():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_list_dynamodb_table_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(list_dynamodb_tables_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                tables = future.result()
        
        print(f"Summary: Found {len(tables)} dynamodb replication tables across all regions")

if __name__ == "__main__":
    list_dynamodb_tables()