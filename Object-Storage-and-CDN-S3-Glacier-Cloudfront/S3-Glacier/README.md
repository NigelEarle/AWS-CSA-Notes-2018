# S3 - HEAVY EXAM TOPIC

---

S3 is a safe place to store your static files being one the oldest services of AWS. It is an object based storage where your data is spread across multiple devices.

S3 allows you to upload, where files can be from 0 bytes to 5TB. If an upload is successful, you will recieve an HTTP status code of `200`.
It is capable of unlimited storage. All files are stored into 'Buckets' which is basically an S3 term for folders.

S3 uses a universal namespace meaning all names must be **_globally_** unique.

Example S3 URL:

**`https://s3-eu-west-1.amazonaws.com/[bucket-name]`**

## Data Consistency

S3 maintains **_Read After Write_** consistency for PUTS of new objects. Meaning, as soon a new object is uploaded or written, it is available to read/view.

When performing overwrite PUTS and DELETES, these updated and/or deleted objects can take time to propagate because, also known as **_Eventual Consistency_**. These type of updates are known as **_Atomic_** - fetching these resources could be old or new.

## S3 Object - Key, Value Store

- Key -> Name of object to be stored
- Value -> Data being stored - made up of a sequence of bytes
- Version ID -> Version signifier
- Metadata -> Data about the data you are storing - date stored, size, 
- Subresource
    - Access Control Lists
    - Torrents

## S3 Basics 

- Built for 99.99% availability for the S3 platform
- Amazon guarantee 99.9% availability - always available
- Amazon guarantees 99.99999999999% (11 9’s) durability for S3 info
- Tiered storage
- Lifecycle management
- Versioning
- Encryption
- Secure data using access control lists bucket policies

### Storage Tiers 

- **S3 (Normal)**
	- 99.99% availability, 99.(11 9’s )
	- durable, reliable - stored redundantly across multiple devices in multiple facilities and is designed to sustain the loss of 2 facilities concurrently

- **S3 IA (infrequent access)**
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
- Takes advantage of AWS Cloudfront global, distributed edge locations.
- When data arrives at an edge location, it is then routed to Amazon S3 over an optimized network path.
