from django.shortcuts import render 
import json 
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
def test_json_view(request): 
 data = { 
 'name': 'John Doe', 
 'age': 30, 
 'location': 'New York', 
 'is_active': True, 
 } 
 return JsonResponse(data)