# Describe Security Group

This script retrieve information about Security Groups in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_sec_group_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_dhcp` method to retrieve information about all Security Groups in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 1 security groups in region ap-south-1
+----------------------+------------+
|  Security Group ID   |   Region   |
+----------------------+------------+
| sg-049d57839d2e1d9c8 | ap-south-1 |
+----------------------+------------+
Found 1 security groups in region eu-north-1
+----------------------+------------+
|  Security Group ID   |   Region   |
+----------------------+------------+
+----------------------+------------+
Found 1 security groups in region eu-west-3
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
+----------------------+-----------+
Found 1 security groups in region eu-west-2
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
+----------------------+-----------+
Found 7 security groups in region eu-west-1
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
+----------------------+-----------+
Found 1 security groups in region ap-northeast-3
+----------------------+----------------+
|  Security Group ID   |     Region     |
+----------------------+----------------+
+----------------------+----------------+
Found 1 security groups in region ap-northeast-2
+----------------------+----------------+
|  Security Group ID   |     Region     |
+----------------------+----------------+
+----------------------+----------------+
Found 1 security groups in region ap-northeast-1
+----------------------+----------------+
|  Security Group ID   |     Region     |
+----------------------+----------------+
+----------------------+----------------+
Found 1 security groups in region ca-central-1
+----------------------+--------------+
|  Security Group ID   |    Region    |
+----------------------+--------------+
+----------------------+--------------+
Found 1 security groups in region sa-east-1
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
+----------------------+-----------+
Found 1 security groups in region ap-southeast-1
+----------------------+----------------+
|  Security Group ID   |     Region     |
+----------------------+----------------+
+----------------------+----------------+
Found 1 security groups in region ap-southeast-2
+----------------------+----------------+
|  Security Group ID   |     Region     |
+----------------------+----------------+
+----------------------+----------------+
Found 1 security groups in region eu-central-1
+----------------------+--------------+
|  Security Group ID   |    Region    |
+----------------------+--------------+
+----------------------+--------------+
Found 1 security groups in region us-east-2
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
+----------------------+-----------+
Found 82 security groups in region us-east-1
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
+----------------------+-----------+
Found 1 security groups in region us-west-1
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
| sg-12345678910       | us-west-1 |
+----------------------+-----------+
Found 0 security groups in region us-west-2
+----------------------+-----------+
|  Security Group ID   |   Region  |
+----------------------+-----------+
+----------------------+-----------+
Summary: Found 38 security_groups across all regions

```
