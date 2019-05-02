# Route 53

## DNS

### What is DNS? (Domain Name Service)

If you've used the internet, you've used DNS. DNS is used to convert human friendly domain names `(http://acloud.guru)` into an Internet Protocol (IP) address `(http://92.123.92.1)`

IP addresses are used by computers to identify eachother on the network. IP addresses commonly come in 2 different forms, **IPv4** and **IPv6**

### IPv4 vs IPv6

The IPv4 space is 32 bit field and has over 4 billion different addresses (4,294,967,296)

IPv6 was created to solve this the depletion issue and has an address space of 128 bits - which is in theory **340,282,366,920,938,463,463,374,607,431,768,211,456** different addresses! _340 undecillion addresses_

### Top Level Domains

If common domain names such as google.com, bbc.co.uk etc. you'll notice a string of characters separated but a `.`. The last work in the domain name represents the 'Top Level Domain'. The second word in the domain, known as the 'Second Level Domain' is optional

**_Example Top Level and Second Level Domains:_**

```
.com
.edu
.gov
.org
.co
.co.uk
.gov.au
```

These top level domains are controlled by the Internet Assigned Numbers Authority (IANA) in a root zone database _(database of all available top level domains)_. You can view this database by going to https://www.iana.org/domains/root/db

### Domain Registrars

Because all the names in a given domain have to be unique there needs to be a way to organize all of this so that domains are duplicated - hence **Domain Registrars**.

A registrar is an authority that can assign domain names directly under one or more top level domains. Domains are registered with InterNIC, a service of ICANN, which enforces uniqueness of domain names across the Internet. Each domain name becomes registered in a central database known as the WhoIS database.

### SOA Records

SOA Records store information related to a domain about:

- The name of the server that supplied data for that zone.
- The admin of that zone.
- The current version of the datafile.
- The number of seconds a secondary name server should wait before checking for updates.
- The number of seconds a secondary name server should wait before retrying a failed zone transfer.
- The maximum number of seconds that secondary name server can use data before it must either be refreshed or expire.
- The default number of seconds for the TTL file on resource records.

### NS Records

NS stands for Name Server records and are used by top level domain servers to direct traffic to the Content DNS server which contains the authoritative DNS records.

### A Records

An A Record is the fundamental type of DNS record and the 'A' in A record stands for 'Address'. The A Record is used by the computer to translate the name of the domain to the IP address. For example `https://google.com` -> `https://92.123.12.1`

### TTL

The length that a DNS record is cached on eitherthe Resolving Server o the users own local PC is equal to the value of the 'Time To Live' _(TTL)_ in seconds. The lower the time to live, the faster changes to DNS records take to propagate throughout the internet. 

### CNAMES

A Canonical Name (CName) can be used to resolve one domain name to another. For example, you may have a mobile website with a domain name `http://m.acloud.guru` that is used for when users browse to your domain name on their mobile devices. You may also want the name `http://mobile.acloud.guru` to resolve to this same address.

### Alias Records

Alias resource record sets can save you time because AWS Route 53 automatically recognizes changes in the record sets that the alias resource record set refers to.

For example, suppose an alias resource record set for example.com points to an ELB load balancer at lb1-1234.us-west-1.elb.amazonaws.com. If the IP address of the load balancer change, AWS Route 53 will automatically reflect those changes in DNS answers for example.com whout any changes to the hosted zone that contains resource record sets for example.com

## Routing Policies

### Simple

This is the default routing policy when you create a new record set. This is the most commonly used when you have a single resource that performs a given function for your domain, for example, one web server that serves content for the `http://acloud.guru` website.

### Weighted

Weighted Routing Policies let you split your traffic based on different weights assigned.
For example you can set 10% of your traffic to go to US-EAST-1 and 90% to go to EU-WEST-1

### Latency

Latency based routing allows you to route your traffic based on the lowest network latency for your end user (ie which region will give them the fastest response time)

To use latency-based routing you create a latency resource record set for the EC2 (or ELB) resource in each region that hosts your website. When Route 53 receives a query for your site, it selects the latency resource record set for the region that gives the user the lowest latency. Route 53 then responds with the value associated with that resource record set

### Failover

Failover routing policies are used when you want to create an active/passive set up. For example you may want your primary site to be in EU-WEST-2 and your secondary DR site in AP-SOUTHEAST-2

Route 53 will monitor the health of your primary site using a health check.

A health check monitors the health of your endpoints.

### Geolocation

Geolocation routing lets you choose where your traffic will be sent based on the geographic location of your users (ie the location from which DNS queries originate). 

For example, you might want all queries from Europe to be routed to a fleet of EC2 instances that are specifically configured for your European customers. These servers may have the local language of your European customers and all prices are displayed in Euros.
