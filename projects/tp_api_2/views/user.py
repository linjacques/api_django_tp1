from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..models.User import User
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

    user = User.objects.create(username=username, email=email, password=password)
    return JsonResponse({"message": f"Utilisateur {user.username} créé", "id": user.id}, status=201)