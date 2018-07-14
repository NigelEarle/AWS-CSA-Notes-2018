# Exam Tips

## ElastiCache

You will be given a scenario where a particular database is under a lot of stress/load. You may be asked which service you should use to alleviate this.

ElastiCache is a good choice if your database is particularly read heavy and not prone to frequent changing.

Redshift is a good answer if the reason your database is feeling stress is because management keep running OLAP transactions on it etc.

## Summary

### Types

- RDS - OLTP
  - SQL
  - MySQL
  - PostgreSQL
  - Oracle
  - Aurora
  - MariaDB
- DynamoDB - NoSQL
- Redshift - OLAP
- Elasticache - In Memory Caching
  - Memacached
  - Redis

---

#### READ FAQ RDS SECTION IN DOCUMENTATION!!

[https://aws.amazon.com/rds/faqs/](https://aws.amazon.com/rds/faqs/)