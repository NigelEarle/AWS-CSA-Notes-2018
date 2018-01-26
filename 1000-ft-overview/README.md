# Section 2: 1,000 ft Overview

## Part 1. Regions, Availability Zones (AZ), Edge Locations

### Regions

An AWS Region is a physical, geographical area or location, consisting of 2 or more Availability Zones.

Current regions across the world:

- US East
- US West
- Asia Pacific
- Canada
- China
- Europe
- South America


### Availability Zones (AZ)

An AWS Availability Zone is one or more discrete data centers, each with redundant power, networking and connectivity housed in separate facilities. Deploying your application across multiple Availability Zones is useful for redundancy, low latency and fault tolerance.

Regions with multiple Availability Zones:

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

## Edge Locations

A AWS Edge Locations are locations around the world meant for caching content, enhancing the user experience, reducing latency. Edge locations are specifically used by AWS Cloudfront and AWS CDN. Every Region is has its own set Availability Zone's and Edge Locations.

