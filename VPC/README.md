# VPC - Virtual Private Cloud

Think of VPC as virtual data center in the cloud!

## VPC Definition

Amazon Virtual Private Cloud (Amazon VPC) lets you provision a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define.

You have complete control over you virtual network environment, including selection of your own IP address range, creation of subnets and config of route tables and network gateways.

You can easily customize the network config for your VPC. For example, you can create a public facing subnet of your webservers that has access to the internet, and place your backend systems such as databases or application servers in a private-facing subnet with no internet access.

You can leverage multiple layers of security, including security groups and network access control lists, to help control access to EC2 instances on each subnet.

Additionally, you can create a Hardware Virtual Private Network (VPN) connection between your corporate datacenter and your VPC and leverage the AWS cloud as an extension of your corporate datacenter.

**NOTE:** Private and public subnets within a VPC can only have one subnet per AZ

Use (cidr.xyz)[https://cidr.xyz/] to figure out subnet ranges within a VPC

### What can you do with a VPC?

- Launch instances into a subnet of your choosing
- Assign custom IP address ranges in each subnet
- Configure route tables between subnets
- Create single internet gateway and attach it to our VPC
- Much better security control over your AWS resources
- Instance security groups
- Subnet network access control lists (ACLS)

### Default VPC vs Private VPC

- Default VPC is user friendly, allowing you to immediately deploy instances
- All subnets have a route to internet
- No private subnets in default VPC
- EC2 instance has both a public and private IP address.

### VPC Peering

- Allows you to connect one VPC with another via a direct network route using private IP addresses
- Instances behave as if they are on the same private network.
- You can peer VPCs with other AWS accounts as well as with other VPCs in the same account
- Peering is in a star config: ie 1 central VPC peers with 4 others. NO TRANSITIVE PEERING!!
