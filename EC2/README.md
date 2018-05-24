# EC2 (Elastic Cloud Compute)

AWS EC2 is a web service that provides resizable compute capacity in the cloud. EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.

EC2 has changed the economics of cloud computing by allowing you to pay only for capacity that your actually use. EC2 provides developers the tools to build failure resistent applications and isolate themselves from common failure scenarios.

## Pricing Options

### On Demand

Allows you to pay a fixed rate by the hour (or by the second) with no commitment.

**_Use Cases_**

- Perfect for users that want the low cost and flexibility of EC2 without any of the up front payment or long term commitment
- Applications with short term, spiky or unpredictable workloads that cannot be interrupted
- Applications being developed or tested on EC2 for the first time

### Reserved

Provides you with a capacity reservation, and offer a significant discount on the hourly charge for an instance. 1 year or 3 year terms.

**_Use Cases_**

- Applications with steady state or predictable usage
- Applications that require reserved capacity
- Users can make up front payments to reduce their totoal computing costs even further
  - Standard RIs (Up to 75% off on-demand)
  - Convertible RIs (Up to 54% off on-demand) feature the capability to change the attributes of the RI as long as the exchange results in the creation of Reserved Instances of equal or greater value. Ability to go from CPU intensive instance to Memory intensive.
  - Scheduled RIs are available to launch within the time window you reserve. This option allows you to match your capacity reservation to predictable recurring schedule that only requires a fraction of a day, a week, or a month.

### Spot

Enables you to bid whatever price you want for an instance capacity, providing for even greater savings if your applications have flexible start and end times.

**Use Cases**

- Applications that have flexible start and end times
- Applications that are only feasible at very low compute prices
- Used for single compute instances to save on costs compared to 9-5 during the week.
- Users with an urgent need for a large amount of additional computing capacity.

### Dedicated Hosts

Physical EC2 server dedicated for your use. Dedicated Hosts can help you reduce costs by allowing yout to use your existing server-bound software licenses.

**Use Cases**

- Useful for regulatory requirements that may not support multi-tenant vitualization.
- Great for licensing which does not support multi-tenancy or cloud deployments
- Can be purchased On-Demand (hourly).
- Can be purchased as a Reservation for up to 70% off the On-Demand price.