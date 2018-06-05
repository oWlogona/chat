from django.shortcuts import render
from .models import User, Dialog, Message


def home_page(request):
	return render(request, 'chats/home_page.html', locals())

def room(request):
	return render(request, 'chats/room.html', locals())

def get_messages(request, dialog_id):
	pass

def get_user(request, preference):
	pass
