# Generated by Django 4.1.6 on 2023-02-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_up',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]