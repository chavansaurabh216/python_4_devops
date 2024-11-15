ec2_type = input("Enter the EC2 type: ")

if ec2_type =="t2.micro":
    print(f"{ec2_type} will be created")
elif ec2_type =="t2.medium":
    print(f"{ec2_type} cannot be created due to subscription")
elif ec2_type =="t2.large":
    print(f"{ec2_type} cannot be created due to subscription")
else:
    print(f"{ec2_type} is not correct, please enter the correct ec2 type")