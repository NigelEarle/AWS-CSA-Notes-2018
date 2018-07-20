# The Well Architected Framework

This section aggregates the well architected framework white paper

https://aws.amazon.com/architecture/well-architected/
https://d0.awsstatic.com/whitepapers/AWS_Cloud_Best_Practices.pdf

## Best Practices

### Business Benefits of the Cloud

- Almost zero upfront infrastructure investment
- Just-in-time infrastructure
- More efficient resource utilization
- Usage-based costing
- Reduced time to market

### Technical Benefits of the Cloud

- Automation - "Scriptable Infrastructure"
- Auto-Scaling
- Proactive Scaling
- More Efficient Development lifecycle
- Improved Testability
- Disaster Recovery and Business Continuity
- "Overflow" the traffic to the cloud

### Design For Failure

**Rule of thumb:**

Be a pessimist when designing architectures in the cloud - assume things will fail. In other words, always design, implement and deploy for automated recovery from failure.

**Assume that...**

- your hardware _will_ fail
- disaster _will_ strike your application
- you _will_ slammed with more than the expected number of requests per second some day.
- with time your application software _will_ fail too.

Being a pessimist, you end up thinking about recovery strategies during design time, which helps in designing overall system better.

### Decouple Your Components

The key is to build components that do not have tight dependencies on each other, so that if once component were to die(fail), sleep(not respond) or remain busy(slow to respond) for some reason, the other components in the system are built so as to continue to work as if no failure is happening.

In essence, loose coupling isolates the various layers and components of you application so that each component interacts async with the others and treats them as a "black box".

**For Example...**

In the case of web application architecture, you can isolate the app server from the web server and from the db. The app server does not know about your web server and vice versa, this gives decoupling between these layers and there are not dependencies code wise or functional perspectives.

In the case of batch processing architecture, you can create async components that are independent of each other.

### Implement Elasticity

The cloud brings a new concept of elasticity in your applications. Elasticity can be implemented in 3 ways..

1. **Proactive Cyclic Scaling:** Periodic scaling that occurs at a fixed interval (daily, weekly, monthly, quarterly)
2. **Proactive Event-base Scaling:** Scaling just when you are expecting a big surge of traffic requests due to a scheduled business event (new product launch, marketing campaigns)
3. **Auto-scaling based on demain:** By using monitoring service, you system can send triggers to take appropriate actions so that if scales up or down based on metrics (utilization of servers or network I/O)

## The Well Architected Framework

### What is the well architected framework?

This has been developed by the Solutions Architecture team based on their experience with helping AWS customers. The well architected framework is a set of questions that you can use to evaluate how well your architecture is aligned to AWS best practices.

### 5 Pillars of the Well Architected Framework

- Security
- Reliability
- Performance Efficiency
- Cost Optimization
- Operation Excellence

### Structure of each pillar

- Design Principles
- Definition
- Best Practices
- Key AWS Services
- Resources

### General Design Principles

- Stop guessing your capacity needs
- Test systems at production scale
- Automate to make architectural experimentation easier
- Allow for evolutionary architectures
- Data-driven architectures
- Improve through game days