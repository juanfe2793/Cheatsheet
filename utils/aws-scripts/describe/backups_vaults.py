# This python script will list all backup instances in all regions

import boto3
import concurrent.futures
from prettytable import PrettyTable

ec2 = boto3.resource("ec2")

def check_list_backup_vault_permission(region_name):
    backupconn = boto3.client("backup", region_name=region_name)
    try:
        backupconn.list_backup_vaults()
    except backupconn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to list backup vaults")
            return False
    return True

# list backup instances in a region
def list_backup_vaults_by_region(region_name):
    try:
        backupconn = boto3.client("backup", region_name=region_name)
        vaults = backupconn.list_backup_vaults()["BackupVaultList"]
        print(f"Found {len(vaults)} Backup vaults in region {region_name}")

        # Create a table with the following columns: Backup Vault Name, Recovery Points, Region
        table = PrettyTable(["Backup Vault Name", "Recovery Points", "Region"])

        for vault in vaults:
            vault_name = vault["BackupVaultName"]
            recovery_points = len(backupconn.list_recovery_points_by_backup_vault(BackupVaultName=vault_name)["RecoveryPoints"])
            
            # Add a row to the table for each backup vault
            table.add_row([vault_name, recovery_points, region_name])

        print(table)
        
        return vaults
    except Exception as e:
        print(f"The following error occurs trying to list backup vaults in region: {region_name}: {e}")
        return []


def list_backup_vaults():
    
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = []
            for region in ec2.meta.client.describe_regions()["Regions"]:
                region_name = region["RegionName"]
                if check_list_backup_vault_permission(region_name): # Check if we have permission to release EIPs.
                  futures.append(executor.submit(list_backup_vaults_by_region, region_name))
                
            for future in concurrent.futures.as_completed(futures):
                vaults = future.result()
        
        print(f"Summary: Found {len(vaults)} backup vaults across all regions")

if __name__ == "__main__":
    list_backup_vaults()