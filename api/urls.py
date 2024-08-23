from django.urls import path
from .views import RecipeListCreate, RecipeRetrieveUpdateDestroy
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('recipes/', RecipeListCreate.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDestroy.as_view(), name='recipe-detail'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
