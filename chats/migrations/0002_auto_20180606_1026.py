# Generated by Django 2.0.6 on 2018-06-06 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dialog',
            name='user',
        ),
        migrations.AlterField(
            model_name='dialog',
            name='user_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_1', to='chats.User'),
        ),
        migrations.AlterField(
            model_name='dialog',
            name='user_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_2', to='chats.User'),
        ),
    ]