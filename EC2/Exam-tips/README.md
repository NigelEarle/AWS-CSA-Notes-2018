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
