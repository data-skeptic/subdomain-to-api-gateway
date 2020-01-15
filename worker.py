import os
import time


def overwrite_check(absfilename):
    if os.path.exists(absfilename):
        raise Exception("File {absfilename} already exists.")


def attach(host, subdomain, destination):
    response = {}
    response['status'] = 'INITIALIZING'
    # TODO: check if subdomain exists in DNS.  If yes, raise Exception
    # TODO: ping destination, raise EXCEPTION if non-200
    # TODO: use boto3 to query AWS for any important details such as VPC information
    # TODO: Use command line interface to ask user questions, if necessary
    fn = 'setup.tfvars'
    overwrite_check(fn)
    tfvars = "write all variables to it (e.g. subdomain, VPC, etc)"
    f = open(fn, 'w')
    f.write(tfvars)
    f.close()
    # TODO: check if `setup.tf` exists in the current location.  If so, raise Exception
    # TODO: generate Terraform recipe and save it as `setup.tf`
    # TODO: Terraform recipe uses Route53 and other services to  connect subdomain to destination
    # TODO: Run `terraform plan` via something like `os.command`.  Capture results to `terraform.plan.txt`
    ts = int(time.time() * 1000)
    response['tf_plan'] = f'{ts}.plan.txt'
    response['status'] = 'NOT IMPLEMENTED (soon: SUCCESS)'
    return response
