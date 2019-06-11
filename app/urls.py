from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='app-home'),
    path('about/', views.about, name='app-about'),
    path('login/', views.user_login, name='app-login'),
    path('register/', views.user_register, name='app-register'),
    path('logout', views.user_logout, name='app-logout'),
    path('makeDrink/', views.makeDrink, name='app-makeDrink'),
]
