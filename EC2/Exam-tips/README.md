# Exam Tips

## EC2 Instance Run Down

- **On Demand** - allows you to pay a fixed rate by the hour (or second) with not commitement

- **Reserved** - provides you with the capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 year terms

- **Spot** - Enables you to bid whatever price you want for instane capacity, providing for even greater savings if your applications have flexible start and end times

- **Dedicated Hosts** - Physical EC2 server dedicated for your use. Dedicated Hosts can help reduce costs by allowing you to use your existing server-bound software license

**_Important Note!!_**

If a Spot instance is terminated by Amazon EC2, you will not be charged for a partial hour of usage. However, if you terminatethe instance yourself, you will be charged for the complete hour in which the instance ran.

## Instance Types

**F.** - FGPA
**I.** - IOPS
**G.** - Graphics
**H.** - High Disk Throughput
**T.** - Cheap General Purpose (think T2 Micro)
**D.** - Density
**R.** - Ram
**M.** - Main choice for general purpose applications
**C.** - Compute
**P.** - Grahics(Pics)
**X.** - Extreme Memory

## Volume Types

### SSD

- **General Purpose (SSD)** - balances price and perf. for a wide variety of workloads

- **Provisioned IOPS (SSD)** - Highest perf. SSD volume for mission-critical low-latency or high-throughput workloads

### Magnetic

- **Throughput Optimized HDD** - Low cost HDD volume designed for frequently accessed, throughput-intensive workloads

- **Cold HDD** - Lowest cost HDD volume designed for less frequently accessed workloads

- **Magnetic** - Previous Generation. Can be a boot volume.

## Upgrading EBS Volume Types - Lab

### Volumes & Snapshots

- Volumes exist on EBS
  - Virtual Hard Disk
- Snapshots exist on S3
- Snapshots are a point in time copies of Volumes
- Snapshots are incremental - this means that only the blocks that have chnaged since your last snapshot are moved to S3. Only recording the changes
- If it's 1st snapshot, takes time to create

### Snapshots of Root Device Volumes

- To create a snapshot of Amazon EBS volumes that serve as root devices, you should stop the instance before taking the snapshot, however you can take a snapshot while instance is running.
- However you can take a snap while the instance is running.
- You can create AMI's from EBS-backed Instances and Snapshots.
- You can change EBS volume sizes on the fly, including changing the size and storage type.
- Volumes will **ALWAYS** be in the same availability zone as the EC2 instance.
- To move and EC2 volume from one AZ/Region to another, take a snap or an image of it, then copy it to the new AZ/Region.

### Volumes vs Snapshots - Security

- Snapshots of encrypted volumes are encrypted automatically.
- Volumes restored from encrypted snapshots are encrypted automatically.
- You can share snapshots, but only if they are unencrypted.
  - These snapshots can be shared with other AWS accounts or made public.

### EBS vs. Instance Store

- Instance store volumes are sometimes called _Ephemeral Storage_.
- Instance store volumes cannot be stopped. If the underlying host fails, you will lose all your data.
- EBS backed instances can be stopped. You will not los the data on this instance if it is stopped.
- You can reboot both, you will not lose your data.
- By default, both ROOT volumes will be deleted on termination, however with EBS volumes, you can tell AWS to keep the root device volume.

## Load Balancers

- 3 Types of Load Balancers
  - Application Load Balancers
  - Network Load Balancers
  - Classic Load Balancers
- 504 Error means the gateway has timed out. Application is not responding within the idle timeout period
  - Trouble shoot the applcation. Web Server or Database Server?
- If you need IPv4 address of your end user, look fro the X-Forwarded-For header.

- Instances are monitored but ELB are reported as `InService` or `OutofService`.
- Health Checks check the instance health by talking to it.
- ELB's have their own DNS name. You are **never** given an IP address.
- Read the ELB FAQ for Classic Load Balancers

## CloudWatch

- Standard Monitoring - 5 minutes
- Detailed Monitoring - 1 minute

### What can you do with CloudWatch? (Not to be confused with CloudTrail)

- **Dashboards** - Creates awesome dashboards to see/monitor what is happening with your AWS environment.
- **Alarms** - Allows you to set Alarms that notify you when a particular thresholds are hit.
- **Events** - Helps you to repsond to state changes in your AWS resources.
- **Logs** - Helps you to aggregate, monitor and store logs.

## Placement Groups

- A Clustered Placement Group cant span multiple Availibitity Zones.
- A Spread Placement Group can.
- The name you specify for a placement group must be unique within your aws account.
- Only certain types of instances can be launched in a placement group (Compute Optimized, GPU, Memory Optimized, Storage Optimized)
- AWS recommend homogenous instances within placement groups.
- You cant merge placement groups
- You cant move an existing instance into a placement group. You can create an AMI from your existing instance, and then launch a new instance from the AMI into a placement group.

## Lambda

- Lambda scales horizontally (not vertically) automatically. Redundancy
- Lambda functions are independent, 1 event = 1 function
- Lambda is serverless
- Know what services are serverless!!
  - S3
  - API Gateway
  - DynamoDB
- Lambda funcitons can trigger other lambda functions, 1 event can = x functions if functions trigger other functions.
- Architectures can get extremely complicated, AWS X-ray allows you to debug what is happening
- Lambda can do things globally, you can use it to back up S3 buckets to other S3 buckets etc.
- Know your triggers