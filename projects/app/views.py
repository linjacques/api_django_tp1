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

@csrf_exempt
def post_json_view(request):
    body = json.loads(request.body)
    name = body.get("name")

    if not name:
        return JsonResponse({"error": "name requis"}, status=400)

    return JsonResponse({
            "name": name,
            "age": 30,
            "location": "New York",
            "is_active": True
        })