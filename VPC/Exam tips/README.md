# Exam Tips

## VPC Intro

- Think of a VPC as a logical data center in AWS
- Consists of IGW(or Virtual Private Gateways), route tables, network access control lists (NACL), subnets, security groups
- 1 subnet = 1 AZ
- Security groups are Statful; NACLs are Stateless
  - Must open both inbound and outbound ports for NACLs
- NO TRANSITIVE PEERING!!

