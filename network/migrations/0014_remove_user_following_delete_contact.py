# Generated by Django 4.1.6 on 2023-02-18 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_user_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='following',
        ),
        migrations.DeleteModel(
            name='Contact',
        ),
    ]
