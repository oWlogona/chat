from django.shortcuts import render
from .models import User, Dialog, Message
from django.http import HttpResponse
import json


def home_page(request):
	if request.method == 'POST':
		print(request.POST)
	return render(request, 'home_page.html', locals())

def room(request):
	return render(request, 'room_page.html', locals())

def get_messages(request, dialog_id):
	message = Message.objects.get(dialog=dialog_id)
	data = json.dumps(message)
	return HttpResponse(data)

def get_user(request, user_id):
	user = User.objects.get(user=user_id)
	data = json.dumps(user)
	return HttpResponse(data)
