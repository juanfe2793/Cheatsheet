# Describe RDS instance

This script retrieve information about RDS instances in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_RDS_instances_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the RDS service in the specified region, and then uses the `describe_instances` method to retrieve information about all RDS instances in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 RDS db_instances in region ap-south-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region eu-north-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region eu-west-3
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region eu-west-2
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region eu-west-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region ap-northeast-3
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region ap-northeast-2
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region ca-central-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region ap-northeast-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region sa-east-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region ap-southeast-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region ap-southeast-2
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region eu-central-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region us-east-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region us-east-2
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region us-west-1
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Found 0 RDS db_instances in region us-west-2
+---------------+------------------+-----------+--------+
| DB Identifier | DB Instance Type | DB Engine | Region |
+---------------+------------------+-----------+--------+
+---------------+------------------+-----------+--------+
Summary: Found 0 RDS db_instance across all regions

```
