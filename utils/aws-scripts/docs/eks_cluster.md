# Describe Elastic IPs

This script retrieve information about EKS clusterss across all regions. Here's a brief overview of what the script does:

* Defines a function called `list_eks_clusters` that takes a single argument, `region_name`. This function uses the `boto3` library to create a client for the EKS service in the specified region, and then uses the `list_eks_clusters_by_region` method to retrieve information about all Elastic IPs in that region.
* The function then loops through each EKS cluster and retrieves additional information about the cluster (if there is one). It then adds the EKS cluster basic information to a list.
* If an error occurs while trying to retrieve the EKS cluster information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of EKS clusters in all the regions.

## Example output

```shell
Found 0 EKS clusters in the region ap-south-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region eu-north-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region eu-west-3
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region eu-west-2
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 1 EKS clusters in the region eu-west-1
+------------------------------------+--------------------+-----------+
|            Cluster Name            | Kubernetes Version |   Region  |
+------------------------------------+--------------------+-----------+
| testing-dummy-cluster |        1.24        | eu-west-1 |
+------------------------------------+--------------------+-----------+
Found 0 EKS clusters in the region ap-northeast-3
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region ap-northeast-2
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region ap-northeast-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region ca-central-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region sa-east-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region ap-southeast-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region ap-southeast-2
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region eu-central-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region us-east-2
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 0 EKS clusters in the region us-west-1
+--------------+--------------------+--------+
| Cluster Name | Kubernetes Version | Region |
+--------------+--------------------+--------+
+--------------+--------------------+--------+
Found 4 EKS clusters in the region us-east-1
+--------------------------------------+--------------------+-----------+
|             Cluster Name             | Kubernetes Version |   Region  |
+--------------------------------------+--------------------+-----------+
|    testing-dummy-cluster-1           |        1.24        | us-east-1 |
| testing-dummy-cluster-2              |        1.24        | us-east-1 |
|   testing-dummy-cluster-3            |        1.24        | us-east-1 |
|  testing-dummy-cluster-4             |        1.24        | us-east-1 |
+--------------------------------------+--------------------+-----------+ç
Found 2 EKS clusters in the region us-west-2
+--------------------------------------+--------------------+-----------+
|             Cluster Name             | Kubernetes Version |   Region  |
+--------------------------------------+--------------------+-----------+
|  testing-dummy-cluster-1             |        1.24        | us-west-2 |
| testing-dummy-cluster-2              |        1.24        | us-west-2 |

Summary: Found 7 EKS clusters across all regions


```
