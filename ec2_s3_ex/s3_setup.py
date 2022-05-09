import boto3


class S3:
    def __init__(self, bucket_name='eng110-anson'):
        self.bucket_name = bucket_name
        self._region = 'eu-west-1'
        self.s3 = None
        self.s3_client = None   # need refactoring later on
        self.response_history = []

    def make_bucket(self):
        self.s3 = boto3.resource('s3')
        self.s3_client = boto3.client('s3')
        self.s3.create_bucket(
            Bucket=self.bucket_name,
            CreateBucketConfiguration={'LocationConstraint': self._region}
        )

    def upload_data(self, file_name='s3_pic.png', object_name=None):
        if object_name is None:
            object_name = file_name
        up_response = self.s3_client.upload_file(file_name, self.bucket_name, object_name)
        self.response_history.append(up_response)

    def retrieve_data(self, object_name='s3_pic.png', file_name=None):
        if file_name is None:
            file_name = object_name
        down_response = self.s3_client.download_file(self.bucket_name, object_name, file_name)
        self.response_history.append(down_response)

    def delete_data(self, object_name='s3_pic2.png'):
        del_f_response = self.s3_client.delete_object(Bucket=self.bucket_name, Key=object_name)
        self.response_history.append(del_f_response)

    def delete_bucket(self, bucket_name=None):
        if bucket_name is None:
            bucket_name = self.bucket_name
        my_bucket = self.s3.Bucket(bucket_name)
        my_bucket.objects.all().delete()
        del_bk_response = self.s3_client.delete_bucket(Bucket=bucket_name)
        self.response_history.append(del_bk_response)

    def manage_read_access(self, object_name='s3_pic.png'):
        object_acl = self.s3.ObjectAcl(self.bucket_name, object_name)
        response = object_acl.put(ACL='public-read')

    def manage_bucket_policy(self):
        pass


if __name__ == "__main__":
    s3 = S3()
    s3.make_bucket()
    s3.upload_data()
    s3.retrieve_data()
    s3.manage_read_access()


# s3 = boto3.resource('s3')
# s3_client = boto3.client('s3')
# s3.create_bucket(Bucket='eng110-anson', CreateBucketConfiguration={
#     'LocationConstraint': 'eu-west-1'})
#
# # upload to s3
# s3.Object('eng110-anson', 's3_pic.png').put(Body=open('s3_pic.png', 'rb'))
# up_response = s3_client.upload_file('s3_pic.png', 'eng110-anson', 's3_pic2.png')
#
# # retrieve
# down_response = s3_client.download_file('eng110-anson', 's3_pic2.png', 's3_pic2_down.png')
#
# # delete file
# del_f_response = s3_client.delete_object(Bucket='eng110-anson', Key='s3_pic2.png')
#
# # delete bucket
# my_bucket = s3.Bucket('eng110-anson')
# my_bucket.objects.all().delete()
# del_bk_response = s3_client.delete_bucket(Bucket='eng110-anson')
