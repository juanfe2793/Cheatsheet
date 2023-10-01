# Describe backup plan

This script retrieve information about backup plans in all regions. Here's a brief overview of what the script does:

* Defines a function called `list_backup_plans_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `list_backup_plans` method to retrieve information about all backup plans in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 Backup plans in region ap-south-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region eu-north-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region eu-west-3
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region eu-west-2
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region eu-west-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region ap-northeast-3
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region ap-northeast-2
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region ap-northeast-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region ca-central-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region sa-east-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region ap-southeast-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region ap-southeast-2
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region eu-central-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region us-east-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region us-east-2
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region us-west-1
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Found 0 Backup plans in region us-west-2
+------------------+--------------+--------+
| Backup Plan Name | Last Runtime | Region |
+------------------+--------------+--------+
+------------------+--------------+--------+
Summary: Found 0 backup plans across all regions

```
