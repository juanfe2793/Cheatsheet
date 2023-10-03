# Describe key_pairs instance

This script retrieve information about key_pairs instances in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_key_pairs_instances_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the key_pairs service in the specified region, and then uses the `describe_key_pairs` method to retrieve information about all key_pairs instances in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and region.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of key_pairs in all the regions.

## Example output

```shell
Found 0 key pairs in region ap-south-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region eu-north-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region eu-west-3
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 1 key pairs in region eu-west-2
+-----------------------+---------------+-----------+
|      Key Pair ID      | Key Pair Name |   Region  |
+-----------------------+---------------+-----------+
| key-12345678910       |  testing-key  | eu-west-2 |
+-----------------------+---------------+-----------+
Found 1 key pairs in region eu-west-1
+-----------------------+---------------+-----------+
|      Key Pair ID      | Key Pair Name |   Region  |
+-----------------------+---------------+-----------+
| key-12345678910       |  testing-key  | eu-west-1 |
+-----------------------+---------------+-----------+
Found 0 key pairs in region ap-northeast-3
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 1 key pairs in region ap-northeast-2
+-----------------------+---------------+----------------+
|      Key Pair ID      | Key Pair Name |     Region     |
+-----------------------+---------------+----------------+
| key-12345678910       |  testing-key  | ap-northeast-2 |
+-----------------------+---------------+----------------+
Found 0 key pairs in region ap-northeast-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region ca-central-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region sa-east-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region ap-southeast-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region eu-central-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 1 key pairs in region us-east-1
+-----------------------+---------------+----------------+
|      Key Pair ID      | Key Pair Name |     Region     |
+-----------------------+---------------+----------------+
| key-12345678910       |  testing-key  |   us-east-1    |
+-----------------------+---------------+----------------+
Found 0 key pairs in region ap-southeast-2
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region us-east-2
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 0 key pairs in region us-west-1
+-------------+---------------+--------+
| Key Pair ID | Key Pair Name | Region |
+-------------+---------------+--------+
+-------------+---------------+--------+
Found 1 key pairs in region us-west-2
+-----------------------+---------------+----------------+
|      Key Pair ID      | Key Pair Name |     Region     |
+-----------------------+---------------+----------------+
| key-12345678910       |  testing-key  |   us-west-2    |
+-----------------------+---------------+----------------+
Summary: Found 5 key pairs across all regions

```
