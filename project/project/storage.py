# storage.py
# s3 연결!!
# pip install boto3
# pip install django-storages
from storages.backends.s3boto3 import S3Boto3Storage

class S3StaticStorage(S3Boto3Storage):
    location = 'static'


