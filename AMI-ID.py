import boto3

# Specify the region
region = 'us-east-1'  # Replace with your preferred region

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name=region)

# Describe AMIs (Amazon Linux 2 in this example)
response = ec2_client.describe_images(
    Filters=[
        {'Name': 'name', 'Values': ['amzn2-ami-hvm-*']},
        {'Name': 'architecture', 'Values': ['x86_64']},
        {'Name': 'owner-alias', 'Values': ['amazon']},
        {'Name': 'state', 'Values': ['available']}
    ]
)

# Get the first AMI ID
ami_id = response['Images'][0]['ImageId']
print(f"AMI ID: {ami_id}")