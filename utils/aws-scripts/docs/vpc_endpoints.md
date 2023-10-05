# Describe VPC Endpoint

This script retrieve information about VPC Endpoints in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_vpc_endpoint_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_dhcp` method to retrieve information about all VPC Endpoints in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 VPC endpoints in region ap-south-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region eu-north-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region eu-west-3
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region eu-west-2
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 2 VPC endpoints in region eu-west-1
+------------------------+---------------------------------------------------------+-----------+
|    VPC Endpoint ID     |                       Service Name                      |   Region  |
+------------------------+---------------------------------------------------------+-----------+
| vpce-12345678910       | com.amazonaws.vpce.eu-west-1.vpce-svc-12345678910       | eu-west-1 |
| vpce-12345678910       | com.amazonaws.vpce.eu-west-1.vpce-svc-12345678910       | eu-west-1 |
+------------------------+---------------------------------------------------------+-----------+
Found 0 VPC endpoints in region ap-northeast-3
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region ap-northeast-2
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region ap-northeast-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region ca-central-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region sa-east-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region ap-southeast-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region ap-southeast-2
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region eu-central-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region us-east-1
+------------------------+---------------------------------------------------------+-----------+
|    VPC Endpoint ID     |                       Service Name                      |   Region  |
+------------------------+---------------------------------------------------------+-----------+
+------------------------+---------------------------------------------------------+-----------+
Found 0 VPC endpoints in region us-east-2
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region us-west-1
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Found 0 VPC endpoints in region us-west-2
+-----------------+--------------+--------+
| VPC Endpoint ID | Service Name | Region |
+-----------------+--------------+--------+
+-----------------+--------------+--------+
Summary: Found 0 endpoints across all regions

```
