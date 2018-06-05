from django.contrib import admin
from .models import User, Dialog, Message

class UserAdmin(admin.ModelAdmin):
	list_display = [field.name for field in User._meta.fields]

class DialogAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Dialog._meta.fields]

class MessageAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Message._meta.fields]

admin.site.register(User, UserAdmin)
admin.site.register(Dialog, DialogAdmin)
admin.site.register(Message, MessageAdmin)