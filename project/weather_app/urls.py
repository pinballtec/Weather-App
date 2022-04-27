from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('about/', views.info, name='about'),
    path('faq/', views.faq, name='faq'),
    path('<id>/delete', views.delete_view, name='delete'),
]