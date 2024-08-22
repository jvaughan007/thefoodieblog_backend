from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreate(generics.ListCreateAPIView):
    """
    Handles GET (list all recipes) and POST (create a new recipe) requests.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class RecipeRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles GET (retrieve a single recipe), PUT (update a recipe), and DELETE (delete a recipe) requests.
    """
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
