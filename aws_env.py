import boto3
s3 = boto3.Session(profile_name='pyAutomation')
session = boto3.Session(profile_name='pyAutomation')
s3 = session.resource('s3')
