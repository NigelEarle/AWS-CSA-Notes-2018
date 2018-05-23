# IAM - Identity Access Management

## What is it?

Allow you to manage users and their level of access management to the AWS console. Tested for exam and co. aws account in real life. IAM is globally available and not specified to region

## What does it give you?
Centralized control of your AWS account
Shared Access to your AWS account
Granular permissions
Identity federation
    access to 3rd party service, Active Directory, Facebook, Linkedin
Multifactor Authentication
Provide temporary access for users/devices and services where necessary
Set up and manage password rotation
Integrates with many different AWS services
supports PCI, DSS compliance

## Terminology

- **Users** - End users (people)
- **Groups** - Collection of users under one set of permissions
- **Roles** - Will Update, create roles and assign them to services grant roles to entities that you trust
- **Policies** - Document that defines one or more permissions - JSON format
- **Root account** - user used to sign into AWS account

## General Notes

- Attach permissions to users as well as groups
- No users have permissions when first created
- New users are assigned and Access Key ID and Secret Key when first created
    - Keys are not the same as passwords
    - Must regenerate keys if lost
- ALWAYS setup multifactor auth on root account
- Customize password rotation policies
- Unable to set billing alarm in cloud watch because of new account