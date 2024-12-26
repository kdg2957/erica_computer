from django.urls import path
from . import views

app_name = "users"
urlpatterns = [
    path('', views.login_request, name='login'), # main - login page
    path('home/', views.home_request, name='home'),
]