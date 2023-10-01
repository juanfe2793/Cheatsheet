# This python script will describe all EC2 instances in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

# Before listing the EKS cluster, we need to check if we have permission to list EKS clusters in all regions.
# If we don't have permission to list EKS Clusters in a region, we will get the following error:
# botocore.exceptions.ClientError: An error occurred (UnauthorizedOperation) when calling the DescribeInstances operation: You are not authorized to perform this operation.

def check_list_clusters_permission(region_name):
    eksconn = boto3.client("eks", region_name=region_name)
    try:
        eksconn.list_clusters()
    except eksconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to describe/list EKS clusters")
            return False
    return True

# List EKS Clusters in a region
def list_eks_clusters_by_region(region_name):
    try:
        eksconn = boto3.client("eks", region_name=region_name)
        cluster_names = eksconn.list_clusters()["clusters"]
        print(f"Found {len(cluster_names)} EKS clusters in the region {region_name}")

        # Create a table with the following columns: Cluster Name, Kubernetes Version, Region
        table = PrettyTable(["Cluster Name", "Kubernetes Version", "Region"])

        for cluster in cluster_names:
            cluster_info = eksconn.describe_cluster(name=cluster)["cluster"]
            k8s_version = cluster_info["version"]
            
            # Add a row to the table for each instance
            table.add_row([cluster, k8s_version, region_name])

        print(table)
        
        return cluster_names
    except Exception as e:
        print(f"The following error occurs trying to List EKS clusters in the region: {region_name}: {e}")
        return []


def list_eks_clusters():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]: # using EC2 client to get all available regions.
                region_name = region["RegionName"]
                if check_list_clusters_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(list_eks_clusters_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                cluster_names = future.result()
        
        print(f"Summary: Found {len(cluster_names)} EKS clusters across all regions")

if __name__ == "__main__":
    list_eks_clusters()