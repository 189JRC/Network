# Generated by Django 4.1.7 on 2023-03-29 14:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0028_remove_post_like_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="like",
            field=models.ManyToManyField(
                blank=True, related_name="liked_by", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.DeleteModel(
            name="Like",
        ),
    ]
