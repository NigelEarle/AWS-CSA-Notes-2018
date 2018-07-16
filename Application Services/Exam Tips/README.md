# Exam Tips

## SQS

- SQS is a distributed message queueing system
- Allows you to decouple the components of an application so that they are independent
- Pull-based, not push- based
- Standard queues (default) - best effort ordering; message delivered at least once
- FIFO Queues (First In First Out) - ordering strictly preserved, message delivered once, no duplicates. eg. good for banking transactions which need to happen in strict order.
