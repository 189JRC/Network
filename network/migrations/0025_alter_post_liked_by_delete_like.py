# Generated by Django 4.1.7 on 2023-03-28 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("network", "0024_remove_post_liked_by_post_liked_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True, related_name="liked_by", to="network.profile"
            ),
        ),
        migrations.DeleteModel(
            name="Like",
        ),
    ]
