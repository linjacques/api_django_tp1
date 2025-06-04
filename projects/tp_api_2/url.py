from django.urls import path
from .views.user import register_user, login_user, profile
from .views.retrieve_datalake import retrieve_all
from .views.filter import filtered_transactions
from .handler.metrics_handler import money_last_5min, top_products, total_per_user_and_type
urlpatterns = [
    path("register/", register_user),
    path('login/', login_user),
    path('profile/', profile),
    path('datalake/', retrieve_all),
    path('filter/', filtered_transactions),
    path('transactions/', filtered_transactions),
    path('money_last_5min/', money_last_5min),
    path('total_per_user_type/', total_per_user_and_type),
    path('top_products/', top_products)
]
