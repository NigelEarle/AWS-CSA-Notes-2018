# Additional Exam Tips

Based on student feedback from those who have already done the course

### Kinesis

- Used to consume Big Data
- Stream large amounts of social media, news feeds, logs etc to the cloud
- Think Kinesis when approached with big data questions

- Process large amounts of data;
  - Redshift for business intelligence
  - Elastic Map Reduce for Big Data Processing


### EC2 - EBS Backed Volumes vs Instance Store Volumes

- EBS backed volumes are persistent
- Instance Store backed volumes are not persistent (ephemeral)
- EBS Volumes can be detached and reattached to other EC2 instances

- Instance store volumes cannot be detached and reattached to other instances - they exist only for the life of that instance.
- EBS volumes can be stopped; data will persist

- Instance store volumes cannot be stopped - if you do this the data will be wiped

- EBS Backed = Store Data Long Term
- Instance Store = Shouldn't be used for long-term data storage

### OpsWork

- Orchestration Service that uses Chef
- Chef consists of recipes to maintain a consistent state
- Look for the term "chef" or "recipes" or "cook books" and think OpsWorks

### Elastic Transcoder

- Media Transcoder in the cloud
- Convert media files from their original source format in to different formats that will play on smartphones, tablets, PC's, etc
- Provides transcoding presets for popular output formats, which means that you dont need to guess about which settings work best on particular devices
- Pay based on the minutes that you transcode and the resolution at which you transcode

### SWF Actors

- **Workflow Starter** - An application that can initiate (start) a workflow. Could be your e-commerce website when placing an order or a mobile app searching for bus times.
- **Deciders** - Control the flow of activity tasks in a workflow execution. If something has finished in a workflow (or fails) a Decider decides what to do next.
- **Activity Workers** - Carry out the activity tasks

### EC2 - Get Public IP Address

- Query the instances metadata:
  - `curl http://169.254.169.254/latest/meta-data`
  - `wget http://169.254.169.254/latest/meta-data`
  - Key thing to remember is that its an instances META-DATA, not user data
  