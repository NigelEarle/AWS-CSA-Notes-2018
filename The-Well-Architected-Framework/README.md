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
