import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("fall-s3")
response = bucket.create(
     ACL='private',
     )
     
print(response)
