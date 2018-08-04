# CDN (Content Delivery Network)

## What's a CDN?

A system of distributed servers that deliver webpages and other content to a user based on the geographic locations of that user, the origin of the webpage and a content delivery server

## CloudFront

CloudFront can be used to deliver your entire website, including dynamic content, static, streaming and interactive content using a global network of edge locations.

Requests for your content are automically routed to the nearest Edge Location, so content is delivered with the best possible performance.

CloudFront is optimized to work with other Amazon Web Services like S3, EC2, Elastic Load Balancing and Route 53. CloudFront also works seamlessly with any non-AWS origin server which stores the original,definitive versions of your files.

## Key Terminology

- **Edge Location** - Location where content will be cached. Separate to and AWS region (See [1000-ft-overview/Edge-locations](https://github.com/NigelEarle/AWS-CSA-Notes-2018/tree/master/1000-ft-overview#edge-locations))
- **Origin** - This is the origin of all the files that the CDN will distribute. Can be S3 bucket, EC2 instance, Elastic Load Balancer or Route 53.
- **Distribution** - Given name of CDN which consists of a collection of Edge Locations
- **Web Distribution** - Typically used for websites
- **RTMP (Real Time Message Protocol)** - Used for media streaming

## Links

- [https://aws.amazon.com/cloudfront/](https://aws.amazon.com/cloudfront/)
- [https://aws.amazon.com/cloudfront/details/](https://aws.amazon.com/cloudfront/details/)
