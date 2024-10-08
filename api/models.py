from django.db import models

class Recipe(models.Model):
    from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.CharField(max_length=120)
    blog = models.TextField() # A list of paragraphs for the blog
    ingredients = models.JSONField(default=list) # A list of ingredients
    steps = models.JSONField()  # A list of steps
    image = models.ImageField(upload_to='recipe_images/')  # Handles image uploads

    def __str__(self):
        return self.title