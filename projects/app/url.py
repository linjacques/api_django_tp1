from django.urls import path 
from . import views 
urlpatterns = [ 
 path("test_json_view", views.test_json_view, 
name="test_json_view"), 
] 

