import boto3
ec2_resource=boto3.resource("ec2")
ec2_resource.create_instances(ImageId='ami-026b57f3c383c2eec',
    InstanceType='t2.micro',
MaxCount=1,
    MinCount=1)
