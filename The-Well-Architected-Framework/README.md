# The Well Architected Framework

This section aggregates the well architected framework white paper

https://aws.amazon.com/architecture/well-architected/
https://d0.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf

## Best Practices

### Business Benefits of the Cloud

- Almost zero upfront infrastructure investment
- Just-in-time infrastructure
- More efficient resource utilization
- Usage-based costing
- Reduced time to market

### Technical Benefits of the Cloud

- Automation - "Scriptable Infrastructure"
- Auto-Scaling
- Proactive Scaling
- More Efficient Development lifecycle
- Improved Testability
- Disaster Recovery and Business Continuity
- "Overflow" the traffic to the cloud

### Design For Failure

**Rule of thumb:**

Be a pessimist when designing architectures in the cloud - assume things will fail. In other words, always design, implement and deploy for automated recovery from failure.

**Assume that...**

- your hardware _will_ fail
- disaster _will_ strike your application
- you _will_ slammed with more than the expected number of requests per second some day.
- with time your application software _will_ fail too.

Being a pessimist, you end up thinking about recovery strategies during design time, which helps in designing overall system better.

### Decouple Your Components

The key is to build components that do not have tight dependencies on each other, so that if once component were to die(fail), sleep(not respond) or remain busy(slow to respond) for some reason, the other components in the system are built so as to continue to work as if no failure is happening.

In essence, loose coupling isolates the various layers and components of you application so that each component interacts async with the others and treats them as a "black box".

**For Example...**

In the case of web application architecture, you can isolate the app server from the web server and from the db. The app server does not know about your web server and vice versa, this gives decoupling between these layers and there are not dependencies code wise or functional perspectives.

In the case of batch processing architecture, you can create async components that are independent of each other.

### Implement Elasticity

The cloud brings a new concept of elasticity in your applications. Elasticity can be implemented in 3 ways..

1. **Proactive Cyclic Scaling:** Periodic scaling that occurs at a fixed interval (daily, weekly, monthly, quarterly)
2. **Proactive Event-base Scaling:** Scaling just when you are expecting a big surge of traffic requests due to a scheduled business event (new product launch, marketing campaigns)
3. **Auto-scaling based on demain:** By using monitoring service, you system can send triggers to take appropriate actions so that if scales up or down based on metrics (utilization of servers or network I/O)

## The Well Architected Framework

### What is the well architected framework?

This has been developed by the Solutions Architecture team based on their experience with helping AWS customers. The well architected framework is a set of questions that you can use to evaluate how well your architecture is aligned to AWS best practices.

### 5 Pillars of the Well Architected Framework

- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Operation Excellence

### Structure of each pillar

- Design Principles
- Definition
- Best Practices
- Key AWS Services
- Resources

### General Design Principles

- Stop guessing your capacity needs
- Test systems at production scale
- Automate to make architectural experimentation easier
- Allow for evolutionary architectures
- Data-driven architectures
- Improve through game days

## Pillar 1 - Security

### Design Principles

- Apply security at all layers!
- Enable tracibility
- Automate responses to security events
- Focus on securing your system
- Automate security best practices

### Definitions

Security in the cloud consists of 4 areas...

#### Data Protection

Before you begin to architect security practices across your environment, **basic data classification should be in place**. You should organize and classify your data in to segments such as publicly available, available to only members of your organization, available to only certain members of your organization, available only to the board etc.

You should also implement a least privilege access system so that people are only able to access what they need. However most importantly, you should encrypt everthing where possible, whether it be at rest or in transit.

**In AWS the following practices help to protect your data...**

- AWS customers maintain full control over their data
- AWS makes it easier for you to encrypt your data and manage keys, including regular key rotation, which can be easily automated natively by AWS or maintained by a customer.
- Detailed logging is available that contains important content, such as file access and changes.
- AWS has designed storage systems for exceptional resiliency. As an example, Amazon S3 is designed for 11, 9's of durability. (if you store 10,000 objects with AWS S3, you can on average expect to incur a loss of a single object once every 10,000,000 years)
- Versioning, which can be part of a larger data lifecycle-management process, can protect against accidental overwrites, deletes and similar harm
- AWS never initiates the movement of data between regions. Content placed in a region will remain in that region unless the customer explicitly enable a feature or leverages a service that provides that functionality

**What questions should you be asking yourself?**

- How are you encrypting your data at rest?
- How are you encrypting your data in transit (SSL)?

#### Privilege Management

Privilege Management ensures that only authorized and authenticated users are able to access your resources, and only in a manner that is intended.

**This can include**

- Access Control Lists (ACLs)
- Role Based Access Controls
- Password Management (such as password rotation policies)

**What questions should you be asking yourself?**

- How are you protecting access to and use the AWS root account credentials?
- How are you defining roles and responsibilites of system users to control human access to the AWS Management Console and APIs?
- How are you limiting automated access (such as frmo applications, scripts, or 3rd party tools or services) to AWS resources?
- How are you managing keys and credentials?

#### Infrastructure Protection

Outside of Cloud, this is how you protect your data center. RFID controls, security, lockable cabinets, CCTV etc. Within AWS they handle this so Infrastructure Protection exists at a VPC level.

**What questions should you be asking yourself?**

- How are you enforcing network and host-level boundary protection?
- How are you enforcing AWS service level protection?
- How are you protecting the integrity of the OS on your AWS EC2 instances?

#### Detective Controls

You can use detective controls to detect or identify a security breach. AWS Services to achieve this include

- AWS Cloudtrail
- AWS CloudWatch
- AWS Config
- AWS S3
- AWS Glacier

**What questions should you be asking yourself?**

- How are you capturing and analyzing your logs?

### Key AWS Services

1. Data Protection
  - Encrypt both in transit and at rest using - ELB, EBS, S3 and RDS
2. Privilege Management
  - IAM, MFA
3. Infrastructure Protection
  - VPC
4. Detective Controls
  - AWS Cloud Trail, AWS Config, AWS Cloud Watch

## Pillar 1 - Reliability

The reliability pillar covers the ability of a system to recover from service or infrastructure outages/discruptions as well as the ability to dynamically acquire computing resources to meet demand.

- Test recovery procedures
- Automatically recover from failure - Netflix SimianArmy
- Scale horizontally increase aggregate system availability
- Stop guessing capacity

### Definition

Reliability in the cloud consists of 3 areas...

1. Foudations
2. Change Management
3. Failure Management

### Foundations

With AWS, they handle most of the foundations for you. The cloud is designed to be essentially limitless meaning that AWS handle the networking and compute requirements themselves. However they do set the service limits to stop customers from accidentally over-provisioning resource

https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html

**What questions should you be asking yourself?**

- How are you managing AWS service limits for your account?
- How are you planning your network topology on AWS?
- Do you have an escalation path to deal with technical issues?

### Change Management

You need to be aware of how change affects a system so that you can plan procatively around it. Monitoring allows you to detect any changes to your environment and react. In traditional systems, change control is done manually and are carefully co-ordinated with auditing.

With AWS things are a lot easier, you can use CloudWatch to monitor your environment and services such as autoscaling to automate change in response on your production environment

**What questions should you be asking yourself?**

- How does your system adapt to changes in demand?
- How are you monitoring AWS resources?
- How are ou executing change management?

### Failure Mangement

With cloud, you should always architect your systems with the assumptons that failure will occur. You should become aware of these failures, how they occured, how to respond to them and then plan on how to prevent these from happening again.

**What questions should you be asking yourself?**

- How are you backing up your data?
- How does your system withstand component failures?
- How are you planning for recovery?

### Key AWS Services

1. Foundations
  - IAM, VPC
2. Change Mangement
  - AWS CloudTrail
3. Failure Management
  - AWS CloudFormation
