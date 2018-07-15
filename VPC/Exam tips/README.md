# Exam Tips

## VPC Intro

- Think of a VPC as a logical data center in AWS
- Consists of IGW(or Virtual Private Gateways), route tables, network access control lists (NACL), subnets, security groups
- 1 subnet = 1 AZ
- Security groups are Statful; NACLs are Stateless
  - Must open both inbound and outbound ports for NACLs
- NO TRANSITIVE PEERING!!

## NAT Instances

- When creating a NAT instance, Disable Source/Destination Check on the instance.
- NAT instances must be in a public subnet
- There must be a route out of the private subnet to the NAT, in order for this to work.
- The amount of traffic that NAT instances can support depends on the instance size. If you are bottlenecking, increase the instance size.
- You can create high availability using Autoscaling Groups, multiple subnets in different AZs, and a script to automate failover.
- Behind a Security Group.

## Nat Gateways

- Preferred by the enterprise
- Scale automatically up to 10G
- No need to patch OS
- Not associated with security groups
- Automatically assigned public IP
- Must update root tables and point them to NAT Gateway
- Having one NAT Gateway in one AZ is not good enough, must me redundant in multiple AZs
- No need to disable Source/Destination Checks
- More Secure than NAT Instance