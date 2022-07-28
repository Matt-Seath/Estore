from django.urls import path
from . import views

#URL Conf
urlpatterns = [
    path('greet/', views.greet_user)
]