#!/bin/bash
yum install httpd -y
yum update -y
aws s3 cp s3://my-default-bucket-blah/healthcheck.html /var/www/html
service httpd start
chkconfig httpd on