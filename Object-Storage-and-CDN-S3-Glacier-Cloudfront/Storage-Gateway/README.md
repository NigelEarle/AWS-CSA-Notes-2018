# Storage Gateway

**_Understand at theoretical level_**

## What is Storage Gateway?

A Service that connects an on-premise software appliance with cloud based storage to provide seamless and secure integration between an organization's on-premise IT environment and AWS's storage infrastructure.

The service enables you to securely store data to AWS cloud for scalable and cost-effective storage. Replicates your data to specifically S3 bucket.

Downloaded as virtual machine (VM) that you install on a host in your datacenter. Storage Gateway supports either VMware ESXi or MS Hyper-V. Once you've installed your gateway and associate with AWS account through activation process, you can use the AWS Management Console to create the storage gateway option this is right for you.

## Four Types of Gateway Storage

### File Gateway (NFS)

Store flat files in S3 through a Network File System (NFS) mount point. Ownership, permissions, and timestamps are durably stored in S3 in the user-metadata of the object associated with the file.

Once objects are transferred to S3, they can be managed as native S3 objects, and bucket policies such as versioning, lifecycle management, and cross-region replication apply directly to objects stored in your bucket.

### Volumes Gateway (iSCSI)

The volume interface presents your applications with disk volumes using the iSCSI block protocol.

Data written to these volumes can be asynchronously backed up as point-in-time snapshots of your volumes, and stored in the cloud as AWS EBS (Elastic Block Store - VM) snapshots.

Snapshots are incremental backups that capture only the changed blocks. All snapshot storage is also compressed to minimize your storage charges.

_NOTE: iSCSI is block based storage. Store OS, DB's. Think of as virtual hard disk_

#### Stored Volumes

Stored volumes let you store your primary data locally, while asynchronously backing up that data to AWS. Stored volumes provide your on-premise applications with low-latency access to their entire datasets, while providing durable, off-site backups.

You can create storage volumes and mount them as iSCSI devices from your on-premises application servers. Data written to your stored volumes is stored on your on-premises storage hardware.

This data is asynchronously backed up to S3 in the form of AWS EBS (Elastic Block Store) snapshots 1 GB - 16 TB in size for Stored Volumes.

#### Cached Volumes

Cached volumes let you use S3 as your primary data storage while retaing frequently accessed data locally in your storage gateway.

Cached volumes minimize the need to scale your on-premise storage infrastucture, while still providing your applications with low-latency access to their frequently accessed data.

You can create storage volumes up to 32Tb in size and attach to them as iSCSI devices from your on-premises application servers. Your gateway stores data that you write to these volumes in S3 and retains recently read data in your on-premises storage gateways cache and upload buffer storage. 1 GB - 32 TB size for cached volumes.

**_TLDR;Volume Gateway takes virtual hard disks that are on premise and back them up to AWS_**

### Tape Gateway (VTL)

Offers a durable, cost-effective solution to archive your data in AWS cloud. The VTL interface it provides lets you leverage your existing tape-based backup application infrastructure to store data on virtual tape cartridges that you create on your tape gateway.

Each tape gateway is preconfigured with a media changer and tape drivers, which are available to your existing client backup applciations as iSCSI devices. You add tape cartridges as you need to archive your data. Supported by Netbackup, Backup Exec, Veeam etc.

## Tips (Summary)

- File Gateway - For flat files, stored directly to S3
- Volume Gateway:
  - Stored Volumes - Entire dataset is stored on site and is asynchronously backed up to S3
  - Cached Volumes - Entire dataset is stored on S3 and the most frequently accessed data is cached on site.
- Gateway Virtual Tape Library (VTL)
  - Used for backup and uses popular backup applications like NetBackup, Backup Exec, Veeam etc.

## Links

- [https://aws.amazon.com/storagegateway/faqs/](https://aws.amazon.com/storagegateway/faqs/)
- [https://aws.amazon.com/blogs/aws/the-aws-storage-gateway-integrate-your-existing-on-premises-applications-with-aws-cloud-storage/](https://aws.amazon.com/blogs/aws/the-aws-storage-gateway-integrate-your-existing-on-premises-applications-with-aws-cloud-storage/)
