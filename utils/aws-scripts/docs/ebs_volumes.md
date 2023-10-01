# Describe EBS Volumes

This script retrieve information about EBS Volumes in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_ebs_volumes_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_ebs_volumes` method to retrieve information about all EBS Volumes in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and volume type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 EBS volumes in region ap-south-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region eu-north-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region eu-west-3
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region eu-west-2
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 2 EBS volumes in region eu-west-1
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
|       Volume ID       |                                     Volume Name                                     | Volume Type |   Region  |
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
| vol-12345678910       |                                                                                     |     gp2     | eu-west-1 |
| vol-12345678910       |                     pvc-k8s-dynamic-volume-12345678910                              |     gp3     | eu-west-1 |
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
Found 0 EBS volumes in region ap-northeast-3
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region ap-northeast-2
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region ap-northeast-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region ca-central-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region sa-east-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region ap-southeast-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region ap-southeast-2
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region eu-central-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 2 EBS volumes in region us-east-1
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
|       Volume ID       |                                     Volume Name                                     | Volume Type |   Region  |
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
| vol-12345678910       |                                                                                     |     gp2     | us-east-1 |
| vol-12345678910       |                     pvc-k8s-dynamic-volume-12345678910                              |     gp3     | us-east-1 |
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
Found 0 EBS volumes in region us-east-2
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 0 EBS volumes in region us-west-1
+-----------+-------------+-------------+--------+
| Volume ID | Volume Name | Volume Type | Region |
+-----------+-------------+-------------+--------+
+-----------+-------------+-------------+--------+
Found 2 EBS volumes in region us-west-2
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
|       Volume ID       |                                     Volume Name                                     | Volume Type |   Region  |
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
| vol-12345678910       |                                                                                     |     gp2     | us-west-2 |
| vol-12345678910       |                     pvc-k8s-dynamic-volume-12345678910                              |     gp3     | us-west-2 |
+-----------------------+-------------------------------------------------------------------------------------+-------------+-----------+
Summary: Found 8 EBS volumes across all regions

```
