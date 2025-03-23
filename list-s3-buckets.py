import boto3

# Create a session
session = boto3.Session()

# Create an S3 client
s3_client = session.client('s3')

# List all S3 buckets
response = s3_client.list_buckets()

# Print bucket names
print("S3 Buckets:")
for bucket in response['Buckets']:
    print(f"- {bucket['Name']}")