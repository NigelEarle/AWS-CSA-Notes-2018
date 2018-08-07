# IAM - Identity Access Management

## What is IAM?

Allow you to manage users and their level of access management to the AWS console. Tested for exam and co. aws account in real life. IAM is globally available and not specified to region

## What can you do with IAM?

- Centralized control of your AWS account
- Shared Access to your AWS account
- Granular permissions
- Identity Federation
    - Access to 3rd party service, Active Directory, Facebook, Linkedin
- Multifactor Authentication (MFA)
- Provide temporary access for users/devices and services where necessary
- Set up and manage password rotation
- Integrates with many different AWS services
- Supports PCI, DSS compliance

## Terminology

- **Users** - End users (people)
- **Groups** - Collection of users under one set of permissions
- **Roles** - Permissions defined for AWS resources (i.e. EC2 etc.)
- **Policy Documents** - Document that defines one or more permissions - JSON format
- **Root account** - user used to sign into AWS account

## General Notes

- Universal. Does not apply to regions at this time.
- Attach permissions to users as well as groups
- New users have NO permissions when first created
- New users are assigned and Access Key ID and Secret Key when first created
    - Keys are not the same as passwords
    - Must regenerate keys if lost
- ALWAYS setup multifactor auth on root account
- Customize password rotation policies
- Unable to set billing alarm in cloud watch because of new account

## Links

- [https://aws.amazon.com/iam/faqs/](https://aws.amazon.com/iam/faqs/)
- [https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)
