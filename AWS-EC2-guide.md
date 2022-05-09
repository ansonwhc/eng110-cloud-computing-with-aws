# AWS
Cloud computing service provided by amazon  
- There are over 200 services offered
- A way to move from local data center to cloud that can be accessed globally, instead of locally

![AWS_pic](images/AWS.png)

## EC2
Amazon Elastic Compute Cloud is a secure and resizable cloud compute service

![EC2_pic](images/EC2.png)

## Two tier architecture
- no more monolithic arch  
- We have a database (mongodb-instance) that can be read through an App-instance
    - mongoDB - 1 tier - Database
    - App - 1 tier - Frontend  

![2_tier_arch_pic](images/2_tier_arch.png)

### Useful tricks
#### Make local file available on the cloud
`scp -i <.pem_path> -r <local_dir_path> <user_name>@<EC2_IP>:<dir_destination>`  
(rsaync also can be used)

### Our use - to start an locally developed app instance on the cloud
1. App
    - securely copy our app dir to the EC2 instance
    - if access denied (port 22 unavailable)
    - install nodejs with required dependencies
    - enter new ip in your security group
    - allow port 3000

    - configure nginx reverse proxy
    - ensure you could see the app home page without port 3000

2. Database
    - configure mongodb  
    - spin up a new ec2 instance in eu-west-1  
    - create a security group to allow required ports - 27017  
    - port 22  
    - inside the app instance create ENV_var DB_HOST:mongo://db-ip-add:27017/posts

    - `cd app/app/`
    - `npm start`
    - Should see localhost:3000/posts working 

    mongodb
    - install 
    - sudo systemctl start mongod
    - sudo systemctl enable mongod
    - sudo systemctl restart mongod (if needed)

## Two tier architecture dissected    

### Step 1
<img src="https://user-images.githubusercontent.com/94448528/167323361-334a6880-6a23-473b-9d74-f5f114221a18.png" height="300">

https://user-images.githubusercontent.com/94448528/167322237-0d731cdb-2dba-4f98-9ba3-96c54c9df7c7.mp4

### Step 2
<img src="https://user-images.githubusercontent.com/94448528/167323336-b29faf92-bce8-4782-aa61-899defd59a4d.png" height="300">
<img src="https://user-images.githubusercontent.com/94448528/167323405-3cfc97b2-1c39-4fe1-8973-516833e9e400.png" height="300">

https://user-images.githubusercontent.com/94448528/167325613-002eca3e-97b5-417b-ba2c-0dc50bd670a5.mp4

https://user-images.githubusercontent.com/94448528/167325618-a0e44c01-3bd1-4a6f-a3f3-186152b18f6e.mp4

### Step 3
<img src="https://user-images.githubusercontent.com/94448528/167323436-80e7f196-1139-4257-ae76-2f3e3e8dcafc.png" height="300">

https://user-images.githubusercontent.com/94448528/167325641-3f120173-044d-4418-a159-7b6a08230f16.mp4

### Step 4
<img src="https://user-images.githubusercontent.com/94448528/167323451-41e942b0-88f3-4b2e-bc7b-8104948def59.png" height="300">

https://user-images.githubusercontent.com/94448528/167325776-7d62a7cd-f026-4e56-ba5a-05929d2b0ef7.mp4

### Step 5
<img src="https://user-images.githubusercontent.com/94448528/167323463-b8d997d2-579f-4673-a2cb-4ec4ba1b4560.png" height="300">

https://user-images.githubusercontent.com/94448528/167325882-8a51ec5a-2e3a-4506-86ff-19af454dfbda.mp4

### Step 6
<img src="https://user-images.githubusercontent.com/94448528/167323482-1ce3a0a4-b8e0-4575-9115-2c2d1551a0a1.png" height="300">
<img src="https://user-images.githubusercontent.com/94448528/167323697-3a6d55c7-7126-4719-a135-4c9a4cc61506.png" width="500">
<img src="https://user-images.githubusercontent.com/94448528/167323708-5a674bc4-8acd-4040-bd67-b067896078d7.png" width="500">

https://user-images.githubusercontent.com/94448528/167326001-fb38fc86-2e89-403f-9c50-4e655501dbf2.mp4

### Step 7
<img src="https://user-images.githubusercontent.com/94448528/167323726-87e9eedf-7be2-4bdb-b7ce-c2b853577862.png" height="300">
<img src="https://user-images.githubusercontent.com/94448528/167323774-bca309bc-e474-42d3-be4b-4130b150128b.png" height="300">

https://user-images.githubusercontent.com/94448528/167326367-97512360-7a9d-41d5-91c4-03c2b868e917.mp4

https://user-images.githubusercontent.com/94448528/167326374-39ac9da5-c7d4-48af-ab0a-b6e64ab18df1.mp4

### Step 8
<img src="https://user-images.githubusercontent.com/94448528/167323808-ed39c351-8f17-4df2-ad72-243a367eee54.png" height="300">

https://user-images.githubusercontent.com/94448528/167326524-be3934ce-05aa-4b69-b1b4-c72923d57230.mp4

### Step 9
<img src="https://user-images.githubusercontent.com/94448528/167323822-8a484dac-9f9d-4dff-8c30-3ad9cd1de89d.png" height="300">

https://user-images.githubusercontent.com/94448528/167326729-acaa4acd-fa2c-485d-8214-7cdc987aa641.mp4

### Step 10
<img src="https://user-images.githubusercontent.com/94448528/167323835-d3a6baff-b8c8-4cdc-ada3-840fa95d052c.png" height="300">
<img src="https://user-images.githubusercontent.com/94448528/167323851-30d98ec0-3890-40ca-b1b5-a4a0a0032146.png" height="300">

https://user-images.githubusercontent.com/94448528/167326750-7e39ab58-7501-478f-a542-ed2bac15ba68.mp4

https://user-images.githubusercontent.com/94448528/167326822-20cc81c4-264d-42be-8a6d-6bba5aba177d.mp4

https://user-images.githubusercontent.com/94448528/167326859-c235b777-49c5-4403-bbf6-333f55d59d44.mp4

### Step 11
<img src="https://user-images.githubusercontent.com/94448528/167323865-07e836f8-2e22-405f-a2aa-cdef63a7f050.png" height="250">

https://user-images.githubusercontent.com/94448528/167326943-3ea1ec2d-4f21-4b68-a8b3-f8c3bb46f87f.mp4






