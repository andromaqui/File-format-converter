from storages.backends.s3boto3 import S3Boto3Storage 
from django.conf import settings
import boto3
import time

class CsvStorage(S3Boto3Storage):    
    location = settings.AWS_CSV_LOCATION    
    file_overwrite = False

class StaticStorage(S3Boto3Storage):
	location = settings.AWS_STATIC_LOCATION