from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('<int:recipe_pk>/', views.recipe_detail_wish_recipe),
    path('<int:is_recommend>/<str:type>/', views.recipe_list),
]
