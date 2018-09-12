import boto3
import click

s3 = boto3.Session(profile_name='pyAutomation')
session = boto3.Session(profile_name='pyAutomation')
s3 = session.resource('s3')

@click.group()
def cli():
	"Webotron deploys websites to AWS"
	pass

@cli.command('list-buckets')
def list_buckets():
	"List all s3 buckets"
	for bucket in s3.buckets.all():
		print(bucket)

@cli.command('list-buckets-objects')
@click.argument('bucket')
def list_buckets_objects(bucket):
	"List objects inside the buckets"
	for object in s3.Bucket(bucket).objects.all():
		print(object)

if __name__ == '__main__':
	cli()
