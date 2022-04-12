from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('about/', views.info, name='about'),
]