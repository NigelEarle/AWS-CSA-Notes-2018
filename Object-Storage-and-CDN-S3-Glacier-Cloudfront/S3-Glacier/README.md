# S3 - HEAVY EXAM TOPIC

S3 is a safe place to store your static files being one the oldest services of AWS. It is an object based storage where your data is spread across multiple devices.

S3 allows you to upload, where files can be from 0 bytes to 5TB. If an upload is successful, you will recieve an HTTP status code of `200`.
It is capable of unlimited storage. All files are stored into 'Buckets' which is basically an S3 term for folders.

S3 uses a universal namespace meaning all names must be **_globally_** unique.

_Example S3 URL:_

**`https://s3-eu-west-1.amazonaws.com/[bucket-name]`**

## Data Consistency

S3 maintains **_Read After Write_** consistency for PUTS of new objects. Meaning, as soon a new object is uploaded or written, it is available to read/view.

When performing overwrite PUTS and DELETES, these updated and/or deleted objects can take time to propagate because, also known as **_Eventual Consistency_**. These type of updates are known as **_Atomic_** - fetching these resources could be old or new.

## S3 Object - Key, Value Store

- Key - Name of object to be stored
- Value - Data being stored - made up of a sequence of bytes
- Version ID - Version signifier
- Metadata - Data about the data you are storing - date stored, size, 
- Subresource
    - Access Control Lists
    - Torrents

## S3 Basics 

- Built for 99.99% availability for the S3 platform
- Amazon guarantee 99.9% availability - always available
- Amazon guarantees 99.99999999999% (11, 9’s) durability for S3 information
- Tiered storage
- Lifecycle management
- Versioning
- Encryption
- Secure data using Access Control Lists bucket policies

### Storage Tiers

- **S3 (Normal)**
	- 99.99% availability, 99.(11 9’s )
	- durable, reliable - stored redundantly across multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently

- **S3 IA (Infrequent Access)**
	- Used for data that is accessed less frequently but requires rapid access when needed
	- Lower fee than S3 but, are charged a retrieval fee

- **S3 Reduces Redundancy Storage (RRS)** 
	- Designed to provide 99.99% durability and 99.99% availability of objects over a given year.

- **Glacier (Separate product from S3)**
	- Very cost effective but used for data archival only
	- Generally takes 3 - 5 hours to restore from glacier
    - Stores data for as low as .01G a month
    - Optimized for data that is infrequently accessed and for which retrieval times of 3 to 5 hours are suitable (slow retrieval).

### S3 Charges

- Storage
- Requests
- Storage Management Pricing
- Data transfer pricing
- Transfer Acceleration

#### Transfer Acceleration

- Enables fast, easy and secure transfers of files over long distances between you and your end users and an S3 bucket.
- Takes advantage of AWS CloudFront global, distributed edge locations.
- When data arrives at an edge location, it is then routed to Amazon S3 over an optimized network path.

## S3 Encrytion and Security

By default all newly created buckets are **PRIVATE**. You need to manually change permissions to access resources.

You can set policies and permissions using either Access Control Lists or Bucket Policies. 

You have the ability to make a bucket private but all certian objects in that bucket to be public.

### Logging

S3 buckets can be configured to create access logs which log all requests made to that bucket. This can be done to another bucket through cross account access.

### Encryption

**4** different methods and **2** types of encryption for S3 buckets.

1. **In Transit** - from client uploading to S3 bucket.
	- Using SSL/TLS encryption. HTTPS

2. **At Rest**
	- Server Side Encryption
		- **SSE-S3** - S3 Managed key. Each object is encrypted with a unique key employing strong multi-factor encryption with rotating master key (AES-256 encryption).
		- **SSE KMS** - AWS Key Management Service, Managed Keys. Similar to SSE-S3. Separate permissions for envelope key - key that protects data encryption key. Audit trail - when keys were used and who were using.
		- **SSE-C** - Server Side Encryption with Customer Provided Keys. You manage encryption key.
	- Client Side Encryption
		- Encrypt data on client side and upload to S3

## Links

- [https://aws.amazon.com/s3/](https://aws.amazon.com/s3/)
- [https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
- [https://aws.amazon.com/s3/faqs/](https://aws.amazon.com/s3/faqs/)
- [https://aws.amazon.com/s3/storage-classes/](https://aws.amazon.com/s3/storage-classes/)
- [https://aws.amazon.com/glacier/faqs/](https://aws.amazon.com/glacier/faqs/)