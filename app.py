import click
import worker


@click.command()
@click.option('--host', '-h', default='dataskeptic.com', prompt='Host')
@click.option('--subdomain', '-s', default='api', prompt='New subdomain')
@click.option('--destination', '-d', default='https://3aoo30oo3o.execute-api.us-east-2.amazonaws.com/prod/', prompt='The AWS API Gateway "root" with stage included.')
def attach(host, subdomain, destination):
    print(f'{subdomain}.{host} -> {destination}')
    response = worker.attach(host, subdomain, destination)
    print(response)


@click.group()
def cli():
    pass


cli.add_command(attach)


if __name__ == "__main__":
    cli()
