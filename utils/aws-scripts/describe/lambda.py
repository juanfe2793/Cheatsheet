# This python script will describe all EC2 lambda in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2", "us-east-1")

# Check if we have permission to list the lambda function in a region
def check_list_lambda_permission(region_name):
    lambdaconn = boto3.client("lambda", region_name=region_name)
    try:
        lambdaconn.list_functions()
    except lambdaconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to list lambda functions in the region")
            return False
    return True

# Describe EC2 lambda in a region
def list_lambda_function_by_region(region_name):
    try:
        lambdaconn = boto3.client("lambda", region_name=region_name)
        functions = lambdaconn.list_functions()["Functions"]
        print(f"Found {len(functions)} lambda functions in region {region_name}")

        # Create a table with the following columns: Function Name, Function Runtime, Region
        table = PrettyTable(["Function Name", "Function Runtime", "Region"])

        for function in functions:
            function_name = function["FunctionName"]
            function_runtime = function["Runtime"]
            
            # Add a row to the table for each instance
            table.add_row([function_name, function_runtime, region_name])

        print(table)
        
        return functions
    except Exception as e:
        print(f"The following error occurs trying to listing the lambda functions in region: {region_name}: {e}")
        return []


def list_lambda_functions():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_list_lambda_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(list_lambda_function_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                functions = future.result()
        
        print(f"Summary: Found {len(functions)} lambda functions across all regions")

if __name__ == "__main__":
    list_lambda_functions()