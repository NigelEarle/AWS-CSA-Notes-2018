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

