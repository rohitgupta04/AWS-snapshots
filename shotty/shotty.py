import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')
def list_instances():
    "List ec2 instances"
    instances=[]
    instances=ec2.instances.all()
    for i in instances:
        print(', '.join((
        i.id,
        i.instance_type,
        i.placement['AvailabilityZone'],
        i.state['Name'],
        i.public_dns_name)))

@instances.command('stop')
def stop_instances():
    "Stop ec2 instances"
    instances=[]
    instances=ec2.instances.all()
    for i in instances:
        print("stopping ".format (i.id))
        i.stop()
    return

@instances.command('start')
def start_instances():
    "Start ec2 instances"
    instances=[]
    instances=ec2.instances.all()
    for i in instances:
        print("starting ".format (i.id))
        i.start()
    return

if __name__ == '__main__':
    instances()
