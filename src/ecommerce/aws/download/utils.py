import boto3
import re
import os

from django.conf import settings
from boto3.s3.transfer import S3Transfer

class AWSDownload(object):
    access_key = None
    secret_key = None
    bucket = None
    region = None
    expires = getattr(settings, 'AWS_DOWNLOAD_EXPIRE', 5000)

    def __init__(self,  access_key, secret_key, bucket, region, *args, **kwargs):
        self.bucket = bucket
        self.access_key = access_key
        self.secret_key = secret_key
        self.region = region
        super(AWSDownload, self).__init__(*args, **kwargs)

    def s3connect(self):
        session = boto3.Session(
            aws_access_key_id=self.access_key, 
            aws_secret_access_key=self.secret_key,
            region_name=self.region
        )
        s3 = session.resource('s3')
        return s3

    def get_bucket(self):
        s3 = self.s3connect()
        bucket = s3.Bucket(self.bucket)
        return bucket

    def get_key(self, path):
        bucket = self.get_bucket()
        key = bucket.Object(path)
        return key

    def get_filename(self, path, new_filename=None):
        current_filename = os.path.basename(path)
        if new_filename is not None:
            filename, file_extension = os.path.splitext(current_filename)
            escaped_new_filename_base = re.sub(
                                            '[^A-Za-z0-9\#]+', 
                                            '-', 
                                            new_filename)
            escaped_filename = escaped_new_filename_base + file_extension
            return escaped_filename
        return current_filename

    def generate_url(self, path, download=True, new_filename=None):
        file_url = None
        aws_obj_key = self.get_key(path)
        if aws_obj_key:
            headers = None
            if download:
                filename = self.get_filename(path, new_filename=new_filename)
                headers = {
                    'response-content-type': 'application/force-download',
                    'response-content-disposition':'attachment;filename="%s"' % filename
                }
            file_url = aws_obj_key.generate_presigned_url(
                'get_object',
                Params={'ResponseCacheControl': 'no-cache', 'ResponseContentDisposition': headers.get('response-content-disposition')},
                ExpiresIn=self.expires
            )
        return file_url
