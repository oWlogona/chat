from django.shortcuts import render
from .models import User, Dialog, Message
from django.http import HttpResponse
from django.http import JsonResponse


def home_page(request):
    if request.method == 'POST':
        data = request.POST
        my_sex = data.get('user_one_sex')
        my_age = data.get('user_one_age')
        partner_sex = data.get('user_two_sex')
        partner_age = data.get('user_two_age')
        print('my_sex: ', my_sex)
        print('my_age: ', my_age)
        print('partner_sex: ', partner_sex)
        print('partner_age: ', partner_age)
        i_user = User(sex=my_sex, age=my_age, name=my_sex)
        i_user.save(force_insert=True)
        search_dialog = Dialog.objects.filter(user_1_age=my_age, user_1_sex=my_sex, user_1__age=partner_age, user_1__sex=partner_sex)
        if search_dialog:
        	search_dialog = Dialog.objects.update(user_2=i_user)
        	return render(request, 'room_page.html', locals())
        waiting_chat = Dialog.objects.create(user_1=i_user, user_1_age=partner_age, user_1_sex=partner_sex)

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
