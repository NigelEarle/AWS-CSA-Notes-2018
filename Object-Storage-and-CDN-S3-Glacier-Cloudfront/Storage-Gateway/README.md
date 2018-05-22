# Storage Gateway

**Understand at theoretical level**

Service that connects an on-premise software appliance with cloud based storage to provide seamless and secure integration between an organization's on-premise IT environment and AWS's storage infrastructure. The service enables you to securely store data to AWS cloud for scalable and cost-effective storage. Replicates your data to specifically S3 bucket.

Downloaded as virtual machine (VM) that you install on a host in your datacenter. Storage Gateway supports either VMware ESXi or MS Hyper-V. Once you've installed your gateway and associate with AWS account through activation process, you can use the AWS Management Console to create the storage gateway option this is right for you.

### Four Types of Gateway Storage

1. File Gateway (NFS)
	- Store flate files in S3 through a Network File System (NFS) mount point. Ownershi, permissions, and timestamps are durably stored in S3 in the user-metadata of the object associated with the file. Once objects are transferred to S3, they can be managed as native S3 objects, and bucket policies such as versioning, lifecycle management, and cross-region replication apply directly to objects stored in your bucket.
2. Volume Gateway (iSCSI)
	- Block based storage, storage you would run OS, DB's on. Not stored in S3.
	- Stored Volumes - Store entire copy of dataset on site.
	- Cached Volumes - Store most recent accessed data.
3. Tape Gateway (VTL)