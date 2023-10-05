import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

elastic_ips = {}

def check_describe_address_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_addresses(AllocationIds=["test"])
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to release Elastic IPs")
            return False
    return True

def describe_eips_in_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        addresses = ec2conn.describe_addresses(
            Filters=[{"Name": "domain", "Values": ["vpc"]}])["Addresses"]
        print(f"Found a Total of **{len(addresses)}** Elastic IPs in {region_name}")
        # Create a table with the following columns: Elastic Public IP, Allocation ID, Region
        table = PrettyTable(["Elastic Public IP", "Allocation ID", "Region"])

        for address in addresses:
            public_ipv4 = address['PublicIp']
            allocation_id = address['AllocationId']
            
            # Add a row to the table for each instance
            table.add_row([public_ipv4, allocation_id, region_name])

        print(table)
        
        return addresses
    except Exception as e:
        print(f"The following error occurs trying to describe Elastic IPs in region: {region_name}: {e}")
        return []

def describe_elastic_ips():

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for region in ec2.meta.client.describe_regions()["Regions"]:
            region_name = region["RegionName"]
            if check_describe_address_permission(region_name): # Check if we have permission to release EIPs.
              futures.append(executor.submit(describe_eips_in_region, region_name))
        for future in concurrent.futures.as_completed(futures):
            elastic_ips = future.result()

    print(f"Summary: Found {len(elastic_ips)} Elastic IPs across all regions:")

if __name__ == "__main__":
    describe_elastic_ips()