from django.urls import path
from .views.user import register_user, login_user, profile
from .views.retrieve_datalake import retrieve_all
from .views.filter import filtered_transactions
urlpatterns = [
    path("register/", register_user),
    path('login/', login_user),
    path('profile/', profile),
    path('datalake/', retrieve_all),
    path('filter/', filtered_transactions)
]
