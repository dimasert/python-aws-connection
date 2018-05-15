import boto3

session = boto3.session(profile_name='3r1ck')
ec2 = session.resource('ec2')

def list_instances():
    for i in ec2.instances.all():
        print(i)

if __name__ == '__main__':
    list_instances()
