# Describe EC2 ami

This script retrieve information about EC2 AMIs in all regions. This script only consider Self Owner Images. **AWS or public Images aren't included.**

Here's a brief overview of what the script does:

* Defines a function called `describe_ec2_amis_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_amis` method to retrieve information about all EC2 AMIs in that region.
* The function then prints out the total number of amis found in the region, and loops through each ami to print out its name, ID, and ami type.
* If an error occurs while trying to retrieve the ami information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of amis in all the regions.

## Example output

```shell
Found 0 AMIs in region ap-south-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region eu-north-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region eu-west-3
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region eu-west-2
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region eu-west-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region ap-northeast-3
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region ap-northeast-2
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region ca-central-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region ap-northeast-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region sa-east-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region ap-southeast-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region ap-southeast-2
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region eu-central-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region us-east-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region us-east-2
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region us-west-1
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Found 0 AMIs in region us-west-2
+--------+----------+--------+
| AMI ID | AMI Name | Region |
+--------+----------+--------+
+--------+----------+--------+
Summary: Found 0 AMIs across all regions

```
