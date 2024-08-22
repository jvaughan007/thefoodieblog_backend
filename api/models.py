from django.db import models

class Recipe(models.Model):
    from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField()
    steps = models.JSONField()  # A list of steps
    image = models.ImageField(upload_to='images/')  # Handles image uploads

    def __str__(self):
        return self.title