# Describe DMS replica endpoint

This script retrieve information about DMS replica endpoints in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_dms_endpoints_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the DMS replica service in the specified region, and then uses the `describe_dms_endpoints` method to retrieve information about all DMS replica endpoints in that region.
* The function then prints out the total number of endpoints found in the region, and loops through each endpoint to print out its name, ID, and endpoint type.
* If an error occurs while trying to retrieve the endpoint information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of endpoints in all the regions.

## Example output

```shell
Found 0 dms replication endpoints in region ap-south-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region eu-north-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region eu-west-3
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region eu-west-2
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region eu-west-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region ap-northeast-3
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region ap-northeast-2
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region ap-northeast-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region ca-central-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region sa-east-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region ap-southeast-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region ap-southeast-2
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region eu-central-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region us-east-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region us-east-2
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region us-west-1
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Found 0 dms replication endpoints in region us-west-2
+------+-------+----------------+--------+
| Name | Class | Engine Version | Region |
+------+-------+----------------+--------+
+------+-------+----------------+--------+
Summary: Found 0 dms replication endpoints across all regions

```
