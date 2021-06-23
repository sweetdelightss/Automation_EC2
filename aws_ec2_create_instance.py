# Create EC2 instance using Python BOTO3 with two users
import boto3


def create_ec2_instance():
    try:
        print("Creating EC2 instance")
        resource_ec2 = boto3.client("ec2")
        resource_ec2.run_instances(
            ImageId="ami-0d8d212151031f51c",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="ec2-key"
        )
    except Exception as e:
        print(e)


create_ec2_instance()

# create IAM client
iam = boto3.client('iam')

# create user
response = iam.create_user(
    UserName='user1'
)
print(response)

# create user
response = iam.create_user(
    UserName='user2'
)
print(response)

# List users with pagination interface
paginator = iam.get_paginator('list_users')
for response in paginator.paginate():
    print(response)

