from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('<int:recipe_pk>/', views.recipe_detail_wish_recipe),
    path('list/', views.recipe_list),
]

