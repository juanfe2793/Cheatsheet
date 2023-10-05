# This python script will describe all EC2 endpoints in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")



def check_describe_vpc_endpoints_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_vpc_endpoints()["VpcEndpoints"]
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe VPC endpoints")
            return False
    return True

# Describe EC2 endpoints in a region
def describe_vpc_endpoint_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        endpoints = ec2conn.describe_vpc_endpoints()["VpcEndpoints"]
        print(f"Found {len(endpoints)} VPC endpoints in region {region_name}")

        # Create a table with the following columns: VPC Endpoint ID, Service Name, Region
        table = PrettyTable(["VPC Endpoint ID", "Service Name", "Region"])

        for endpoint in endpoints:
            endpoint_id = endpoint['VpcEndpointId']
            service_name = endpoint['ServiceName']
            
            # Add a row to the table for each endpoint
            table.add_row([endpoint_id, service_name, region_name])

        print(table)
        
        return endpoints
    except Exception as e:
        print(f"The following error occurs trying to describe VPC Endpoints in region: {region_name}: {e}")
        return []


def describe_vpc_endpoints():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_vpc_endpoints_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_vpc_endpoint_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                endpoints = future.result()
        
        print(f"Summary: Found {len(endpoints)} endpoints across all regions")

if __name__ == "__main__":
    describe_vpc_endpoints()