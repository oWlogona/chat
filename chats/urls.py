from django.urls import path
from . import views

urlpatterns = [
	path('', views.home_page, name="home_page"),
	path('room/', views.room, name="home_page"),
	path('get_messages/<int:dialog_id>/', views.get_messages, name='get_messages'),
	path('get_user/<int:user_id>', views.get_user, name='get_user'),
]