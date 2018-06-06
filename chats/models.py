from django.db import models

class User(models.Model):
	name = models.CharField(max_length=32, default='anonimus')
	age = models.IntegerField(default=10)
	sex = models.CharField(max_length=10)

	def __str__(self):
		return "{} {}".format(self.sex, self.age)

class Dialog(models.Model):
	user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_1')
	user_2 = models.ForeignKey(User, blank=True, null=True, default=None, on_delete=models.CASCADE, related_name='user_2')
	user_1_age = models.IntegerField(default=10)
	user_1_sex = models.CharField(max_length=10, default='secret')
	user_2_age = models.IntegerField(default=10)
	user_2_sex = models.CharField(max_length=10, default='secret')

class Message(models.Model):
	dialog = models.ForeignKey(Dialog, on_delete=models.CASCADE)
	sender = models.CharField(max_length=32)
	receiver = models.CharField(max_length=32)