IAM - Identity Access Management
    Allow you to manage users and their level of access management to the AWS console. Tested for exam and co. aws account in real life.

What does it give you?
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

Terminology
    Users - End users (people)
    Groups - collection of users under one set of permissions
    Roles - Will Update, create roles and assign them to services grant roles to entities that you trust
    Policies -document that defines one or more permissions - JSON
    
IAM is globally available. Not specified to region
root account - user I use to sign into aws account
Attach permissions to users as well as groups
No users have permissions when first created
New users are assigned access key id and secret key when first created
    Keys are not the same as passwords
    must regenerate if lost
ALWAYS setup multifactor auth on root account
Customize password rotation policies
    

Unable to set billing alarm in cloud watch because of new account**