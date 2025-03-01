# your_project/api_urls.py
from django.urls import path
from . import api_views  # create your API views module


urlpatterns = [
    path('', index, name="index"),
    path('login', index, name="login"),
    path('signup', index, name="signup"),
    path('register/<str:competition>', index, name="register"),
    path('competitions', index, name="competition"),
]