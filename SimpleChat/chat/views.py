# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.http import Http404, JsonResponse
from django.shortcuts import render

from .controller.user_controller import get_or_create_user_id_from_name as get_or_create_user_id
from .controller.user_controller import get_user_id_from_name as get_user_id
from .controller.user_message_controller import UserMessageController

from .controller.user_message_controller import UserMessageController

def index(request):
    return render(request, 'index.html')

def talk(request):
	username = request.POST.get("username", "")
	if not username:
		raise Http404("Enter a valid username")

	user_id = get_or_create_user_id(username)
	stream = UserMessageController(user_id)
	context = {
		'user_id': user_id,
		'user_name': username,
		'messages': stream.get_existing_messages()
	}

	# create user if not exist
	# get all messages for that user from db
	# open keep alive connection and listen for new messages
	return render(request, 'talk.html', context)

def send_message(request):
	receiver_name = request.POST.get("username", "")
	sender_name = request.POST.get("sender_name", "")
	receiver_id = None
	if receiver_name:
		receiver_id = get_user_id(receiver_name)
	sender_id = request.POST.get("user_id", 0)
	message = request.POST.get("message", "")

	if not receiver_id or not message or not sender_id:
		return JsonResponse({"success": False, "reason": "bad input"})

	controller = UserMessageController(sender_id)
	timestamp = datetime.datetime.now()
	controller.post_message(timestamp, receiver_id, message)

	return JsonResponse({"success": True, "receiver_name": receiver_name, "sender_name": sender_name, "message": message, "timestamp": timestamp.strftime("%c")});