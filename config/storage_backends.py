''' Set up storage for S3 in production '''
from storages.backends.s3boto3 import S3Boto3Storage

class MediaStorage(S3Boto3Storage):
    '''Class to manage media storage in S3'''
    location = 'media'
    file_overwrite = False