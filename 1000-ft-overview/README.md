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

## Links

- [https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

- [https://www.linuxnix.com/amazon-aws-regions-vs-availability-zones-vs-edge-locations-vs-data-centers/](https://www.linuxnix.com/amazon-aws-regions-vs-availability-zones-vs-edge-locations-vs-data-centers/)