import boto3

# Specify the region
region = 'us-east-1'  # Replace with your preferred region

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name=region)

# Terminate the instance
instance_id = 'i-07a0627e3bcb0fa7d'  # Replace with your instance ID
ec2_client.terminate_instances(InstanceIds=[instance_id])

print(f"Instance {instance_id} terminated!")