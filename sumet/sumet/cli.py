import click
import requests

from bs4 import BeautifulSoup
from PIL import Image
from StringIO import StringIO

@click.command()
@click.option('--as-cowboy', '-c', is_flag=True, help='Greet as a cowboy.')
@click.argument('name', default='100013455674701', required=False)
def main(name, as_cowboy):
    	"""get image on facebook"""
	if 0<=ord(name[0])<=9:
		graph='https://graph.facebook.com/{}/picture?type=large'.format(name)
	else:
		url='https://www.facebook.com/{}'.format(name)
		html=requests.get(url)
		b=BeautifulSoup(html.content,'html.parser')
		Facebook_id=b.find_all('meta')[7]['content'].replace('fb://profile/','')
		graph='https://graph.facebook.com/{}/picture?type=large'.format(Facebook_id)
    	req=requests.get(graph)
    	img=Image.open(StringIO(req.content))
    	img.show()
