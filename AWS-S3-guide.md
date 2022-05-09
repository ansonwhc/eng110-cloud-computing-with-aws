# Simple storage service  

Amazon Simple Storage Service (Amazon S3) is an object storage service that offers industry-leading scalability, data availability, security, and performance. Customers of all sizes and industries can use Amazon S3 to store and protect any amount of data for a range of use cases, such as data lakes, websites, mobile applications, backup and restore, archive, enterprise applications, IoT devices, and big data analytics. Amazon S3 provides management features so that you can optimize, organize, and configure access to your data to meet your specific business, organizational, and compliance requirements.  

## Our first use case  

![](images/s3.png)

### S3 setup
command | function
--- | ---
ec2_setup.sh | -
`sudo apt install python` | install python
`sudo apt install python3-pip -y` | install python pip
`alias python=python3` | instruct the system to use python 3
`python --version` | ensure we have python > 3.x
`python` | start python env
`exit()` | exit python env
` `| to make it permanent - make it an env var
`sudo python3 -m pip install awscli` | install awscli
. | .
`aws configure` | input configs - securing our keys as now they are stored in the aws cloud
`aws s3` | to use s3
`aws s3 ls` | tell s3 to list the contents (to know we have secured and inputted our keys correctly)
`aws s3 mb s3://eng110-anson` | make a s3 bucket - name can only contain [^a-zA-Z0-9_]
`aws s3 cp <file_path> s3://<bucket_name>/` | copying file from ec2 to s3
`aws s3 cp s3://<bucket_name>/<file_name> .` | copying file from s3 to ec2

### AWS Command Line Interface (CLI) with s3
command | function | example
--- | --- | ---
`aws s3 mb <s3_bucket>` | make a s3 bucket | `aws s3 mb s3://<bucket_name>`
`aws s3 ls <s3_bucket>` | list contents within the bucket | `aws s3 ls s3://<bucket_name>`
`aws s3 cp <source> <destination>` | copy data from s3 to ec2 | `aws s3 cp s3://<bucket_name>/<file_name> .`
`aws s3 mv <source> <destination>` | move data from s3 to ec2 | `aws s3 mv s3://<bucket_name>/<file_name> .`
`aws s3 sync <source> <destination>` | sync ec2 directory with a s3 bucket | `aws s3 sync . s3://<bucket_name>/<path>`
`aws s3 rb <s3_bucket>` | remove s3 bucket | `aws s3 rb s3://<bucket_name>`
`aws s3 rm <file_path>` | remove a from from s3 bucket | `aws s3 rm s3://<bucket_name>/<file_name>`

#### Useful options
command | function
--- | --- 
`--force` | force an action
`-r` | recursive action, useful for handling directories

### S3 policies (Web interface)
- Object URL - for access
- Object policies -> bucket -> object -> permission
- Bucket policies -> bucket -> permission
- We can customise the policies

### Exercise
- Create a script for s3 CRUD
  - script stored in ec2_s3_ex
  - scp file to ec2 instance
  - `bash <path>/ex2_setup.sh`
  - (potentially) `alias python=python3`
  - `aws configure`
  - `python <path>/s3_setup.py`
  - S3 class within s3_setup.py have methods for CRUD
