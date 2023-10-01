# This python script will describe all launch_templates in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

# Before describing the Launch templates in a region, we need to check if we have permission to describe launch templates.
# If we don't have permission to describe launch templates in a region, we will get the following error:
# botocore.exceptions.ClientError: An error occurred (UnauthorizedOperation) when calling the DescribeInstances operation: You are not authorized to perform this operation.

def check_describe_launch_template_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.describe_launch_templates()
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe the Launch Templates")
            return False
    return True

# Describe Launch Templates in a region
def describe_launch_templates_by_region(region_name):
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        launch_templates = ec2conn.describe_launch_templates()["LaunchTemplates"]
        print(f"Found {len(launch_templates)} launch templates in the region {region_name}")

        # Create a table with the following columns: Launch Template ID, Launch Template Name, Default Version, Region
        table = PrettyTable(["Launch Template ID", "Launch Template Name", "Default Version", "Region"])

        for launch_template in launch_templates:
            lt_id = launch_template["LaunchTemplateId"]
            lt_name = launch_template["LaunchTemplateName"]
            default_version = launch_template["DefaultVersionNumber"]
            
            # Add a row to the table for each Launch Template
            table.add_row([lt_id, lt_name, default_version, region_name])

        print(table)
        
        return launch_templates
    except Exception as e:
        print(f"The following error occurs trying to describe Launch Templates in region: {region_name}: {e}")
        return []


def describe_launch_templates():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_launch_template_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_launch_templates_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                launch_templates = future.result()
        
        print(f"Summary: Found {len(launch_templates)} instances across all regions")

if __name__ == "__main__":
    describe_launch_templates()