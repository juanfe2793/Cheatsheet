import boto3
import concurrent.futures
import argparse


ec2 = boto3.resource("ec2")
quota = boto3.client('service-quotas')

EIP_QUOTA=quota.get_service_quota(ServiceCode='ec2', QuotaCode='L-0263D0A3')["Quota"]["Value"]

unused_ips = {}

def check_release_address_permission(region_name):
    ec2conn = boto3.client("ec2", region_name=region_name)
    try:
        ec2conn.release_address(AllocationId="test")
    except ec2conn.exceptions.ClientError as e:
        if e.response["Error"]["Code"] == "UnauthorizedOperation":
            print("Current credentials do not have permission to release Elastic IPs")
            return False
    return True

def clean_unused_eips_in_region(region_name, dry_run):
    unused_ips_in_region = {}
    try:
        ec2conn = boto3.client("ec2", region_name=region_name)
        addresses = ec2conn.describe_addresses(
            Filters=[{"Name": "domain", "Values": ["vpc"]}])["Addresses"]
        print(f"Found a Total of **{EIP_QUOTA-len(addresses)}** Elastic IPs available in: {region_name}")
        for address in addresses:
            if (
                "AssociationId" not in address
                and address["AllocationId"] not in unused_ips_in_region
            ):
                unused_ips_in_region[address["AllocationId"]] = region_name
                if not dry_run:
                    ec2conn.release_address(AllocationId=address["AllocationId"])
                    print(f"Deleted unused Elastic IP {address['PublicIp']} in region {region_name}")
                else:
                    print(f"Dry-run: Would have deleted unused Elastic IP {address['PublicIp']} in region {region_name}")
    except Exception as e:
        print(f"The following error occurs trying to delete Unused Elastic IP in region: {region_name}: {e}")
    return unused_ips_in_region

def clean_unused_eips():

    parser = argparse.ArgumentParser(description='Clean up unused Elastic IPs in all AWS regions.')
    parser.add_argument('--dry-run', dest='dry_run', action='store_true',
                        help='Perform a dry run and do not delete any Elastic IPs')
    args = parser.parse_args()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for region in ec2.meta.client.describe_regions()["Regions"]:
            region_name = region["RegionName"]
            if check_release_address_permission(region_name): # Check if we have permission to release EIPs.
              futures.append(executor.submit(clean_unused_eips_in_region, region_name, dry_run=args.dry_run))
        for future in concurrent.futures.as_completed(futures):
            unused_ips.update(future.result())

    print(f"Summary: Found {len(unused_ips)} unused Elastic IPs across all regions:")
    print(unused_ips)

if __name__ == "__main__":
    clean_unused_eips()