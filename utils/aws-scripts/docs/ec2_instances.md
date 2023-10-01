# Describe EC2 instance

This script retrieve information about EC2 instances in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_ec2_instances_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_instances` method to retrieve information about all EC2 instances in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 instances in region ap-south-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region eu-north-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region eu-west-3
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region eu-west-2
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 3 instances in region eu-west-1
+---------------------+---------------+-----------+
|     Instance ID     | Instance Type |   Region  |
+---------------------+---------------+-----------+
| i-12345678910 |  r6i.4xlarge  | eu-west-1 |
| i-12345678910 |  r6i.4xlarge  | eu-west-1 |
| i-12345678910 |  r6i.4xlarge  | eu-west-1 |
+---------------------+---------------+-----------+
Found 0 instances in region ap-northeast-3
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region ap-northeast-2
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region ap-northeast-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region ca-central-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region sa-east-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region ap-southeast-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region ap-southeast-2
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region eu-central-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region us-east-2
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 instances in region us-west-1
+-------------+---------------+--------+
| Instance ID | Instance Type | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 4 instances in region us-east-1
+---------------------+---------------+-----------+
|     Instance ID     | Instance Type |   Region  |
+---------------------+---------------+-----------+
| i-12345678910 |  m6i.2xlarge  | us-east-1 |
| i-12345678910 |  r6i.2xlarge  | us-east-1 |
| i-12345678910 |  r6i.4xlarge  | us-east-1 |
| i-12345678910 |  r6i.4xlarge  | us-east-1 |
+---------------------+---------------+-----------+
Found 5 instances in region us-west-2
+---------------------+---------------+-----------+
|     Instance ID     | Instance Type |   Region  |
+---------------------+---------------+-----------+
| i-12345678910 |    m5.large   | us-west-2 |
| i-12345678910 |    m5.large   | us-west-2 |
| i-12345678910 |  r6i.4xlarge  | us-west-2 |
| i-12345678910 |  r6i.2xlarge  | us-west-2 |
| i-12345678910 |  r6i.2xlarge  | us-west-2 |
+---------------------+---------------+-----------+
Summary: Found 12 instances across all regions
```
