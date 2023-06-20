# Generated by Django 4.1.7 on 2023-03-30 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0030_alter_post_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contact",
            name="follower",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="follows",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]