# Generated by Django 4.1.6 on 2023-02-17 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_alter_post_id_alter_profile_id_alter_profile_photo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_time', models.DateTimeField(auto_now_add=True)),
                ('followed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='is_followed_by', to=settings.AUTH_USER_MODEL)),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_is_following', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-up_time'],
            },
        ),
        migrations.AddIndex(
            model_name='contact',
            index=models.Index(fields=['-up_time'], name='network_con_up_time_31ed8f_idx'),
        ),
    ]
