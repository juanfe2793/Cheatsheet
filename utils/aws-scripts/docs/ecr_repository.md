# Describe ecr repository

This script retrieve information about ecr instances in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_ecr_repository_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the ecr service in the specified region, and then uses the `describe_instances` method to retrieve information about all ecr instances in that region.
* The function then prints out the total number of instances found in the region, and loops through each repository to print out its name, ID, and repository type.
* If an error occurs while trying to retrieve the repository information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell
Found 0 ecr repositories in region ap-south-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region eu-north-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region eu-west-3
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region eu-west-2
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region eu-west-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region ap-northeast-3
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region ap-northeast-2
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region ap-northeast-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region ca-central-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region sa-east-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region ap-southeast-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region ap-southeast-2
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region eu-central-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region us-east-2
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region us-west-1
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Found 0 ecr repositories in region us-west-2
+------+----------------+------------------+--------+
| Name | Private/Public | Number of Images | Region |
+------+----------------+------------------+--------+
+------+----------------+------------------+--------+
Summary: Found 0 ecr_repository across all regions

```
