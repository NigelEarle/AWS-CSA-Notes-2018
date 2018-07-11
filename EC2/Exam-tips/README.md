# Exam Tips

## EC2 Instance Run Down

- **On Demand** - allows you to pay a fixed rate by the hour (or second) with not commitement

- **Reserved** - provides you with the capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 year terms

- **Spot** - Enables you to bid whatever price you want for instane capacity, providing for even greater savings if your applications have flexible start and end times

- **Dedicated Hosts** - Physical EC2 server dedicated for your use. Dedicated Hosts can help reduce costs by allowing you to use your existing server-bound software license

**_Important Note!!_**

If a Spot instance is terminated by Amazon EC2, you will not be charged for a partial hour of usage. However, if you terminatethe instance yourself, you will be charged for the complete hour in which the instance ran.

## Instance Types

- **F.** - FGPA
- **I.** - IOPS
- **G.** - Graphics
- **H.** - High Disk Throughput
- **T.** - Cheap General Purpose (think T2 Micro)
- **D.** - Density
- **R.** - Ram
- **M.** - Main choice for general purpose applications
- **C.** - Compute
- **P.** - Grahics(Pics)
- **X.** - Extreme Memory

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
- ELB's have their own DNS name. You are **never** given an IP address
- Read the ELB FAQ for Classic Load Balancers

_Note: ELB's do not have IP Addresses, only found by DNS namespace_

## CloudWatch

- Standard Monitoring - 5 minutes
- Detailed Monitoring - 1 minute

### What can you do with CloudWatch? (Not to be confused with CloudTrail)

- **Dashboards** - Creates awesome dashboards to see/monitor what is happening with your AWS environment.
- **Alarms** - Allows you to set Alarms that notify you when a particular thresholds are hit.
- **Events** - Helps you to repsond to state changes in your AWS resources.
- **Logs** - Helps you to aggregate, monitor and store logs.

## Placement Groups

- A Clustered Placement Group can not span multiple Availibitity Zones.
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
- Know your triggers - connecting AWS services

## Summary (TLDR;)

- Know the differences between EC2 instances
  - On Demand
  - Spot
  - Reserved
  - Dedicated hosts

**_Remember with Spot Instances_**

- If you terminate the instance, you pay for the hour
- If AWS terminates the instance, you get the hour it was terminated for free.

### EC2 Instance Types

**F.I.G.H.T.D.R.M.C.P.X** (Use Reference)

### EBS (Elastic Block Storage)

**Consists of:**

- SSD, General Purpose - GP2 - Up to 10,000 IOPS
- SSD, Provisioned IOPS - IO1 - More than 10,000 IOPS
- HDD, Throughput Optimized - ST1 - frequently accessed workloads
- HDD, Cold - SC1 - Less frequently accessed data
- HDD, Magnetic - Standard - Cheap, Infrequently accessed storage.

**IMPORTANT NOTE:** You cannot mount 1 EBS volume to mulitple EC2 instances; Instead use EFS (Elastic File Storage)

### Lab Tips! 

- Termination Protection is turned off by default, you must turn this on!
- On a EBS-backed instance, the default action is for the root EBS volume to be deleted when the instance is terminated.
- EBS backed Root volumes can now be encrypted using AWS API or console, or you can use a third party tool (bitlocker etc.) to encrypt the root volume.
- Additional volumes can be encrypted

### Volumes vs. Snapshots

- Volumes exist on EBS; Virtual Hard Disks
- Snapshots exist on S3
- You can take a snapshot of a volume, this will store that volume on S3
- Snapshots are point-in-time copies of volumes
- Snapshots are incremental. This means that only the blocks that have changed since your last snapshot are moved to S3
- If taking your first snapshot, may take some time

**Security**

- Snapshots of encrypted volumes are encrypted automatically
- Volumes restored from encrypted snapshots are encrypted automatically
- You can share snapshots, but only if they are unencrypted
  - These snapshots can be shared with other AWS accounts or made public

**Snapshots or Root Device Volumes**

- To create a snapshot for EBS volumes that serve as root devices, you should stop the instance before taking the snapshot.

### EBS vs Instance Store

- Instance Store Volumes are sometimes called Ephemeral Storage
- Instance Store Volumes cannot be stopped. If the underlying host fails, you will lose your data.
- EBS backed instances can be stopped. You will not lose the data on this instance if it is stopped.
- You can reboot both, you will not lose your data
- By default, both ROOT volumes will be deleted on termination. However, with EBS volumes, you can tell AWS to keep the root device volume.

### How can you take a snapshot of a RAID Array?

**Problem** - Take a snapshot, the snapshots excludes data held in the cache by applications and the OS. This tends not to matter on a single volume. However, using multiple volumes in a RAID array, this can be a problem due to interdependencies of the array.

**Solution** - Take an application consistent snapshot.

- Stop the application from writing to disk
- Flush all caches to the disk.

How is this accomplised?

- Freeze the file system
- Unmount the RAID array
- Shutting down the associated EC2 instance.

### AMI (Amazon Machine Image)

AMIs are regional. You can only launch an AMI from the region in which its stored. However you can copy AMIs to other regions using the console, command line, or the Amazon EC2 API

- Standard monitoring - 5 min
- Detailed monitoring - 1 min

- Cloudwatch is for **performance monitoring**
- Cloudtrail is for **auditing**

### Cloudtrail

 - **Dashboards** - Cloudwatch creates awesome dashboards to see what is happening with your AWS envrionment
- **Alarms** - Allows you to set alarms when particular thresholds are hit.
- **Events** - Helps you to respond to state changes in your AWS resources.
- **Logs** - Helps you to aggregate, monitor, and store logs

### Roles

- Roles are more secure than storing your access key and secret access key on individual instances.
- Roles are easier to manage
- Roles can be assigned to an EC2 instance after it has been provisioned using both the command line and the AWS console
- Roles are universal - they can be used in any region

### Instance Metadata

- Used to get information about an instance (public IP, DNS etc)
  - `curl http://169.254.169.254/latest/meta-data`
  - `curl http://169.254.169.254/latest/user-data`

### EFS (Elastic File System)

- Supports the Network File System version 4 (NFSv4) protocol
- You only pay for the storage you use (no pre-provisioning required)
- Can scale up to petabytes
- Can support thousands of concurrent NFS connections
- Data is stored accross multiple AZs within a region
- Read after Write consistency

### Lambda

- Lambda is a compute service where you can upload you code and create a Lambda function.
- Takes care of provisioning and managing servers that you use to run your code.
- Need not worry about OS, patching, scaling etc.

**_Use Lambda as:_**

- Event driven compute service where Lambda runs your code in response to events. These events could be changes in an S3 bucket or Dynamo DB table.
- A compute service to run your code in response to HTTP requests using API Gateway or API calls made using AWS SDKs

### Placement Groups

**Know the differences between and why you would use...**

- Clustered Placement Groups
- Spread Placement Groups