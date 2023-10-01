# Describe lambda function

This script retrieve information about EC2 lambda functions in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_ec2_lambda functions_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_lambda functions` method to retrieve information about all EC2 lambda functions in that region.
* The function then prints out the total number of lambda functions found in the region, and loops through each lambda function to print out its name, ID, and lambda function type.
* If an error occurs while trying to retrieve the lambda function information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of lambda functions in all the regions.

## Example output

```shell
Found 0 lambda functions in region ap-south-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region eu-north-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region eu-west-3
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region eu-west-2
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region eu-west-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region ap-northeast-3
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region ap-northeast-2
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region ca-central-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region ap-northeast-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region sa-east-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region ap-southeast-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region ap-southeast-2
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region eu-central-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 1 lambda functions in region us-east-1
+-----------------------------------------------------------------+------------------+-----------+
|                          Function Name                          | Function Runtime |   Region  |
+-----------------------------------------------------------------+------------------+-----------+
| some-cool-function-name                                         |    python3.7     | us-east-1 |
+-----------------------------------------------------------------+------------------+-----------+
Found 0 lambda functions in region us-east-2
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region us-west-1
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Found 0 lambda functions in region us-west-2
+---------------+------------------+--------+
| Function Name | Function Runtime | Region |
+---------------+------------------+--------+
+---------------+------------------+--------+
Summary: Found 1 lambda functions across all regions
```
