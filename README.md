# AWS-snapshots
Demo project to manage EC2 instances and snapshots

## Configuring

Confiure the AWS user profile 'aws configure --profile shotty'

make sure to install boto3 and ipython using pipenv


## Running

pipenv run python shotty.py <type> <command>

*type* is instances, volumes or snapshots
*command* is list, start or stop
