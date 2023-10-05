# Describe DHCP option set

This script retrieve information about DHCP option sets in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_dhcp_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_dhcp` method to retrieve information about all DHCP option sets in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 1 options sets in region ap-south-1
+------------------------+------------+
|     Option set ID      |   Region   |
+------------------------+------------+
| dopt-12345678910       | ap-south-1 |
+------------------------+------------+
Found 1 options sets in region eu-north-1
+------------------------+------------+
|     Option set ID      |   Region   |
+------------------------+------------+
+------------------------+------------+
Found 1 options sets in region eu-west-3
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Found 1 options sets in region eu-west-2
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Found 1 options sets in region eu-west-1
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Found 1 options sets in region ap-northeast-3
+------------------------+----------------+
|     Option set ID      |     Region     |
+------------------------+----------------+
+------------------------+----------------+
Found 1 options sets in region ap-northeast-2
+------------------------+----------------+
|     Option set ID      |     Region     |
+------------------------+----------------+
+------------------------+----------------+
Found 1 options sets in region ap-northeast-1
+------------------------+----------------+
|     Option set ID      |     Region     |
+------------------------+----------------+
+------------------------+----------------+
Found 1 options sets in region ca-central-1
+------------------------+--------------+
|     Option set ID      |    Region    |
+------------------------+--------------+
+------------------------+--------------+
Found 1 options sets in region sa-east-1
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Found 1 options sets in region ap-southeast-1
+------------------------+----------------+
|     Option set ID      |     Region     |
+------------------------+----------------+
+------------------------+----------------+
Found 1 options sets in region ap-southeast-2
+------------------------+----------------+
|     Option set ID      |     Region     |
+------------------------+----------------+
+------------------------+----------------+
Found 1 options sets in region eu-central-1
+------------------------+--------------+
|     Option set ID      |    Region    |
+------------------------+--------------+
+------------------------+--------------+
Found 1 options sets in region us-east-1
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Found 1 options sets in region us-east-2
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Found 1 options sets in region us-west-1
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Found 1 options sets in region us-west-2
+------------------------+-----------+
|     Option set ID      |   Region  |
+------------------------+-----------+
+------------------------+-----------+
Summary: Found 1 buckets across all regions
```
