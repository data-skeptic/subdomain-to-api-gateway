import os
import time
import re
from pythonping import ping

def overwrite_check(absfilename):
    if os.path.exists(absfilename):
        raise Exception(f'File {absfilename} already exists.')

def ping_address(url):
    try:
        response_list = ping(url)
        return response_list.success()
    except Exception:
        return False

def parse_destination(destination, variables):
    pattern = re.compile(r'\/\/(.*)\..*\.(.*)\..*\..*\/(.*)\/')
    matches = pattern.findall(destination)
    if len(matches) != 1 or len(matches[0]) !=3 :
        error = f'Failed to match {destination} with expected format.'
        raise Exception(error)

    variables['api-id'] = matches[0][0]
    variables['region'] = matches[0][1]
    variables['stage'] = matches[0][2]

def attach(host, subdomain, destination):
    response = {}
    response['status'] = 'INITIALIZING'
    
    variables = {'host': host, 'subdomain': subdomain}
    parse_destination(destination, variables)

    if ping_address(f'{subdomain}.{host}'):
        error = f'Subdomain {subdomain}.{host} already exists.'
        raise Exception(error)

    # TODO: ping destination, raise EXCEPTION if non-200
    # API Gateway doesn't allow ping, so to check I suggest to use AWS SDK (boto3). Probably same can be done for subdomain 

    fn = 'setup.tfvars'
    overwrite_check(fn)
    tfvars = ""
    for k, v in variables.items():
        tfvars += f'{k} = "{v}"\r\n'
    f = open(fn, 'w')
    f.write(tfvars)
    f.close()
    
    ts = int(time.time() * 1000)
    response['tf_plan'] = f'{ts}.plan.txt'
    os.system(f'terraform plan -var-file="setup-static.tfvars" -var-file="setup.tfvars" -out {ts}.plan.txt')
    
    response['status'] = 'NOT TESTED (soon: SUCCESS)'
    return response
