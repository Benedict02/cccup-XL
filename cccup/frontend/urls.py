from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path('login', index, name="login"),
    path('signup', index, name="signup"),
    path('register/<str:competition>', index, name="register"),
    path('competitions', index, name="competition"),
]