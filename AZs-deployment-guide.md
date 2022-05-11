# Highly available and scalability multi Availability Zones deployment

![](images/AZ%20autoscaling%20group.png) 
1. Auto Scaling Group Setup Option 1 Example [Here](#asg-set-up-option-1) 
   - Launch Template Guide [Here](#launch-template-guide)
   - Auto Scaling Group Setup Guide [Here](#auto-scaling-group-setup-guide)
2. App deployment exercise using Auto Scaling Group - <i>to be added</i>
3. Glossary [Here](#glossary)

## ASG Setup Option 1
### Launch Template Guide
<img src="https://user-images.githubusercontent.com/94448528/167620030-7b653ba0-d0ae-4915-9c0d-ed76069e7e5b.png" width="600">
<img src="https://user-images.githubusercontent.com/94448528/167620041-04bb0fec-0422-4af1-a078-211ee0396160.png" width="600">
<img src="https://user-images.githubusercontent.com/94448528/167620046-d09d2211-3d2b-4764-91ee-5c1047edebbd.png" width="600">
<img src="https://user-images.githubusercontent.com/94448528/167620050-56b584f4-dfba-423c-9ec5-b5951ba72082.png" width="600">
<img src="https://user-images.githubusercontent.com/94448528/167620054-bbf9119b-2d70-4bfc-88d4-28802eb71956.png" width="600">
<img src="https://user-images.githubusercontent.com/94448528/167620060-9ac174dd-c407-4b21-a57a-362c6fe54490.png" width="600">

<i>(User data can be used for provisioning)</i>

<img src="https://user-images.githubusercontent.com/94448528/167620067-eb9d3d0f-533f-46f1-bba3-0d71d232dfe0.png" width="500">
<img src="https://user-images.githubusercontent.com/94448528/167620071-4234c7ed-a376-4348-a884-33690636c95c.png" width="600">
<br><br>

### Auto Scaling Group Setup Guide
<img src="https://user-images.githubusercontent.com/94448528/167806001-c5ea86b1-f858-485d-a7a8-cd42697b3097.png" width="500">

We use the launch template created with the guide [Here](#launch-template-guide)  
<img src="https://user-images.githubusercontent.com/94448528/167806013-9ba9b89e-c46d-403c-b8de-5292c87f380a.png" width="500">

<img src="https://user-images.githubusercontent.com/94448528/167806019-54d43425-7ca2-4459-8cd4-7fc32b4ef481.png" width="500">

<img src="https://user-images.githubusercontent.com/94448528/167806033-6b4d60b5-3a4c-4808-b5b2-a95de07c9214.png" width="500">

<img src="https://user-images.githubusercontent.com/94448528/167806046-679ae7ca-fb33-4594-ba3a-56ef3bf83e6d.png" width="500">

We require the default listening port 80 for our service  
<img src="https://user-images.githubusercontent.com/94448528/167806054-f371184b-fe05-4ca6-b907-c367d977c76a.png" width="500">

<img src="https://user-images.githubusercontent.com/94448528/167806066-4e6e74e1-9266-4191-9195-c55951543895.png" width="500">

<img src="https://user-images.githubusercontent.com/94448528/167806074-2fc38e41-6e13-4874-a5c4-5d964c607a90.png" width="500">

<img src="https://user-images.githubusercontent.com/94448528/167806093-0b6289f2-9b32-4af9-a382-d58004c344b2.png" width="500">

Successful ASG setup  
<img src="https://user-images.githubusercontent.com/94448528/167806097-577ccf35-2aaf-46e4-812b-75c7e233b095.png" width="500">

Pre-set number of instances should berunning, 24/7, until further instructions  
<img src="https://user-images.githubusercontent.com/94448528/167806107-40477f21-3ff4-4860-8910-e2f955e1fad9.png" width="500">


## Glossary
### Availability Zones
Availbility zones, AZs are isolated locations within data centre regions that public cloud services originate and operate from.
<br><br>

### High Availability
Using multi AZs, we can ensure service availability across different instances, so no longer have a single point of failure.
<br><br>

### High Scalability
The ability and functionality to easily adjust the number of instances that are available, up and running for the services.
<br><br>

### Load Balancing
Distribution of incoming traffic across multiple targets, such as EC2 instances, in one or more Availability Zones, so that no instance get overwhelmed. For AWS, Elastic Load Balancing is a service that does this automatically.
<br><br>

### Listener Groups
A listener is a process that checks for connection requests, using the protocol and port that we configure. The rules that we define for a listener determine how the load balancer routes request to the registered targets. Listener groups are groups of listeners checking for different requests.
<br><br>

### Auto Scaling Group
Auto Scaling is the function of automatically adjusting the amount of computational resources based on the server load. An Auto Scaling group (ASG) contains a collection of cloud computing units/instances, for example Amazon EC2 instances, that are treated as a logical grouping for the purposes of automatic scaling and management. For AWS, Auto Scaling group also enables you to use Amazon EC2 Auto Scaling features such as health check replacements and scaling policies.
<br><br>

### ASG Launch Configuration 
When we create an Auto Scaling group, we must specify the launch configuration, the necessary information to configure the cloud computing units/instances, such as Amazon EC2 instances, the Availability Zones and VPC subnets for the instances, the desired capacity, and the minimum and maximum capacity limits, etc. These configurations are usually dependent on the services being deployed.
<br><br>

### ASG Launch Template
Launch templates are used as a pre-set launch configuration. they contain fixed parameters (AMI, instance type, security groups, and key pairs etc.) so that we do not need to define these parameters every time we launch new instances.

For AWS, we can specify a launch template or a launch configuration to configure Amazon EC2 instances that are launched by our Auto Scaling group.
<br><br>

### Autoscaling Policy 
We specify one or more step adjustments in our Auto Scaling Group, such that it automatically scales the number of instances dynamically based on the scaling metrics and threshold values for the alarms that invoke the scaling process. 

