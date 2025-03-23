import boto3

# Create an S3 client
s3_client = boto3.client('s3')

# Download a file
s3_client.download_file(
    'jeffmbita.buzz',  # S3 bucket name
    'remote-file.txt',  # S3 object key
    'downloaded-file.txt'  # Local file path
)

print("File downloaded successfully!")