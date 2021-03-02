from django.urls import path
from . import views


urlpatterns = [
	path('', views.todoview, name='index'),
	path('add-todo/', views.add_todo, name='add-todo'),
	path('delete/<int:pk>/', views.delete, name="delete"),
]