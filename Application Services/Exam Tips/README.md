# Exam Tips

## SQS

- SQS is a distributed message queueing system
- Allows you to decouple the components of an application so that they are independent
- Pull-based, not push- based
- Standard queues (default) - best effort ordering; message delivered at least once
- FIFO Queues (First In First Out) - ordering strictly preserved, message delivered once, no duplicates. eg. good for banking transactions which need to happen in strict order.

## API Gateway

- Remember what API Gateway is at a high level
- API Gateway has caching capabilities to increase performance
- API Gateway is low cost and scales automatically
- You can throttle API Gateway to prevent attacks 
- You can log results to CloudWatch
- If you are using JS/AJAX that uses multiple domains with API Gateway, ensure that you have CORS enabled on API Gateway