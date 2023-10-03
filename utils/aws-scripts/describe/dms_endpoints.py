# This python script will describe all dms endpoints in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

def check_describe_dms_endpoint_permission(region_name):
    dmsconn = boto3.client("dms", region_name=region_name)
    try:
        dmsconn.describe_endpoints()
    except dmsconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe dms replica endpoints")
            return False
    return True

# describe dms endpoints in a region
def describe_dms_endpoints_by_region(region_name):
    try:
        dmsconn = boto3.client("dms", region_name=region_name)
        endpoints = dmsconn.describe_endpoints()["Endpoints"]
        print(f"Found {len(endpoints)} dms replication endpoints in region {region_name}")

        # Create a table with the following columns: Name, Type, Engine Version, Server Name, Region
        table = PrettyTable(["Name", "Type", "Engine Version", "Server Name", "Region"])

        for endpoint in endpoints:
            name = endpoint["EndpointIdentifier"]
            endpoint_type = endpoint["EndpointType"]
            engine_version = endpoint["EngineVersion"]
            server_name = endpoint["ServerName"]
            
            # Add a row to the table for each DMS endpoint
            table.add_row([name, endpoint_type, engine_version, server_name, region_name])

        print(table)
        
        return endpoints
    except Exception as e:
        print(f"The following error occurs trying to describe dms replication endpoints in region: {region_name}: {e}")
        return []


def describe_dms_endpoints():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_dms_endpoint_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_dms_endpoints_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                endpoints = future.result()
        
        print(f"Summary: Found {len(endpoints)} dms replication endpoints across all regions")

if __name__ == "__main__":
    describe_dms_endpoints()