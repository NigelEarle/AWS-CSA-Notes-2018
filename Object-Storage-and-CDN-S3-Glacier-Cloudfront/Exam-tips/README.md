# Exam Tips

## S3, Glacier

### General

- S3 is object based, allows you to upload files
- Files can be 0B up to 5TB
- Unlimited storage
    - Files are stored in Buckets (folder)
    - S3 uses universal namespace. bucket names must unique
- Control access to buckets using either a bucket ACL routing Bucket Policies
- By default, **BUCKETS ARE PRIVATE AND ALL OBJECTS STORED INSIDE THEM ARE PRIVATE**

### Reads and Writes

- Read after Write consistency for PUTS of new objects
- Eventual consistency of overwrite PUTS and DELETES (can take time to propagate)

### Storage Class Tiers

- S3 (normal) - durable, immediately available, frequently used
- S3  IA (infrequent access) - like normal S3 tier but infrequently accessed
- S3 Reduced Redundancy Storage (RRS) - data storage that is easily reproducible, such as thumb nails etc
- Glacier (separate product from S3) - Used to archive data. Low and slow retrieval 

### Core fundamentals of S3 Object

- key (name)
- value (data)
- version id
- metadata 
- subresources
	- ACL 
	- Torrent
- Object based storage only
- Not installable on apps, DB or OS
- Success uploads will generate HTTP 200 status code
- Read S3 FAQ before taking the exam. it comes up a lot

### Encryption

- Client side encryption
- Server side encryption
	- encryption with amazon s3 managed keys (SSE-S3)
	- encryption with KMS (SSE-KMS)
	- encryption with Customer Provided Keys (SSE-C)

### Versioning

- Stores all version of an object (all writes/udpates and even if you delete the object). Must manually delete object if you wish to delete a version
- Great back up tool
- Once enabled, cannot be disabled, only suspended
- Integrates with Lifecycle rules
- Versioning MFA Delete capability, uses mulit-factor authentication, can be used to provide an additional layer of security

### Cross Region Replication

- Versioning must be enabled on source and destination buckets
- Regions must be unique, Cannot cross region to same region
- Files are not replicated automatically. All subsequent updated files will be replicated automatically.
- You cannot replicate to multiple buckets - daisy chaining (currently).
- Delete markers are replicated
- Deleting individual versions or delete markers will not be replicated
- Understand what CRR at high level

### Lifecycle management

- Can be used with or without versioning
- Can be applied to current version as well as previous versions
- Acceptable actions
	- Transition to Standard - IA Storage Class (128kb and 30 days after creation date)
	- Archive to Glacier - 30 days after IA Storage if relevant
	- Permanently delete
- Understand at high level

## CDN Cloudfront

- Edge Location - Location where content will be cached - separate from AWS Region
- Origin - Origin of all files the the CDN will distribute. Can be S3, EC2, Elastic Load Balancer, Route 53 or your own custom server.
- Distribution - Name given to the CDN which consistsof a collection of Edge Locations
	- Web Distribution - Typically used for websites
	- RTMP - Used for media streaming
- Edge Locations are not just for READ only, you can write (PUT) too!
- Object are cached for life of TTL (Time To Live)
- Can clear cached objects, but you will be charged

## Storage Gateway

- File Gateway - For flat files, stored directly on S3.
- Volume Gateway:
  - Stored Volumes - Entire dataset is stored on site and is asynchronously backedup to S3
  - Cached Volumes - Entire dataset is stored on S3 and the most frequent accessed data is cached on site.
- Gateway Virtual Tape Library
  - Used for backup and uses popular backup applications like NetBackup, Backup Exec, Veeam etc.

## Snowballs

- Understand what a Snowball is
- Understand what Import Export is
- Snowball can
	- Import to S3
	- Export from S3