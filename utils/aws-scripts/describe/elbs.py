# This python script will describe all EC2 buckets in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

def check_describe_elb_permission(region_name):
    elbconn = boto3.client("elbv2", region_name=region_name)
    try:
        elbconn.describe_load_balancers()["LoadBalancers"]
    except elbconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe Elastic Load Balancers")
            return False
    return True

# Describe EC2 buckets in a region
def describe_elb_by_region(region_name):
    try:
        elbconn = boto3.client("elbv2", region_name=region_name)
        load_balancers = elbconn.describe_load_balancers()["LoadBalancers"]
        print(f"Found {len(load_balancers)} Elastic Load Balancers in region {region_name}")

        # Create a table with the following columns: Name, Type, Region
        table = PrettyTable(["Name", "Type", "Region"])

        for load_balancer in load_balancers:
            load_balancer_name = load_balancer['LoadBalancerName']
            load_balancer_type = load_balancer['Type']
            
            # Add a row to the table for each load balancer
            table.add_row([load_balancer_name, load_balancer_type, region_name])

        print(table)
        
        return load_balancers
    except Exception as e:
        print(f"The following error occurs trying to load_balancers in region: {region_name}: {e}")
        return []


def describe_elb():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_elb_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_elb_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                load_balancers = future.result()
        
        print(f"Summary: Found {len(load_balancers)} load_balancers across all regions")

if __name__ == "__main__":
    describe_elb()