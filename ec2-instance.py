import boto3

# Specify the region
region = 'us-east-1'  # Replace with your preferred region

# Create an EC2 resource
ec2_resource = boto3.resource('ec2', region_name=region)

# Launch an EC2 instance
instance = ec2_resource.create_instances(
    ImageId='ami-0062355a529d6089c',  # Replace with the AMI ID from Step 2
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',  # Free tier eligible
    KeyName='my-key-pair'  # Replace with the key pair name from Step 1
)

# Wait for the instance to be running
instance[0].wait_until_running()

# Print instance details
print(f"Instance {instance[0].id} created!")
print(f"Public IP: {instance[0].public_ip_address}")