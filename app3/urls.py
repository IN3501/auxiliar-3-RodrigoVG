from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('pagina2/', views.pagina2, name='pagina2'),
	path('inputs/', views.inputs, name='inputs'),
	]