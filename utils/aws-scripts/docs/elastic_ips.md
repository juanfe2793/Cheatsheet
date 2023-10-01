# Describe Elastic IPs

This script retrieve information about Elastic IPs across all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_eips_in_region` that takes a single argument, `region_name`. This function uses the `boto3` library to create a client for the EC2 service in the specified region, and then uses the `describe_addresses` method to retrieve information about all Elastic IPs in that region.
* The function then loops through each Elastic IP and retrieves additional information about the associated EC2 instance (if there is one). It then adds the Elastic IP information to a list.
* If an error occurs while trying to retrieve the Elastic IP information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

## Example output

```shell

Found a Total of **0** Elastic IPs in ap-south-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in eu-north-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in eu-west-3
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in eu-west-2
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **3** Elastic IPs in eu-west-1
+-------------------+----------------------------+-----------+
| Elastic Public IP |       Allocation ID        |   Region  |
+-------------------+----------------------------+-----------+
|    1.2.3.4        | eipalloc-12345678910       | eu-west-1 |
|    1.2.3.4        | eipalloc-12345678910       | eu-west-1 |
|    1.2.3.4        | eipalloc-12345678910       | eu-west-1 |
+-------------------+----------------------------+-----------+
Found a Total of **0** Elastic IPs in ap-northeast-3
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in ap-northeast-2
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in ap-northeast-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in ca-central-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in sa-east-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in ap-southeast-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in ap-southeast-2
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in eu-central-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **0** Elastic IPs in us-east-2
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **1** Elastic IPs in us-east-1
+-------------------+----------------------------+-----------+
| Elastic Public IP |       Allocation ID        |   Region  |
+-------------------+----------------------------+-----------+
|    1.2.3.4        | eipalloc-12345678910       | us-east-1 |
+-------------------+----------------------------+-----------+
Found a Total of **0** Elastic IPs in us-west-1
+-------------------+---------------+--------+
| Elastic Public IP | Allocation ID | Region |
+-------------------+---------------+--------+
+-------------------+---------------+--------+
Found a Total of **2** Elastic IPs in us-west-2
+-------------------+----------------------------+-----------+
| Elastic Public IP |       Allocation ID        |   Region  |
+-------------------+----------------------------+-----------+
|    1.2.3.4        | eipalloc-12345678910       | us-west-2 |
|    1.2.3.4        | eipalloc-12345678910       | us-west-2 |
+-------------------+----------------------------+-----------+
Summary: Found 6 Elastic IPs across all regions:


```
