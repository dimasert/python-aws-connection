import boto3
import click

session = boto3.Session(profile_name='3r1ck')
ec2 = session.resource('ec2')

def filter_instances(project):
    instances = []

    if project:
        filters = [{'Name':'tag:Project','Values':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    return instances

@click.group()
def cli():
    """Program that manage AWS Account!"""

@cli.group('volumes')
def volumes():
    """Command for volumes"""
@cli.group('instances')
def instances():
    """Command for instances"""
@instances.command('list')
@click.option('--project',default=None, help="only instances for project(tag Project:<name>)")
def list_instances(project):
    "List EC2 instances"
    instances = filter_instances(project)

    for i in instances:

        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name
            )))
    return

@instances.command('stop')
@click.option('--project',default=None, help="only instances for project(tag Project:<name>)")
def stop_instances(project):
    "Stops EC2 Instances by project (TAG)"
    instances = filter_instances(project)

    for i in instances:
        print("Stopping {0}...".format(i.id))
        i.stop()
    return

@instances.command('start')
@click.option('--project',default=None, help="only instances for project(tag Project:<name>)")
def start_instances(project):
    "Start EC2 Instances by project (TAG)"
    instances = filter_instances(project)

    for i in instances:
        print("Starting {0}...".format(i.id))
        i.start()
    return

if __name__ == '__main__':
    cli()
