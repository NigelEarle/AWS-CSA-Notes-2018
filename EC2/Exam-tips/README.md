# Exam Tips

### EC2 Instance Run Down

- **On Demand** - allows you to pay a fixed rate by the hour (or second) with not commitement

- **Reserved** - provides you with the capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 year terms

- **Spot** - Enables you to bid whatever price you want for instane capacity, providing for even greater savings if your applications have flexible start and end times

- **Dedicated Hosts** - Physical EC2 server dedicated for your use. Dedicated Hosts can help reduce costs by allowing you to use your existing server-bound software license

**_Important Note!!_**

If a Spot instance is terminated by Amazon EC2, you will not be charged for a partial hour of usage. However, if you terminatethe instance yourself, you will be charged for the complete hour in which the instance ran.

### Instance Types

**F.I.G.H.TD.R.M.C.P.X.**

### Volume Types

#### SSD

- **General Purpose (SSD)** - balances price and perf. for a wide variety of workloads

- **Provisioned IOPS (SSD)** - Highest perf. SSD volume for mission-critical low-latency or high-throughput workloads

#### Magnetic

- **Throughput Optimized HDD** - Low cost HDD volume designed for frequently accessed, throughput-intensive workloads

- **Cold HDD** - Lowest cost HDD volume designed for less frequently accessed workloads

- **Magnetic** - Previous Generation. Can be a boot volume.