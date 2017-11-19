import click
import requests

from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='100013455674701', required=False)
def main(name, as_cowboy):
    	"""get image on facebook"""
	graph='https://graph.facebook.com/{}/picture?type=large'.format(name)
    	req=requests.get(graph)
    	img=Image.open(StringIO(req.content))
    	img.show()
