# Generated by Django 4.1.7 on 2023-03-28 08:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0021_alter_post_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="liked_by",
                to="network.like",
            ),
        ),
    ]
