import boto3
import click

session = boto3.Session(profile_name='shotty')
ec2=session.resource('ec2')

@click.group()
def cli():
    """Shotty manages snapshots"""

@cli.group('volumes')
def volumes():
    """Commands for instances"""

@cli.group('instances')
def instances():
    """Commands for instances"""

@cli.group('snapshots')
def snapshots():
    """Commands for snapshots"""


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
        if i.state['Name'] != 'terminated':
            i.stop()
    return

@instances.command('start')
def start_instances():
    "Start ec2 instances"
    instances=[]
    instances=ec2.instances.all()
    for i in instances:
        print("starting ".format (i.id))
        if i.state['Name'] != 'terminated':
            i.start()
    return

@volumes.command('list')
def list_volumes():
    "list ec2 volumes"
    vols=[]
    instances=[]
    vols=ec2.volumes.all()
    instances=ec2.instances.all()
    for i in instances:
        if i.state['Name'] != 'terminated':
            print (i)
            for v in i.volumes.all():
                print(",".join((
                v.id,
                i.id,
                v.state,
                str(v.size)+ "GiB",
                v.encrypted and "Encrypted" or "Not Encrypted"
                )))
    return

@snapshots.command('list')
def list_snapshots():
    "list ec2 volume snapshots"
    vols=[]
    instances=[]
    snapshots=[]
    vols=ec2.volumes.all()
    instances=ec2.instances.all()
    for i in instances:
        if i.state['Name'] != 'terminated':
            print (i)
            for v in i.volumes.all():
                print(v)
                for s in v.snapshots.all():
                    print (",".join((
                    s.id,
                    s.state,
                    s.progress
                    )))
    return

@instances.command('snapshot', help="Create snapshot of all volumes")
def create_snapshot():
    "Create snapshots of EC2 instances"

    for i in instances():
        for v in i.volumes.all():
            print("creating snapshot of {0}".format(v.id))
            v.create_snapshot(Description="Created by Shotty")
    return

if __name__ == '__main__':
    cli()
