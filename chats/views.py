from django.shortcuts import render
from .models import User, Dialog, Message
from django.http import HttpResponse
import json


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
        #i_user = User(sex=my_sex, age=my_age, name=my_sex)
        #i_user.save(force_insert=True)

        search_dialog = Dialog.objects.get(
            user_1_age=partner_age, user_1_sex=partner_sex, user_2_age=my_age, user_2_sex=my_sex, user_2=None)
        if not search_dialog:
            waiting_dialog = Dialog.objects.get(
                user_1_age=my_age, user_1_sex=my_sex, user_2_age=partner_age, user_2_sex=partner_sex, user_2=None)
            print(waiting_dialog)
        partner = User.objects.filter(sex=partner_sex, age=partner_age)
        print(partner)

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
