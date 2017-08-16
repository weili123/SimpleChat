import json

from django.http import HttpResponse
from channels import Channel
from channels.handler import AsgiHandler
from channels.sessions import channel_session

connections = {}


@channel_session
def ws_connect(message):
	name = message['path'].split('/')[-1]
	print name
	connections[name] = message.reply_channel.name
	print connections
	message.reply_channel.send({"accept": True})


def ws_message(message):
	print message.content['text']
	data = json.loads(message.content['text'])
	receiver = data['receiver_name']
	try:
		Channel(connections[receiver]).send({
			"text": message.content['text']
			})
	except Exception:
		pass