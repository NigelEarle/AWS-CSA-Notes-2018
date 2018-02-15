# S3

HEAVY EXAM TOPIC

S3 is a safe place to store your files
Object based storage
Data is spread across multiple devices

S3 allows you to upload files
Files can be from 0 bytes to 5TB
Unlimited storage
Buckets are folders
S3 is a universal namespace. Names must be unique globally
creates dns address - ex. https://s3-eu-west-1.amazonaws.com/[bucket-name]
if upload is successful - will receive a 200 http response

DATA CONSISTENCY
    read after write consistency for PUTS of new objects
    eventual consistency for overwrite PUTS and DELETES can take some time to propagate
        takes time to propagate because. not immediate
    Updates are atomic - updates could be new or old data.
    
S3 Object - Key Value store
    key - name of object
    value - data made up of sequence of bytes
    version id - versioning
    metadata - data about data ur storing
    subresource
        access control lists
        torrent

Built for 99.99% availability for the S3 platform
Amazon guarantee 99.9% availability - always available
Amazon guarantees 99.99999999999% (11 9’s) durability for S3 info
Tiered storage
Lifecycle management
Versioning
Encryption
Secure data using access control lists bucket policies

Storage Tiers 
    S3 - Normal S3, 99.99% availability, 99.(11 9’s ) durability, stored redundantly across multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently.

    S3 IA (infrequent access) - for data that is accessed less frequently but requires rapid access when needed. lower fee than s3 but you are charged a retrieval fee.

    Reduces Redundancy Storage (RRS) - Designed to provide 99.99% durability and 99.99% availability of objects over a given year.

    Glacier - Very cheap but used for data archival only. Takes 3 - 5 hours to restore from glacier
        It’s own separate product from S3. Extremely low cost storage service for data archival. Stores
        data for as low as .01G a month and is optimized for data that is infrequently accessed and for
        which retrieval times of 3 to 5 hours are suitable.

S3 Charges
    Storage
    Requests
    Storage Management Pricing
    Data transfer pricing
    Transfer Acceleration

Transfer Acceleration
    Amazon S3 Transfer Acceleration enables fast, easy and secure transfers of files over long
distances between you and your end users and an S3 bucket. Transfer Acceleration takes
advantage of Amazon Cloudfront’s global distributed edge locations. As the data arrives at an edge location, data is routed Amazon S3 over an optimized network path.

Exam Tip
    S3 is object based and allows you to upload files
    Files can be 0B up to 5TB
    Unlimited storage
    Files are stored in Buckets (folder)
    S3 uses universal namespace. bucket names must unique

    Read after Write consistency for PUTS of new objects
    Eventual consistency of overwrite PUTS and DELETES (can take time to propagate)
    
    S3 storage classes tiers
        S3 (durable, immediately available, frequently used)
        S3  IA (durable, immediately available, infrequently accessed)
        S3 Reduced Redundancy Storage (data that is easily reproducible, such as thumb nails etc)
        Glacier - Archival data

    Core fundamentals of S3 Object
        key (name)
        value (data)
        version id
        metadata 
        subresources
            ACL 
            Torrent
    Object based storage only
    Cannot install apps, db or os
    Success uploads will generate HTTP 200 status code
    Read S3 FAQ before taking the exam. it comes up a lot
    
    Encryption
      Client side encryption
      Server side encryption
        encryption with amazon s3 managed keys (SSE-S3)
        encryption with KMS (SSE-KMS)
        encryption with Customer Provided Keys (SSE-C)
    
    Control access to buckets using either a bucket ACL orusing Bucket Policies

    BY DEFAULT BUCKETS ARE PRIVATE AND ALL OBJECTS STORED INSIDE THEM ARE PRIVATE


