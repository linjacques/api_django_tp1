from django.urls import path 
from . import views 
urlpatterns = [ 
 path("test_json_view", views.test_json_view, name="test_json_view"), 
 path("post_json_view", views.post_json_view, name="post_json_view")
] 

