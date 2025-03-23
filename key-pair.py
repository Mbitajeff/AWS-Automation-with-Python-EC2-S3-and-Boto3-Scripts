import boto3

# Specify the region
region = 'us-east-1'  # Replace with your preferred region

# Create an EC2 client
ec2_client = boto3.client('ec2', region_name=region)

# Create a key pair
key_pair_name = 'my-key-pair'  # Replace with your desired key pair name
response = ec2_client.create_key_pair(KeyName=key_pair_name)

# Save the private key to a file
with open(f'{key_pair_name}.pem', 'w') as key_file:
    key_file.write(response['KeyMaterial'])

print(f"Key pair '{key_pair_name}' created and saved to '{key_pair_name}.pem'!")