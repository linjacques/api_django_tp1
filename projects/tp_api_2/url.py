from django.urls import path
from .views.User import register_user

urlpatterns = [
    path("register/", register_user)
]
