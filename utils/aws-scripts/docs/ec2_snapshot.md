# Describe EC2 snapshot

This script retrieve information about EC2 snapshots in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_ec2_snapshots_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_snapshots` method to retrieve information about all EC2 snapshots in that region.
* The function then prints out the total number of snapshots found in the region, and loops through each snapshot to print out its name, ID, and snapshot type.
* If an error occurs while trying to retrieve the snapshot information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of snapshots in all the regions.

## Example output

```shell
Found 0 EC2 snapshots in region ap-south-1
+-------------+---------------+-------------+--------+
| Snapshot ID | Snapshot Name | Volume Size | Region |
+-------------+---------------+-------------+--------+
+-------------+---------------+-------------+--------+
Found 0 EC2 snapshots in region eu-north-1
+-------------+---------------+-------------+--------+
| Snapshot ID | Snapshot Name | Volume Size | Region |
+-------------+---------------+-------------+--------+
+-------------+---------------+-------------+--------+
Found 0 EC2 snapshots in region eu-west-3
+-------------+---------------+-------------+--------+
| Snapshot ID | Snapshot Name | Volume Size | Region |
+-------------+---------------+-------------+--------+
+-------------+---------------+-------------+--------+
Found 0 EC2 snapshots in region eu-west-2
+-------------+---------------+-------------+--------+
| Snapshot ID | Snapshot Name | Volume Size | Region |
+-------------+---------------+-------------+--------+
+-------------+---------------+-------------+--------+
Found 1589 EC2 snapshots in region eu-west-1
+------------------------+-------------------------------------------------------------------------------------+-------------+-----------+
|      Snapshot ID       |                                    Snapshot Name                                    | Volume Size |   Region  |
+------------------------+-------------------------------------------------------------------------------------+-------------+-----------+
| snap-0601ac0a603ad2654 | aws-otk-sandbox-dev-istio-euw1-001-dynamic-pvc-e0c0f3d7-dba1-4bb3-a6c1-69fd4f4c6aba |      1      | eu-west-1 |
| snap-06a46176a0718696b | aws-otk-sandbox-dev-istio-euw1-001-dynamic-pvc-e0c0f3d7-dba1-4bb3-a6c1-69fd4f4c6aba |      1      | eu-west-1 |
| snap-00f957ec66150d533 | aws-otk-sandbox-dev-istio-euw1-001-dynamic-pvc-e0c0f3d7-dba1-4bb3-a6c1-69fd4f4c6aba |      1      | eu-west-1 |
```
