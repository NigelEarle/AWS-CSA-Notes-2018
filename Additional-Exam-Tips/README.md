# Additional Exam Tips

## Based on Student Feedback...

### Kinesis

- Used to consume Big Data
- Stream large amounts of social media, news feeds, logs etc to the cloud
- Think Kinesis when approached with big data questions

- Process large amounts of data;
  - Redshift for business intelligence
  - Elastic Map Reduce for Big Data Processing


### EC2 - EBS Backed Volumes vs Instance Store Volumes

- EBS backed volumes are persistent
- Instance Store backed volumes are not persistent (ephemeral)
- EBS Volumes can be detached and reattached to other EC2 instances

- Instance store volumes cannot be detached and reattached to other instances - they exist only for the life of that instance.
- EBS volumes can be stopped; data will persist

- Instance store volumes cannot be stopped - if you do this the data will be wiped

- EBS Backed = Store Data Long Term
- Instance Store = Shouldn't be used for long-term data storage

### OpsWork

- Orchestration Service that uses Chef
- Chef consists of recipes to maintain a consistent state
- Look for the term "chef" or "recipes" or "cook books" and think OpsWorks

### Elastic Transcoder

- Media Transcoder in the cloud
- Convert media files from their original source format in to different formats that will play on smartphones, tablets, PC's, etc
- Provides transcoding presets for popular output formats, which means that you dont need to guess about which settings work best on particular devices
- Pay based on the minutes that you transcode and the resolution at which you transcode

### SWF Actors

- **Workflow Starter** - An application that can initiate (start) a workflow. Could be your e-commerce website when placing an order or a mobile app searching for bus times.
- **Deciders** - Control the flow of activity tasks in a workflow execution. If something has finished in a workflow (or fails) a Decider decides what to do next.
- **Activity Workers** - Carry out the activity tasks

### EC2 - Get Public IP Address

- Query the instances metadata:
  - `curl http://169.254.169.254/latest/meta-data`
  - `wget http://169.254.169.254/latest/meta-data`
  - Key thing to remember is that its an instances META-DATA, not user data


## Consolidated Billing

### AWS Organizations

AWS Organizations is an account management service that enables you to consolidate multiple AWS accounts into an organization that you create and centrally manage.

Available in 2 feature sets
  - Consolidated Billing
  - All features

**General Rules**

- Paying account is independent
- Cannot access resources of other accounts
- All linked accounts are independent
- Currently a limit of 20 linked accounts - can add more

**Advantages**

- One bill per AWS account
- Very esy to track charges and allocate costs
- Volume Pricing

### Best Practices

- Always enable MFA on root account
- Always use a strong and complex password on root account
- Paying account should be used for billing purposes only. Do not deploy resources in to paying account

### Things to note

- Billing Alerts
  - When monitoring is enabled on the paying account the billing data for all linked accounts is included
  - You can still create billing alerts per indvidual account

- CloudTrail
  - Per AWS Account and is enabled per region

- Can consolidate logs using an S3 bucket
  1. Turn on CloudTrail in the paying account
  2. Create a bucket policy that allows cross account access
  3. Turn on CloudTrail in the other accounts and use the bucket in the paying account

### Tips

- Consolidate billing allows you to get volume discounts on all your accounts.
- Unused reserved instances for EC2 are applied across the group
- CloudTrail is on a per account and per region basis but can be aggregated in to a single bucket in the paynig account.

## Cross Account Access

Many AWS customers use separate AWS accounts for their development and production resources. This separation allows them to cleanly separate different types of resources and can also provide some security benefits.

Cross account access makes it easier for you to work productively within a multi-account (or multi-role) AWS environment by making it easy for you to switch roles within the AWS Management Console.

You can sign in to the console using you IAM user name then switch the console using your IAM user name then switch the console to manage another account without having to enter (or remember) another user name and password

## Resource Groups & Tags

Key Value Pairs attached to AWS resources

Metadata (data about data)

Tags can sometimes be inherited

- Autoscaling, CloudFormation and Elastic Beanstalk can create other resources

Resource groups make it easy to groups your resources using the tags that are assigned to them. You can group that share one or more tags.

**Note: Container for resources**

Resource groups contain information such as:
- Region 
- Name
- Health Checks

Specific Information:
- For EC2 - Public and Private IP Addresses
- For ELB - Port Configurations
- For RDS - Database Engine etc.

## VPC Peering

**Note: Generally not tested in Associate exams, only in Professional exams**

### What is VPC Peering?

VPC Peering is simply a connection bewtween 2 VPCs that enables you to route traffic between them using private IP addresses.

Instances in either VPC can communicate with each other as if they are within the same network. You can create a VPC peering connection between your own VPCs, or with a VPC in another AWS account within a **SINGLE REGION**

AWS uses the existing infrastructure of a VPC to create a VPC peering connection; it is neither a gateway nor a VPN connection, and does not rely on separate piece of physical hardware. There is no single point of failure for communication or bandwidth bottleneck.

### VPC Peering Limitations

1. You cannot create a VPC peering connection between VPCs that have not matching or overlapping CIDR blocks ie. `10.0.0.0/16 -- X --> 10.0.0.0/24`
2. You cannot create a VPC peering connection between VPCs in different regions
3. VPC peering does not support transitive peering relationships.

## Direct Connect

AWS Direct Connect makes it easier to establish a dedicated network connection from your premises to AWS.

Using AWS Direct Connect, you can establish private connectivity between AWS and your datacenter, office or colocation environment, which in many cases can reduce your network costs, increase bandwidth throughput, and provide a more consistent network experience than internet-based connections.

### Main Benefits

- Reduce costs when using large volumes of traffic
- Increase reliability
- Increase bandwidth

### How is Direct Connect different from a VPN?

VPN Connections can be configured in minutes and are a good solution if you have and immediate need, have low to moderate bandwidth requirements, and can tolerate the inherent variability in Internet-based connectivity.

AWS Direct Connect does not involve the Internet - instead, it uses dedicated, private network connections between your intranet and AWS VPC

### Direct Connect Connections

Available in:
  - 10Gbs
  - 1Gbbs

- Sub 1 Gbps can be purchased through AWS Direct Connect Partners
- Uses Ethernet VLAN trunking (802.1Q)

## STS - Security Token Service

Grants users limited and temporary access to AWS resources. Users can come from 3 sources

### Federation (typically Active Directory)

- Uses Security Assertion Markup Language (SAML)
- Grants temp access based off the users Active Directory credentials. Does not need to be a user in IAM
- Single sign on allows users to log in to AWS console without assigning IAM credentials
- Federation with mobile apps - Facebook/AWS/Google/OpenID providers
- Cross Account Access - Access resources from one account to another

### Key Terms

- Federation
    - Combining or joing a list of users in one domain (such as IAM) with a list of users in another domain (such as Active Directory, Facebook etc)
- Identity Broker
    - A service that allows you to take an identity from point A and join it (federate it) with point B
- Identity Store
    - Services like Active Directory, Facebook, Google etc
- Identities
    - A user of a service like Facebook etc.

**SCENARIO!**

```
You are hosting a company website on some EC2 web servers in your VPC. Users of the website must log in to the site which authenticates against the companies active directory servers which are based on site at the companies head quarters

Your VPC is connected to your company HQ via a secure IPSEC VPN. Once logged in the user can only have access to their own S3 bucket. How do you set this up?
```

**SOLUTION!**

1. Users enter credentials (username and password)
2. Application calls identity broker - broker captures username and passwords
3. Broker checks with LDAP directory server - validates credentials
4. Call to STS (security token service) - getFederationToken function using IAM credentials
5. STS confirms policy and gives permisssion to create new tokens - returns 4 values
    - Access Key
    - Secret Access Key
    - Token
    - Duration (lifetime of token)
6. 4 values are sent back to application via broker
7. Application makes call to S3
8. S3 uses IAM to validate credentials
9. Credentials validated via IAM

**In The Exam!**

1. Develop and Identity Broker to communicate with LDAP and AWS STS.
2. Identity Broker alway authenticates with LDAP first, THEN with AWS STS
3. Application then gets temp access to AWS resources

## Active Directory Tips

### Exam Questions

**QUESITON: _Can you authenticate with Active Directory?_**

**ANSWER: Yes. Using SAML**

**QUESITON: _In what order do you authenticate to get the security credentials to log into Active Directory?_**

**ANSWER: Authenticate with Active Directory first and then you are assigned the temp security crednetial.**

## Workspaces

It's basically a VDI (virtual development infrastructure). A Workspace is a cloud-based replacement for a traditional desktop.

A Workspace is available as a bundle of compute resources, storage space, and software application access that allow a user to perform day-to-day tasks just like using a traditional desktop.

A user can connect to a Workspace from any supported device (PC, Mac, Chromebook, iPad, KindleFire or Android Tablets) using free Amazon Workspaces client application and credentials set up by an administrator, or their existing Active Directory credentials if Amazon Workspaces is integrated with an existing Active Directory domain.

### Quick Facts

- Windows 7 experience, provided by Windows Server 2008 R2
- By default, users can personalize their workspaces. This can be locked down by an admin however
- By default, you will be given local admin access, so you can install your own applications
- Workspaces are persistent
- All data on the D:\ is backed up every 12 hours
- You do not need an AWS account to login into workspaces
