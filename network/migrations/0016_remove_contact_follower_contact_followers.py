# Generated by Django 4.1.6 on 2023-02-18 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_contact_contact_network_con_up_time_31ed8f_idx'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='follower',
        ),
        migrations.AddField(
            model_name='contact',
            name='followers',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='followers', to=settings.AUTH_USER_MODEL),
        ),
    ]
