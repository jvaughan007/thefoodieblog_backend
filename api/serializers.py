from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['title', 'author', 'description', 'steps', 'image']

    def validate_steps(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError("Steps must be a list.")
        return value

