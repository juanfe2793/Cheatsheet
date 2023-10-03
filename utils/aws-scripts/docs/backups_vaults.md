# Describe backup vault

This script retrieve information about backup vaults in all regions. Here's a brief overview of what the script does:

* Defines a function called `list_backup_vaults_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `list_backup_vaults` method to retrieve information about all backup vaults in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 Backup vaults in region ap-south-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region eu-north-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region eu-west-3
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region eu-west-2
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region eu-west-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region ap-northeast-3
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region ap-northeast-2
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region ap-northeast-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region ca-central-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region sa-east-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region ap-southeast-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region ap-southeast-2
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region eu-central-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 1 Backup vaults in region us-east-1
+-------------------+-----------------+-----------+
| Backup Vault Name | Recovery Points |   Region  |
+-------------------+-----------------+-----------+
|      Default      |        0        | us-east-1 |
+-------------------+-----------------+-----------+
Found 0 Backup vaults in region us-east-2
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region us-west-1
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Found 0 Backup vaults in region us-west-2
+-------------------+-----------------+--------+
| Backup Vault Name | Recovery Points | Region |
+-------------------+-----------------+--------+
+-------------------+-----------------+--------+
Summary: Found 0 instances across all regions

```
