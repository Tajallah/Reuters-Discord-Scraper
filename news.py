import discord
import asyncio
from discord.ext import commands
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError

def openlink (url):
	print('opening link %s'%(url))
	html = urlopen(url)
	z = riplinks(html, url)
	print(z)
	return z

def riplinks (html, url):
	q = []
	print('ripping links')
	soup = BeautifulSoup(html, 'lxml')
	for a in soup.find_all('a', href=True):
		if '/article' in a['href']:
			q.append(url+a['href'])
			print('%i found.'%(len(q)))
	print('%i found.'%(len(q)))
	return q

def doall (site):
	print('starting')
	q = openlink(site)
	return q

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('-----------')

@client.event
async def on_message(message):
	if (message.content.startswith('!headlines')):
		x = message.content.replace('!headlines', '')
		if x == '':
			x = 10
		elif x[0] != ' ' :
			x = 10
		else:
			x = int(x.replace(' ', ''))
			
		links = doall("https://www.reuters.com")
		await client.send_message(message.channel, 'Here are some headlines for you.')
		print(links)
		print('Printing headlines')
		for n in range(0, x):
			await client.send_message(message.channel, '%s'%(links[n]))
	
	elif (message.content == 'END NEWS MODULE'):
		await client.send_message(message.channel, 'News module shutting down')
		client.close()
		raise SystemExit

client.run('MjkxNDc5OTE4MDQ5NjI0MDY1.DPkOcQ.bF5gWMX8_-3ZKjFlnCBX8M3zOb0')
