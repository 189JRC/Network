# Generated by Django 4.1.7 on 2023-03-30 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0029_post_like_delete_like"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="users_posts",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
