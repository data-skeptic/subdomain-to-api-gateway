# Subdomain to API Gateway

It is surprising difficult to use AWS in certain situations.  One of the worst is trying to route a subdomain (e.g. `api.dataskeptic.com`) to a particular stage in API gateway (e.g. `https://3aoo30oo3o.execute-api.us-east-2.amazonaws.com/prod/`).  This project is here to help.

As a developer on this project, you are **FORBIDDEN** from changing `app.py`.  It is set up, but design, in a very simple way to make sure your work is delivered in a format which is usable for us as a company.  You are free to change and update every other file, but DO NOT modify `app.py` without first getting explicit permission.  You may add default parameters in `worker.py`, but you MUST call the functions in `worker.py` as instructed in `app.py`.

Uses:

* Terraform
* Route53
* Misc AWS
