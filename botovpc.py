import boto3
client=boto3.client("ec2")
response = client.delete_vpc(
    VpcId= 'vpc-0663b2727b0ae0c60'
    )
response
