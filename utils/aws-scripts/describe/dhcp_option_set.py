# This python script will describe all EC2 buckets in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")



def check_describe_dhcp_permission(region_name):
    dhcpconn = boto3.client("ec2", region_name=region_name)
    try:
        dhcpconn.describe_dhcp_options()["DhcpOptions"]
    except dhcpconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe DHCP options")
            return False
    return True

# Describe DHCP options set in a region
def describe_dhcp_by_region(region_name):
    try:
        dhcpconn = boto3.client("ec2", region_name=region_name)
        option_sets = dhcpconn.describe_dhcp_options()["DhcpOptions"]
        print(f"Found {len(option_sets)} options sets in region {region_name}")

        # Create a table with the following columns: ID, Region
        table = PrettyTable(["Option set ID", "Region"])

        for option_set in option_sets:
            option_set_id = option_set['DhcpOptionsId']
            
            # Add a row to the table for each option set
            table.add_row([option_set_id, region_name])

        print(table)
        
        return option_sets
    except Exception as e:
        print(f"The following error occurs trying to describe the DHCP option set: {region_name}: {e}")
        return []


def describe_dhcp():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_dhcp_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_dhcp_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                buckets = future.result()
        
        print(f"Summary: Found {len(buckets)} buckets across all regions")

if __name__ == "__main__":
    describe_dhcp()