# Section 2: 1,000 ft Overview

## Part 1. Regions, Availability Zones (AZ), Edge Locations

### Regions

**AWS Region** is a physical, geographical area or location, consisting of 2 or more Availability Zones.

**_Current regions across the world:_**

- US East (N. Virginia) - `us-east-1`
- US East (Ohio) - `us-east-2`
- US West (Northern California) - `us-west-1`
- US West (Oregon) - `us-west-2`
- Canada (Central) - `ca-central-1`
- EU (Frankfurt) - `eu-central-1`
- EU (Ireland) - `eu-west-1`
- EU (London) - `eu-west-2`
- EU (Paris) - `eu-west-3`
- Asia Pacific (Tokyo) - `ap-northeast-1`
- Asia Pacific (Seoul) - `ap-northeast-2`
- Asia Pacific (Osaka-Local) - `ap-northeast-3`
- Asia Pacific (Singapore) - `ap-southeast-1`
- Asia Pacific (Sydney) - `ap-southeast-2`
- Asia Pacific (Mumbai) - `ap-south-1`
- South America (Sao Paulo) - `sa-east-1`

### Availability Zones (AZ)

**AWS Availability Zones** are one or more discrete data centers, each with redundant power, networking and connectivity housed in separate facilities. Deploying your application across multiple Availability Zones is useful for redundancy, low latency and fault tolerance.

**_Regions with multiple Availability Zones:_**

- US East
  - Ohio (3)
  - North Virginia (6)
- US West
  - Oregon (3)
  - Northern California (3)
- Canada
  - Central (3)
- South America
  - Sao Paulo (3)
- Europe
  - Ireland (3)
  - Frankfurt (3)
  - London (3)
  - Paris (3)
- Asia Pacific
  - Singapore (3)
  - Seoul (2)
  - Tokyo (4)
  - Mumbai (2)
  - Sydney (3)
  - Beijing (2)
  - Ningxia (2)

### Edge Locations

**AWS Edge Locations** are locations around the world meant for caching content, enhancing the user experience, reducing latency. Edge locations are specifically used by AWS Cloudfront and AWS CDN. Every Region is has its own set Availability Zone's and Edge Locations.

## Part 2. AWS Services Overview

Compute:
    EC2 - elastic compute cloud
    EC2 Container Services - containerization docker
    Elastic Beanstalk - plug and play - for developers
    Lambda (server less) - code/functions uploaded to the cloud to run at different points
    Lightsail - plug and play
    Batch - batch computing in the cloud

Storage:
    S3 - simple storage service - object based storage - buckets
    EFS - elastic file system
    Glacier - data archival 
    Snowball - large amounts of data to aws data center
    Storage gateway - VM installed in datacenter or office - replicate info to S3

Databases:
    RDS - relation database service - postgres, mysql, oracle
    DynamoDB - non relational db
    Elasticache - cache things from db
    Redshift - data warehousing business intelligence, complex queries
    
Migration:
    AWS Migration Hub - tracking service for moving to aws
    Application Discover Service - track applications and dependency
    Database Migration Service - migrate db from on premise to AWS
    Server Migration Service - migrate server to AWS cloud
    Snowball - in between storage and migration

Networking and Content Delivery:
    VPC (highlight) - Amazon virtual private cloud - virtual datacenter - configure avail zones, firewall, network acl etc.
    Cloudfront - AWS content delivery network, store assets specific regions around the world
    Route 53 - AWS DNS service - lookup ip to get ipv4 and ipv6 address
    API Gateway - Serverless way of creating own api
    Direct Connect - Dedicated line from office directly into amazon, connects to VPC

Developer Tools:
    Codestart - project management, CI toolchain, collaborate
    Codecommit - store code, like github    
    Codebuild - compile and run tests, produce package
    Code deploy - deployment service to ec2 instance
    Codepipeline - automate and visualize steps to release software
    X-ray - debug and analyze server less application
    Cloud9 - IDE environment in browser

## Part 3. AWS Services Overview (Continued)

Management tools:
    Cloudwatch - Monitoring service
    Cloudformation - solutions architect specific - scripting infrastructure - turn infrastructure to code
    Cloudtrail - log changes to aws environment
    Config - monitors config of aws environment
    Opswork - similar to elastic beanstalk - chef and puppet to automate environments
    Service Catalog - manage a catalog of IT services
    Systems manager - interface for managing aws resources - group resources
    Trusted Advisor - advice around security, advice for aws services and resources, accountant like
    Managed Services - manage service for aws cloud
    
    ** Recap for exam - cloudformation, cloudtrail, cloudtrail, trusted advisor

Media Services:
    Elastic transcoder - takes media and resizes on different devices
    Media convert - file based video transcoding with broadcast grade features
    Media live - broadcast grade live video processing service. tv internet connected multiscreen
    Media Package - protect content over internet 
    Media Store - media storage, optimized for media
    Media Tailor - target advertising into video streams with out harming broadcast

Machine Learning:
    Sage maker - easy for deep learning when coding for environment
    Comprehend - sentiment analysis on products. good or bad?
    Deep lens - computer vision on camera, recognition, physical piece of hardware
    Lex - powers alexa, AI 
    Machine Learning - throw dataset to AWS cloud and predict outcome
    Polly - text to speech, voices sound real, accents
    Rekognition - upload file, tells you what is in the file
    Amazon translate - translate to other langs
    Amazon transcribe - hard of hearing, speech recognition, speech to text

Analytics: 
    Athena - SQL queries ins S3 buckets, serverless
    EMR - elastic map reduce - processing large amounts of data, chops data up for analysis
    Cloudsearch - search service
    Elastic Search service - search service
    Kinesis - solutions architect highlight, ingesting large amounts data
    Kinesis Video streams - ingesting streams and analyze    
    Quicksight - business intelligence tool
    Datapipeline - moving data between different services
    Glue - ETL (extract transform load)

## Part 4. AWS Services Overview (Continued)

Security Identity and Compliance:
    IAM - identity access management
    Cognito - device authentication, oath, after authenticated, use aws services
    Guard Duty - monitor for malicious activity
    Inspector - install on vm or instances, test against it, schedule
    Macie - Scan s3 buckets and looks for sensitive info and alert
    Certificate Manager - ssl cert for free, manage ssl cert
    Cloud HSM - cloud hardware security module - dedicate bits of hardware to store keys to authenticated
    Directory Service - integration ms active service to aws services
    WAF - web application firewall - at application layer to stop attacks, XSS, sql injection
    Shield - by default for cloud front - ddos mitigation, prevent ddos attacks
    Artifact - portal to download aws client reports, manage agreements 
    
    **Key security services for exam: IAM, inspector, cloudHMS, directory services, waf, shield, cert manager

Mobile Services: 
    Mobile hub - management console for mobile app for aws services
    AWS Pinpoint - targeted push notifications
    AWS Appsync - atomically updates data in web or mobile in real time
    Device Farm - test apps on real device, iOS, android
    Mobile Analytics - analytics service for mobile

AR/VR:
    Sumerian - tools to create environment, super new

Application Integration:
    Step functions - manage lambda functions and ways to go through it
    Amazon MQ - message queue
    SNS - notification services
    SQS - decouple infrastructure, queue
    SWF - workflow job creation

Customer Engagement:
    Connect - contact center as a service, call center
    Simple Email Service - email service, send grid, mailchimp

Business Productivity:
    Alexa for business - manager for business needs
    Amazon chime - google hangouts like
    Work Docs - dropbox for AWS
    Work Mail - Office 365 like
   
Desktop and App streaming:
    Workspaces - VDI solution, run OS in aws cloud
    App stream 2.0 - streaming application to desktop of device
    
IOT:
    iOT - devices sending sensor information
    iOT Device Management - device management
    Amazon FreeRTOS - OS for microcontrollers
    Greengrass - ?? 

Game Development:
    Gamelift - service to develop games

## What Services Will Be Tested On The Exam??

Analytics
Management Tools
Migration
Compute
AWS Global infrastructure
Storage
Databases
Network and Content delivery
Security and Identity compliance
Application Integration
Desktop and App streaming

## Links

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

- [https://www.linuxnix.com/amazon-aws-regions-vs-availability-zones-vs-edge-locations-vs-data-centers/](https://www.linuxnix.com/amazon-aws-regions-vs-availability-zones-vs-edge-locations-vs-data-centers/)