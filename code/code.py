import boto3

if __name__ == '__main__':

    session = boto3.session(profile_name='3r1ck')
    ec2 = session.resource('ec2')

    for i in ec2.instances.all():
        print(i)
