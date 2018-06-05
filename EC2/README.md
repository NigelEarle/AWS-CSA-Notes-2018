# EC2 (Elastic Cloud Compute)

AWS EC2 is a web service that provides resizable compute capacity in the cloud. EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.

EC2 has changed the economics of cloud computing by allowing you to pay only for capacity that your actually use. EC2 provides developers the tools to build failure resistent applications and isolate themselves from common failure scenarios.

## Pricing Options

### On Demand

Allows you to pay a fixed rate by the hour (or by the second) with no commitment.

**_Use Cases_**

- Perfect for users that want the low cost and flexibility of EC2 without any of the up front payment or long term commitment
- Applications with short term, spiky or unpredictable workloads that cannot be interrupted
- Applications being developed or tested on EC2 for the first time

### Reserved

Provides you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 year terms.

**_Use Cases_**

- Applications with steady state or predictable usage
- Applications that require reserved capacity
- Users can make up front payments to reduce their totoal computing costs even further
  - Standard RIs (Up to 75% off on-demand)
  - Convertible RIs (Up to 54% off on-demand) feature the capability to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or greater value. Ability to go from CPU intensive instance to Memory intensive.
  - Scheduled RIs are available to launch within the time window you reserve. This option allows you to match your capacity reservation to predictable recurring schedule that only requires a fraction of a day, a week, or a month.

### Spot

Enables you to bid whatever price you want for an instance capacity, providing for even greater savings if your applications have flexible start and end times.

**Use Cases**

- Applications that have flexible start and end times
- Applications that are only feasible at very low compute prices
- Used for single compute instances to save on costs compared to 9-5 during the week.
- Users with an urgent need for a large amount of additional computing capacity.

### Dedicated Hosts

Physical EC2 server dedicated for your use. Dedicated Hosts can help you reduce costs by allowing yout to use your existing server-bound software licenses.

**Use Cases**

- Useful for regulatory requirements that may not support multi-tenant vitualization.
- Great for licensing which does not support multi-tenancy or cloud deployments
- Can be purchased On-Demand (hourly).
- Can be purchased as a Reservation for up to 70% off the On-Demand price.

## EC2 Instance Types

**_No need to memorize for associate exams_**

| Family | Specialty                     | Use Cases                       |
| :------:|:-----------------------------:| :------------------------------:|
| F1     | Field Programmable Gate Array | Genomics research, financial analytics, real-time video processing, big data etc|
| I3      | High Speed Storage            | NoSQL DBs, Datawarehousing |
| G3      | Graphics Intensive            | Video Encoding / 3D Application Streaming|
| H1      | High Disk Throughput          | MapReduce-based workloads, distributed file systems such as HDFS and MapR-FS |
| T2      | Lowest Cost General Purpose   | Web Servers / Small DBs |
| D2      | Dense Storage                 | Fileservers / Data Warehousing / Hadoop |
| R4      | Memory Optimization           | Memory Intensive Apps/DBs |
| M5      | General Purpose               | Application Servers |
| C5      | Compute Optimized             | CPU Intensive Apps / DBs |
| P3      | Graphics / General Purpose GPU | Machine Learning, Bit Coin Mining etc |
| X1      | Memory Optimized               | SAP HANA / Apache Spark |


**How to remember EC2 instance types F.I.G.H.T.D.R.M.C.P.X (after 2017 reinvent):**
  - **_F_** - FGPA
  - **_I_** - IOPS
  - **_G_** - Graphics
  - **_H_** - High Disk Throughput
  - **_T_** - Cheap General Purpose (think T2 Micro)
  - **_D_** - Density
  - **_R_** - Ram
  - **_M_** - Main choice for general purpose applications
  - **_C_** - Compute
  - **_P_** - Grahics(Pics)
  - **_X_** - Extreme Memory

## EBS - Elastic Block Storage

Amazon EBS allows you to create storage volumes and attch them Amazon EC2 instances. Once attached, you can create a file system on top of theses volumes, run a database, or use them in any other way you would use a block device. EBS volumes are placed in a specific Availibility Zone, where they are automatically replicated to protect you from the failure of a single component.

_TLDR; A disk in the cloud that you attach to your EC2 instances_

### EBS Volume Types

- General Purpose SSD (GP2)
  - General purpose, balances both price and performance.
  - Ratio of 3 IOPS per GB with up to 10,000 IOPS and the ability to burst up to 3000 IOPS for extended periods of time for volumes at 3334 GB and above
- Provisioned IOPS SSD (IO1)
  - Designed for I/O intensive applications such as large relational or NoSQL databases.
  - Use if you need more than 10,000 IOPS
  - Provision up to 20,000 IOPS per volume
  - Super high performant
- Throughput Optimized HDD (ST1)
  - Big Data
  - Data warehouses
  - Log processing
  - Cannot be a boot volume
- Cold HDD (SC1)
  - Lowest cost storage for infrequently accessed workloads
  - File server
  - Cannot be a boot volume
- Magnetic (Standard)
  - Lowest cost per GB of all EBS volume types that is bootable. Magnetic volumes are ideal for workloads where data is accessed infrequently, and applications where the lowest storage cost is important

## Let's get our hands dirty! Launch an EC2 instance lab!

### Summary

- Termination protection is turned off by default, you _MUST_ turn it on.
- On an EBS-backed instance, the default action is for the root EBS volume to be deleted when the instance is terminated
- EBS Root Volume of you DEFAULT AMI's cannot be encrypted. You can also use a third party tool (such as bit locker) to encrypt the root volume, or this can be done when creating AMI's (future lab) in the AWS console or using the API.
- Additional volumes can be encrypted.

## Security Groups

### What is a Security Group?

A security group is a virtual firewall that's controlling traffic to your EC2 instance. When you first launch as EC2 instance you associate it to 1 or more instances. You have the ability to add rules to these security groups that allows traffic to or from these instances.