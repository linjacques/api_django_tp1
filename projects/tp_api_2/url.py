from django.urls import path
from .views.user import register_user
from .views.user import login_user

urlpatterns = [
    path("register/", register_user),
    path('login/', login_user),
]
