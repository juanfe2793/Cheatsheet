# Describe DMS replication task

This script retrieve information about DMS replication tasks in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_dms_instances_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the DMS replica service in the specified region, and then uses the `describe_dms_instances` method to retrieve information about all DMS replication tasks in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 dms replication db_replication_tasks in region ap-south-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region eu-north-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region eu-west-3
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region eu-west-2
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region eu-west-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region ap-northeast-3
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region ap-northeast-2
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region ca-central-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region ap-northeast-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region sa-east-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region ap-southeast-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region ap-southeast-2
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region eu-central-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region us-east-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region us-east-2
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region us-west-1
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Found 0 dms replication db_replication_tasks in region us-west-2
+------------+--------+--------+
| Identifier | Status | Region |
+------------+--------+--------+
+------------+--------+--------+
Summary: Found 0 dms replication db_replication_tasks across all regions


```
