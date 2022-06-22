from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('material/', views.material),
    path('<int:recipe_pk>/', views.recipe_detail_wish_recipe),
    path('list/', views.list),
]

