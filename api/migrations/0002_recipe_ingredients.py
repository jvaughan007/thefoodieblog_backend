# Generated by Django 5.1 on 2024-08-22 16:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="ingredients",
            field=models.JSONField(default=list),
        ),
    ]
