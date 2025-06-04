from django.http import JsonResponse
from rest_framework.authtoken.models import Token

def check_token(request):
    auth = request.META.get("HTTP_AUTHORIZATION")
    if not auth or not auth.startswith("Token "):
        return None, JsonResponse({"error": "Token manquant"}, status=401)

    token_key = auth.split("Token ")[1]
    try:
        user = Token.objects.get(key=token_key).user
        return user, None
    except Token.DoesNotExist:
        return None, JsonResponse({"error": "Token invalide"}, status=401)
