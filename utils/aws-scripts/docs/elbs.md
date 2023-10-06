# Describe ELB

This script retrieve information about ELBs in all regions. Here's a brief overview of what the script does:

* Defines a function called `list_s3_buckets_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `list_s3_buckets` method to retrieve information about all ELBs in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 Elastic Load Balancers in region ap-south-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region eu-north-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region eu-west-3
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region eu-west-2
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 2 Elastic Load Balancers in region eu-west-1
+----------------------------------+-------------+-----------+
|               Name               |   Type      |   Region  |
+----------------------------------+-------------+-----------+
| 12345687910abdcefghijklmopqrstuv | network     | eu-west-1 |
| a1a1cfd3da1fc47d89385cf732fc1df6 | application | eu-west-1 |
+----------------------------------+---------+-----------+
Found 0 Elastic Load Balancers in region ap-northeast-3
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region ap-northeast-2
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region ap-northeast-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region ca-central-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region sa-east-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region ap-southeast-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region ap-southeast-2
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region eu-central-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 41 Elastic Load Balancers in region us-east-1
+----------------------------------+-------------+-----------+
|               Name               |     Type    |   Region  |
+----------------------------------+-------------+-----------+
+----------------------------------+-------------+-----------+
Found 0 Elastic Load Balancers in region us-east-2
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 0 Elastic Load Balancers in region us-west-1
+------+------+--------+
| Name | Type | Region |
+------+------+--------+
+------+------+--------+
Found 9 Elastic Load Balancers in region us-west-2
+----------------------------------+-------------+-----------+
|               Name               |     Type    |   Region  |
+----------------------------------+-------------+-----------+
+----------------------------------+-------------+-----------+
Summary: Found 9 load_balancers across all regions

```
