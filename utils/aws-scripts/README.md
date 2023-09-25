# AWS useful Scripts

Here you will find useful python scripts

## Pre-requisites

Install the following:

### Python3

```shell
brew install python3
```

### pip packages

```shell
pip install -r requirements.txt
```

## Describe AWS Resources

This is the list of the scripts useful to **describe** AWS resources such like: EC2 instances, Elastic IPs.

[describe EC2 instance](#describe-ec2-instances)

## Teardown AWS Resources

This is the list of the scripts useful to **teardown/delete** AWS resources such like: EC2 instances, Elastic IPs.

[Teardown unused Elastic IPs](#teardown-unused-elastic-ips)

### Describe EC2 instances

```shell
python3 describe/ec2_instances.py
```

This script retrieve information about EC2 instances in all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_ec2_instances_by_region` that takes a single argument, region_name. This function uses the boto3 library to create a client for the EC2 service in the specified region, and then uses the `describe_instances` method to retrieve information about all EC2 instances in that region.
* The function then prints out the total number of instances found in the region, and loops through each instance to print out its name, ID, and instance type.
* If an error occurs while trying to retrieve the instance information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

### Describe Elastic IPs

```shell
python3 describe/elastic_ips.py
```

This script retrieve information about Elastic IPs across all regions. Here's a brief overview of what the script does:

* Defines a function called `describe_eips_in_region` that takes a single argument, `region_name`. This function uses the `boto3` library to create a client for the EC2 service in the specified region, and then uses the `describe_addresses` method to retrieve information about all Elastic IPs in that region.
* The function then loops through each Elastic IP and retrieves additional information about the associated EC2 instance (if there is one). It then adds the Elastic IP information to a list.
* If an error occurs while trying to retrieve the Elastic IP information, the function catches the exception and prints out an error message.
* Finally, the function returns a summary of the total number of instances in all the regions.

### Teardown unused Elastic IPs

```shell
python3 teardowm/clean_unused_eips.py
```

Do you want to verify firts which Elastic IPs will be deleted? use `--dry-run` option

```shell
python3 teardowm/clean_unused_eips.py --dry-run
```

The Python script runs the following steps in order to delete the unused EIPs:

* Get all the regions available in the AWS account
* Get the Service_Quota limits for the Elastic IPs in the AWS account
* For each region, get all the allocated EIPs
* For each EIP, check if it is associated with any AWS resource
* If the EIP is not associated with any AWS resource, then release it
* Communicate the user which EIP are released
