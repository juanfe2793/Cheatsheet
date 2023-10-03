# This python script will describe all EC2 ecr_repository in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

# Before describing the EC2 ecr_repository, we need to check if we have permission to describe EC2 ecr_repository in all regions.
# If we don't have permission to describe EC2 ecr_repository in a region, we will get the following error:
# botocore.exceptions.ClientError: An error occurred (UnauthorizedOperation) when calling the Describeecr_repository operation: You are not authorized to perform this operation.

def check_describe_ecr_repository_permission(region_name):
    ecrconn = boto3.client("ecr", region_name=region_name)
    try:
        ecrconn.describe_repositories()
    except ecrconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe ECR repositories")
            return False
    return True

# Describe ECR repositories in a region
def describe_ecr_repository_by_region(region_name):
    try:
        ecrconn = boto3.client("ecr", region_name=region_name)
        repositories = ecrconn.describe_repositories()["repositories"]
        print(f"Found {len(repositories)} ecr repositories in region {region_name}")

        # Create a table with the following columns: Name, Private/Public, Number of Images, Region
        table = PrettyTable(["Name", "Private/Public", "Number of Images", "Region"])

        for repository in repositories:
            name = repository["repositoryName"]
            is_private = repository["repositoryArn"].split(":")[5] == "aws"
            num_images = repository["imageCount"]
            
            # Add a row to the table for each ECR repository
            table.add_row([name, "Private" if is_private else "Public", num_images, region_name])

        print(table)
        
        return repositories
    except Exception as e:
        print(f"The following error occurs trying to describe ECR repositories in region: {region_name}: {e}")
        return []


def describe_ecr_repository():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_describe_ecr_repository_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(describe_ecr_repository_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                repositories = future.result()
        
        print(f"Summary: Found {len(repositories)} ecr_repository across all regions")

if __name__ == "__main__":
    describe_ecr_repository()