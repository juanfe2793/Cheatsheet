# Describe launch templates

This script retrieve information about launch templates across all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_launch_templates_by_region` that takes a single argument, `region_name`. This function uses the `boto3` library to create a client for the EC2 service in the specified region, and then uses the `describe_launch_templates` method to retrieve information about all launch templates in that region.
* The function then loops through each Launch Template and retrieves additional information about the launc template. It then adds the Launch Template information to a list.
* If an error occurs while trying to retrieve the Launch Template information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 launch templates in the region ap-south-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region eu-north-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region eu-west-3
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region eu-west-2
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 1 launch templates in the region eu-west-1
+----------------------+------------------------------------------+-----------------+-----------+
|  Launch Template ID  |           Launch Template Name           | Default Version |   Region  |
+----------------------+------------------------------------------+-----------------+-----------+
| lt-12345678910       | eks-12345678910                          |        1        | eu-west-1 |
+----------------------+------------------------------------------+-----------------+-----------+
Found 0 launch templates in the region ap-northeast-3
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region ap-northeast-2
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region ap-northeast-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region ca-central-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region sa-east-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region ap-southeast-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region ap-southeast-2
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region eu-central-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 1 launch templates in the region us-east-1
+----------------------+------------------------------------------+-----------------+-----------+
|  Launch Template ID  |           Launch Template Name           | Default Version |   Region  |
+----------------------+------------------------------------------+-----------------+-----------+
| lt-12345678910       | eks-12345678910                          |        1        | eu-east-1 |
+----------------------+------------------------------------------+-----------------+-----------+
Found 0 launch templates in the region us-east-2
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 0 launch templates in the region us-west-1
+--------------------+----------------------+-----------------+--------+
| Launch Template ID | Launch Template Name | Default Version | Region |
+--------------------+----------------------+-----------------+--------+
+--------------------+----------------------+-----------------+--------+
Found 1 launch templates in the region us-west-2
+----------------------+-----------------------------------------------+-----------------+-----------+
|  Launch Template ID  |              Launch Template Name             | Default Version |   Region  |
+----------------------+-----------------------------------------------+-----------------+-----------+
| lt-12345678910       | eks-12345678910                               |        1        | eu-west-2 |
+----------------------+-----------------------------------------------+-----------------+-----------+
Summary: Found 3 instances across all regions

```
