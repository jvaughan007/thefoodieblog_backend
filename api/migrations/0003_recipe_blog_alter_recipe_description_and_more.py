# Generated by Django 5.1 on 2024-08-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0002_recipe_ingredients"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="blog",
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(upload_to="recipe_images/"),
        ),
    ]
