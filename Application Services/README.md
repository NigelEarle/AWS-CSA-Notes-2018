# Application Services

## SQS - Message Queue

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

- The Visibility Timeout is the amount of time that the message is invisible in the SQS queue after the reader picks up that message. Provided the job is processed before the visibility timout expires, the message will then be deleted from the queue. If the job is not processed within that time, the message will become visible again and another reader/worker will process it. This could result in the same message delivered twice
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

- Amazon SWF presents a task-oriented API, whereas Amazon SQS offers a message-oriented API
- Amazon SWF ensures that a task is assigned **ONLY ONCE** and is **NEVER DUPLICATED**. With SQS, you need to handle duplicated messages and may also need to ensure that a message is processed only once.
- Amazon SWF keeps track of all the tasks and events in an application. With SQS, you need to implement your own application level tracking, especially if your application uses multiple queues.

## SNS

