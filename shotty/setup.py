from setuptools import setup

setup (
    name = 'snapy',
    version = 0.1,
    Author = "Rohit Gupta",
    description = 'this is a tool to take snapshots of EC2 instances',
    pakages = ['shotty'],
    url = 'https://github.com/rohitgupta04/AWS-snapshots',
    install_requires = ['click','boto3'],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        '''
)
