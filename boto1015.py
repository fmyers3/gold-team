import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="ciara id.jpeg",
    Bucket="fall-s3",
    Key="ciara id.jpeg")
    