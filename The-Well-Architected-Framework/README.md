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

### Data Protection

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

### Privilege Management

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

### Infrastructure Protection

Outside of Cloud, this is how you protect your data center. RFID controls, security, lockable cabinets, CCTV etc. Within AWS they handle this so Infrastructure Protection exists at a VPC level.

**What questions should you be asking yourself?**

- How are you enforcing network and host-level boundary protection?
- How are you enforcing AWS service level protection?
- How are you protecting the integrity of the OS on your AWS EC2 instances?

### Detective Controls

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

## Pillar 2 - Reliability

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

## Pillar 3 - Performance Efficiency

The Performance Efficiency pillar focuses on how to use computing resources efficiency to meet your requirements and how to maintain that efficiency as demand and technology evolves.

### Design Priniciples

- Democratize advanced technologies
- Go global in minutes
- Use server-less architectures
- Experiment more often

### Definition

**Performance Efficiency in the cloud consists of 4 areas...**

### Compute

When architecting your system it is important to choose the right kind of server!!

Some applications require heavy CPU utilization, some require heavy memory utilization etc.

With AWS servers are virtualized and at the click of a button (or API call) you can change the type of server in which your environment is running on. You can even switch to running with no servers at all and use AWS Lambda.

**What questions should you be asking yourself?**

- How do you select the appropriate instance type for your system?
- How do you ensure that you continue to have the most appropriate instance type as new instance types and features are introduced?
- How do you monitor your instances post launch to ensure they are performing as expected?
- How do you ensure that the quantity of your instances match demand?

### Storage

The optimal storage solutions for your environment depends on a number of factors

- Access Methods - Block, File or Object
- Patterns of Access - Random or Sequential
- Throughput Required
- Frequency of Access - Online, Offline or Archival
- Frequency of Update - Worm, Dynamic
- Availability Constraints
- Durability Constraints

At AWS the storage is virtualized. With S3 you can have 11 x 9's durability, Cross Region Replication etc. With EBS you can choose between storage mediums (SSD, Magnetic, PIOPS etc).
You can also easily move volumes between the different types of storage mediums.

**What questions should you be asking yourself?**

- How do you select the appropriate storage solution for your system?
- How do you ensure that you continue to have the most appropriate storage solution as new storage solution features are launched?
- How do you monitor your storage solution to ensure it is performing as expected?
- How do you ensure that the capacity and throughput of your storage solutions matches demand?

### Database

The optimal database solution depends on a number of factors. Do you need database consistency, do you need high availability, do you need No-SQL, do you need DR etc.

With AWS you get a LOT of options. RDS, DynamoDB, Redshift etc.

**What questions should you be asking yourself?**

- How do you select the appropriate database solution for your system?
- How do you ensure that you continue to have the most appropriate database solution and features as new database solution and features are luanched?
- How do you monitor your databases to ensure performance is as expected?
- How do you ensure the capacity and throughput of your databases matches demand?

### Space-time trade-off

Using AWS you can use services such as RDS to add read replicas, reducing the load on your database and creating mutliple copies of the database. This helps to lower latency.

You can use the global infrastructure to have multiple copies of your environment, in regions that is closest to our customer base. You can also use caching services such as ElastiCache or CloudFront to reduce latency.

**What questions should you be asking yourself?**

- How do you select the appropriate proximity and caching solutions for your system?
- How do you ensure that you continue to have the most appropriate proximity and caching solutions as new solutions are launched?
- How do you monitor your proximity and caching solutions to ensure performance is as expected?
- How do you ensure that the proximity and caching solutions you have matches demand?

### Key AWS Services

1. Compute
  - Autoscaling
2. Storage
  - EBS, S3, Glacier
3. Database
  - RDS, DynamoDB, Redshift
4. Space-time Trade-Off
  - Cloudfront, Elasticache, Direct Connect, RDS Read Replicas etc.

## Pillar 4 - Cost Optimization

Use the Cost Optimization pillar to reduce your costs to a minimum and use those savings for other parts of your business. A cost-optimized system allows you to pay the lowest price possible while sitll achieving your business objectives.

### Design Principles

- Transparently attribute expenditure
- Use managed services to reduce cost of ownership
- Trade capital expense for operating expense
- Benefit from economies of scale
- Stop spending money on data center operations

### Definition

**Cost optimization in the cloud consists of 4 areas...**

### Matched supply and demand

Try to optimally align supply with demand. Dont over provision or under provision, instead as demand grows, so should your supply of compute resources. Think of things like Autoscaling which scale with demand.

Similiarly in a server-less context, use services sucha as Lambda that only execute when a request comes in.

Services such as CloudWatch can also help you keep track as to what your demand is.

**What questions should you be asking yourself?**

- How do you make sure your capacity matches but does not substantially exceed what you need?
- How are you optimizing your usage of AWS services?

### Cost-effective resources

Using the correct instance type can be key to cost savings. For example you might hvae a reporting process that is running on a t2-Micro and it takes 7 hours to complete. That same process could be run on a an m4.2xlarge in a manner of minutes. The result remains the same but the t2.micro is more expensive because it ran for longer.

A well architected system will use the most cost efficient resources to reach the end business goal

**What questions should you be asking yourself?**

- Have you selected the appropriate resource types to meet your cost targets?
- Have you selected the appropriate pricing model to meet your cost targets?
- Are there managed services (higher level services that Amazon EC2, Amazon EBS) that you can use improve your ROI?

### Expenditure Awareness

With cloud you no longer have to go out and get quotes on physical servers, choose a supplier, have those resources delivered, installed, made available etc. You can provision things within seconds, however this comes with its own issues.

Many organizations have different teams, each with their own AWS accounts. Being aware of what each team is spending and where is crucial to any well architected system.

You can use cost allocation tags to track this, billing alerts as well as consolidated billing.

**What questions should you be asking yourself?**

- What access control and procedures do you have in place to govern AWS costs?
- How are you monitoring usage and spending?
- How do you decommission resources that you no longer need, or stop resources that are temporarily not needed?
- How do you consider data-transfer charges when designing your architecture?

### Optimizing Over Time

AWS moves FAST! There are hundreds of new services (and potentially 1000 new services this year). A service that you chose yesterday may not be the best service to be using today.

For example, consider MySQL RDS, Aurora was launched at re:invent 2014 and is now out of preview. Aurora may be a better option now for your business because of its performance and redundancy.

You should keep track of the changes made to AWS and constantly re-evaluate your existing arhcitecture. You can do this by subscribing to AWS blog nd by using services such as Trusted Advisor.

**What questions should you be asking yourself?**

- How do you manage and/or consider the adoption of new services?

### Key AWS Services

1. Matched Supply and Demand
  - Autoscaling
2. Cost-effective resources
  - EC2 (reserved instances), AWS Trusted Advisor
3. Expenditure Awareness
  - CloudWatch Alarms, SNS
4. Optimizing Over Time
  - AWS Blog, AWS Trusted Advisor

## Pillar 5 - Operational Excellence

The Operational Excellence pillar includes operational practices and procedures used to manage production workloads

This includes how planned changes are executed, as well as responses to unexpected operational events.

Change execution and responses should be automated. All processes and procedures of operational excellence should be documented, tested and regularly reviewed

### Design Principles

- Perform operations with code
- Align operations processes to business objectives
- Make regular, small, inceremental changes
- Test for responses to unexpected events
- Learn from operational events and failures
- Keep operations procedures current

### Definition

**There are 3 best practice areas of Operational Excellence in the cloud...**

### Preperation

Effective preparation is required to drive operational excellence. Operations checklists will ensure that workloads are ready for production operation, and prevent unintentional production promotion without effective preparation.

Workloads should have...

**Runbooks** - operations guidance that operations teams can refer to so they can perform normal daily tasks.

**Playbooks** - guidance for responding to unexpected operational events. Playbooks should include response plans, as well as escalation paths and stakeholder notifications.

In AWS there are several methods, services and features that can be used to support operational readiness and the ability to prepare for normal day-to-day operations as well as unexpected operational events.

**CloudFormation** can be used to ensure that environments contain all required resources when deployed to prod and the configuration of the environment is based on tested best practices, which reduces the opportunity for human error.

**Autoscaling** or other automated scaling mechanisms will allow workloads to automatically respond when business-related events affect operational needs.

**AWS Config** with the AWS Config rules feature create mechanisms to automatically track and respond to changes in your AWS workloads and environments

It is also important to use features like **tagging** to make sure all resources in a workload can be easily identified when needed during operations and respones.

**What preperation questions should you ask yourself for operational excellence?**

- What best practices for cloud operations are your using?
- How are you doing configuration management for your workload?

Be sure that documentation doesnt become stale or out of date! Documentation should be thorough!

Without application designs, environment configs, resource configs, response plans, and mitgation plans documentation is not complete.

If documentation is not updated and tested regularly, it will not be useful when unexpected operational events occur. If workloads are not reviewed before production, operations will be affected when undetected issues occur.

If resources are not documented, when operational events occur, determining how to respond will be more difficult while the correct resources are identified.

### Operation

Operations should be standardized and manageable on a routine basis. The focus should be on automation, small frequent changes, regular QA testing, and defined mechanisms to track, audit, roll back and review changes.

Changes should not be large and infrequent, they should not require scheduled downtime, and they should not require manual execution. A wide range of logs and metrics that are based on key operational indicators for a workload should be collected and reviewed to ensure continuous operations.

**What questions should you be asking yourself for operational excellence?**

- How are you evolving your workload while minimizing the impact of change?
- How do you monitor your workload to ensure it is operating as expected?

Routine operations, as well as responses to unplanned events, should be automated. Manual processes for deployments, release management, changes and rollbacks should **avoided**.

Releases should **not** be large batches that are done infrequently.

Rollbacks are more difficult in large changes, and failing ot have a rollback plan or the ability to mitigate failure impacts will prevent continuity of operations.

Align monitoring to business needs, so that the responses are effective at maintaining business continuity. Monitoring that is ad hoc and not centralized, with responses that are manual, will cause more impact to operations during unexpected events.

### Response

Responses to unexpected operational events should be automated. This is not just for alerting but also for mitigation, remediation, rollback and recovery.

Alerts should be timely and should invoke escalations when response are not adequate to mitigate the impact of operational events.

QA mechanisms should be in place to automatically roll back failed deployments.

Responses should follow a pre-defined playbook that includes stakeholders, the escalation process and procedures. Escalation paths should be defined and include both functional and hierarchical escalation capabilities. Heirarchical escalation should be automated and escalated priority should result in stakeholder notifications.

**What questions should you be asking yourself?**

- How do respond to unplanned operational events?
- How is escalation managed when responding to unplanned operational events?

### Key AWS Services

1. **Preparation**
  AWS Config provides a detailed inventory of your AWS resources and configuration, and continuously records configuration changes. AWS Service Catalog helps to create a standarized set of service offerings that are aligned to best practices. Designing workloads that use automation with services like AutoScaling, AWS SQS are good methods to ensure continuous operations in the event of unexpected operational events.
2. **Operations**
  AWS CodeCommit, AWS CodeDeploy and AWS CodePipeline can be used to manage and automate code changes to AWS workloads. Use AWS SDKs or 3rd party libs to automate operational changes. Use AWS CloudTrail to audit and track changes made to AWS environments
3. **Responses**
  Take advantage of all of the AWS CloudWatch service features for effective and automated responses. CloudWatch alarms can be used to set thresholds for alerting and notification and CloudWatch events can trigger notifications and automated responses.


