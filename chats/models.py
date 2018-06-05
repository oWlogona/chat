from django.db import models

class User(models.Model):
	name = models.CharField(max_length=32)
	age = models.IntegerField(default=10)
	sex = models.CharField(max_length=10)

class Dialog(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	sender = models.CharField(max_length=32)
	receiver = models.CharField(max_length=32)

class Message(models.Model):
	dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
	sender = models.CharField(max_length=32)
	receiver = models.CharField(max_length=32)