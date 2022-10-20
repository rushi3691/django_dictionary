from django.urls import path 
from . import views

urlpatterns = [
    path('', views.getAll.as_view()),
    path('<int:id>', views.getOneByID.as_view()),
    path('<str:word>', views.getSearches.as_view()),
]