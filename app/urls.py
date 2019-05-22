from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('login/', views.login, name='app-login'),
    path('register/', views.register, name='app-register'),
]
