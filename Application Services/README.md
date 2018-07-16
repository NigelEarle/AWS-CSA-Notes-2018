# Application Services

## SQS - Simple Queue Service

First **EVER** AWS Service!

Amazon SQS is a web service that gives you access to a message queue that can be used to store messages while waiting for a computer to process them.

Amazon SQS is a distributed queue sustem that enables web service applications to quickly and reliably queue messages that one component in the application generates to be consumed by another component. A queue is a temporary repository for messages that are awaiting processing.

### SQS Breakdown

Using Amazon SQS, you can decouple the components of an application so they run independentlym easing message management between components

Any component of a distributed application can store messages in the queue. Messages can contain up to 256Kb of text in any format. Any component can later retrieve the messages programatically using the SQS API

### What do you mean by "Queue"?

The queue acts as a buffer between the component producing and saving data, and the component receiving the data for processing. This means the queue resolves issues that arise if the producer is producing faster than the consumer can process it, of if the producer or consumer are only intermittenly connected to the network.

### Queue Types

### Standard Queue (default)

Amazon SQS offers standard as the default queue type. A standard queue lets you have a nearly-unlimited number of transactions per second. Standard queues guarantee that a message is delivered at least once. However, because of the highly distributed architecture that allows high throughput, more than one copy of a message might be delivered out of order. Standard queues provide best effort ordering which ensures that messages are generally delivered in the same order as they are sent.

### FIFO Queues (First In, First Out)

The FIFO queue complements the standard queue. The most important features of this queue type are FIFO delivery and exactly one processing: The order in which messages are sent and received is strictly preserved and a message is delivered once and remains available until a consumer processes and deletes it; duplicates are not introduced into the queue. FIFO queues also support message groups that allow multiple ordered message groups within a single queue. FIFO queues are limited to 300 transactions per second, but have all the capabilities of standard queues

```|_5_| ---> |_4_| ---> |_3_| ---> |_2_| ---> |_1_|```

### Key Facts

- SQS is pull-based, not pushed based
- Messages are 256Kb in size
- Messages can be kept in the queue from 1 minute to 14 days
- Default retention period is 4 days
- SQS guarantees that your messages will be processed at least once.

### Visibility Timeout

- The Visibility Timeout is the amount of time that the message is invisible in the SQS queue after the reader picks up that message. Provided the job is processed before the visibility timeout expires, the message will then be deleted from the queue. If the job is not processed within that time, the message will become visible again and another reader/worker will process it. This could result in the same message delivered twice
- Default visibility timeout is 30 seconds
- Increase it if your task takes >30 seconds
- Maximum is 12 hours

### Long Polling

- Amazon SQS long polling is a way to retrieve messages from your Amazon SQS queues
- While the regular short polling returns immediately (even if the message queue being polled is empty), long polling doesn't return a repsonse until a message arrives in the message queue, or the long poll times out.
- Waits til message is in the queue.
- As such, long polling saves you money.

## SWF - Simple Workflow Service

Amazon Simple Workflow Service is a web service that makes it easy to coordinate work across distributed application components. Amazon SWF enables applications for a range of use cases, including media processing, web application back-ends, business process workflows, and analytics pipelines, to be designed as a coordination of tasks.

Tasks represent invocations of various processing steps in an application which can be performed by executable code, web service calls, human actions, scripts.

### Starters

An application that can initiate a workflow. Could be your e-commerce website when placing an order or a mobile app searching for bus times

### Workers

Workers are programs that interact with Amazon SWF to get tasks, process received tasks and return results.

### Deciders

The decider is a program that controls the coordination of tasks, ie their ordering, concurrency and scheduling according to the application logic.


### Workers and Deciders Interaction

The workers and the decider can run on cloud infrastructure, such as Amazon EC2, or on machines behind firewalls, Amazon SWF brokers the interactions between workers and the decider. It allows the decider to get consistent views into the progress of tasks and to initiate new tasks in an ongoing manner.

At the same time, Amazon SWF stores tasks, assigns them to workers when they are ready and monitors their progress. It ensures that a task is assigned **ONLY ONCE** and is **NEVER DUPLICATED** (key difference from SQS).

Since Amazon SWF maintains the applications state durably, workers and deciders dont have to keep track of execution state. They can run independently, and scale quickly.

### SWF Domains

Your workflow and activity types and the workflow execution itself are all scoped to a domain. Domains isolate a set of types, executions, and task lists from others within the same account.

You can register a domain by using the AWS Management Console or by using the Register Domain action inthe Amazon SWF API.

Maximum workflow can be 1 year and the value is always measured in seconds

_JSON Domain Registration Example_

```JSON
{
  "name": "92034",
  "description": "music",
  "workflowExecutionRetentionPeriodInDays": "60"
}
```

### SWF vs. SQF

- Amazon SWF has a retention period of 1 year vs SQS's 14 days retention
- Amazon SWF presents a task-oriented API, whereas Amazon SQS offers a message-oriented API
- Amazon SWF ensures that a task is assigned **ONLY ONCE** and is **NEVER DUPLICATED**. With SQS, you need to handle duplicated messages and may also need to ensure that a message is processed only once.
- Amazon SWF keeps track of all the tasks and events in an application. With SQS, you need to implement your own application level tracking, especially if your application uses multiple queues.

## SNS - Simple Notification Service

SNS is a web service that makes it easy to set up, operate and send notifications from the cloud. It provides developers with a highly scalable, flexible and cost-effective capability to publish messages from an application and immediately deliver them to subscribers or ther applications

May push notifications to Apple, Google, Fire OS and Windows devices as well as Android devices in China with Baidu Cloud Push.

Besides pushing cloud notifications directly to mobile devices, SNS can also deliver notifications by SMS text message or emai, to SQS queues, or to any HTTP endpoint.

SNS notifications can also trigger Lambda functions. When a messge is published to and SNS topic that has a Lambda function subscribed to it, the Lambda function is invoked with the payload of the published message. The Lambda function receives the message payload as an input parameter and can manipulate the information in the message, publish the message to other SNS topics, or send the message to other AWS services.

### SNS Structure

SNS allows you to group multiple recipients using topics. A topic is an "access point" for allowing recipients to dynamically subscribe for identical copies of the same notification. 

One topic can support deliveries to multiple endpoint types - for example, you can group together iOS, Android and SMS recipients. When you publish once to a topic, SNS delivers appropriately formatted copies of your message to each subscriber.

To prevent messages from being lost, all messages published to SNS are stored redundantly across multiple availability zones.

### Subscribers - Who may subscribe to notifications?

- HTTP
- HTTPS
- Email
- Email-JSON
- SQS
- Application
- Lambda


### SNS Benefits

- Instantaneous, push-based delivery (no polling)
- Simple APIs and easy integration with applications
- Flexible message delivery over multiple transport protocols
- Inexpensive, pay-as-you-go model with no up-front costs
- Web-based AWS Management Console offers the simplicity of a point-and-click interface

### SNS vs SQS

- Both messaging services in AWS
- SNS = push; SQS = polls (pulls)

### Pricing

- User pays $0.50 per 1 million SNS Requests
- $0.06 per 100,000 notification deliveries over HTTP
- $0.75 per 100 notifications deliveries over SMS
- $2.00 per 100,000 notification deliveries over email

## Elastic Transcoder

- Media Transcoder in the cloud.
- Convert media files from their original source format in to different formats that will play on smarphones, tablets, PCs etc.
- Provides transcoding presets for popular output formats, which means that you dont need to guess about which settings work bets on particular devices.
- Pay based on the minutes that you transcode and the resolution at which you transcode.

## API Gateway

API Gatewayis a fully managed service that makes it easy for developers to publish, maintain, monitor and secure APIs at any scale. With a few clicks in the AWS Management Console, you can create and API that acts as a "front door" for applications to access data, business logic, or functionality from you back-end services, such as applications running on EC2, code running on Lambda or any web application.

### Caching

You can enable API caching in API Gateway to cache your endpoints response. With caching, you can reduce the number of calls made to your endpoint and also improve the latency of the requests to your API.

When you enable caching for a stage, API Gateway caches responses from your endpoint for a specified TTL period, in seconds. API Gateway then responds to the request by looking up the endpoint response from the cache instead of making a request to your endpoint.

- Low cost & efficient
- Scales effortlessly
- You can throttle requests to prevent attacks
- Connect to Cloudwatch to log all requests

## Kinesis

### What is streaming data?

Streaming data is data that is generated continuously by thousands of data sources, which typically send in the data records simultaneously, and in small sizes (order of KB)

**Examples of usage:**

- Purchases from online stores
- Stock prices
- Game data
- Social network data
- Geospatial data - uber, google maps
- iOT data

### What is Kinesis?

AWS Kinesis is a platform on AWS to send your streaming data to. Kinesis makes it easy to load and analyze streaming data, and also providing the ability for you to build your own custom applications for your business needs.

### Core Kinesis Services?

#### Kinesis Streams

- Streams consist of shards
  - 5 transactions per second for reads, up to a maximum total data read rate of 2Mb per second and up to 1,000 records per second for writes, up to a maximum total data write rate of 1 Mb per second (including partition keys).
  - The data capacity of your stream is a function of the number of shards that you specify for the stream. The total capacity of the stream is the sum of the capacities of its shards.

#### Kinesis Firehose

- Handles stream data automatically, no need to specify shards.

#### Kinesis Analytics

- Allows you to run SQL queries, analyzing the data and store said data in to another storage service like S3


