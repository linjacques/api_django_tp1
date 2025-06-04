from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from ..models.user import User
from ..middleware.token import check_token
import json

@csrf_exempt
def register_user(request):
    data = json.loads(request.body)
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return JsonResponse({"error": "Champs requis manquants"}, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({"error": "Nom d'utilisateur déjà pris"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    return JsonResponse({"message": f"Utilisateur {user.username} créé", "id": user.id}, status=201)

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")

    user = authenticate(username=username, password=password)
    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({"token": token.key})
    else:
        return JsonResponse({"error": "Identifiants invalides"}, status=status.HTTP_401_UNAUTHORIZED)
    
def profile(request):
    user, error = check_token(request)
    if error:
        return error

    return JsonResponse({"id": user.id, "username": user.username})