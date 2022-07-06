from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/', views.profile),
    path('ingredients/', views.ingredients),
    path('<int:ingredient_pk>/', views.ingredient_add_delete),
]