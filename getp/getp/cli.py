import click
import requests

from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='100013455674701', required=False)
def main(name, as_cowboy):
    """get image on facebook"""
    #greet = 'Howdy' if as_cowboy else 'Hello'
    #click.echo('{0}, {1}.'.format(greet, name))
	graph='https://graph.facebook.com/{}/picture?type=large'.format(name)
	req=requests.get(graph)
	img=Image.open(StringIO(req.content))
	img.show()
    
