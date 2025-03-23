# AWS Automation with Python: EC2, S3, and Boto3 Scripts

This repository contains Python scripts to automate AWS tasks using Boto3. It covers creating and managing EC2 instances, interacting with S3 buckets, and handling IAM permissions programmatically.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Scripts](#scripts)
  - [S3 Bucket Operations](#s3-bucket-operations)
  - [EC2 Instance Management](#ec2-instance-management)
  - [IAM Permissions](#iam-permissions)
- [How to Use](#how-to-use)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Features
- **S3 Bucket Operations**:
  - List S3 buckets.
  - Upload and download files to/from S3.
  - Delete files from S3.
- **EC2 Instance Management**:
  - Create and terminate EC2 instances.
  - Automate key pair creation.
  - Find valid AMI IDs for your region.
- **IAM Permissions**:
  - Troubleshoot and fix `AccessDenied` errors.
  - Attach policies to IAM users.

## Prerequisites
- Python 3.6+
- Boto3 installed (`pip install boto3`)
- AWS CLI configured with valid credentials (`aws configure`)

## Scripts

### S3 Bucket Operations
1. **List S3 Buckets**:
   - Script: `list-s3-buckets.py`
   - Lists all S3 buckets in your AWS account.

2. **Upload a File to S3**:
   - Script: `upload-to-s3.py`
   - Uploads a local file to an S3 bucket.

3. **Download a File from S3**:
   - Script: `download-from-s3.py`
   - Downloads a file from an S3 bucket.

4. **Delete a File from S3**:
   - Script: `delete-from-s3.py`
   - Deletes a file from an S3 bucket.

### EC2 Instance Management
1. **Create a Key Pair**:
   - Script: `create-key-pair.py`
   - Creates a key pair and saves the private key to a `.pem` file.

2. **Find a Valid AMI ID**:
   - Script: `find-ami-id.py`
   - Finds the latest Amazon Linux 2 AMI ID for your region.

3. **Launch an EC2 Instance**:
   - Script: `launch-ec2-instance.py`
   - Launches a `t2.micro` instance using the key pair and AMI ID.

4. **Terminate an EC2 Instance**:
   - Script: `terminate-ec2-instance.py`
   - Terminates an EC2 instance.

### IAM Permissions
1. **Troubleshoot `AccessDenied` Errors**:
   - Ensure your IAM user has the necessary permissions (e.g., `s3:ListAllMyBuckets`).

## How to Use
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/aws-automation-python.git
   cd aws-automation-python
##Troubleshooting
##AccessDenied Error
If you encounter an AccessDenied error, ensure your IAM user has the necessary permissions. For example:

For S3: Attach the AmazonS3ReadOnlyAccess policy.

For EC2: Attach the AmazonEC2FullAccess policy.

##NoRegionError
If you encounter a NoRegionError, specify the region in your script or AWS CLI configuration:

python
Copy
ec2_resource = boto3.resource('ec2', region_name='us-east-1')
##License
This project is licensed under the MIT License. See the LICENSE file for details.

Copy

---

### **Push to GitHub**
Now, let’s push everything to your newly created GitHub repository.

#### **Steps to Push**:
1. **Initialize a Git Repository**:
   ```bash
   git init
