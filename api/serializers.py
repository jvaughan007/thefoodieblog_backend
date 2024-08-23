from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['id', 'title', 'author', 'description', 'blog', 'ingredients', 'steps', 'image']
    
    # Adding validation to fields to ensure they are provided and not empty
    title = serializers.CharField(max_length=255, required=True)
    author = serializers.CharField(max_length=255, required=True)
    description = serializers.CharField(required=True)
    blog = serializers.JSONField(required=True)
    ingredients = serializers.JSONField(required=True)
    steps = serializers.JSONField(required=True)
    image = serializers.ImageField(required=True)

    def validate_ingredients(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("Ingredients must be a non-empty list.")
        return value

    def validate_steps(self, value):
        if not isinstance(value, list) or len(value) == 0:
            raise serializers.ValidationError("Steps must be a non-empty list.")
        return value
