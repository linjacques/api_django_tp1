from django.http import JsonResponse
from django.views.decorators.http import require_GET
from ..middleware.token import check_token
from ..views.metrics import compute_money_last_5min, compute_total_per_user_and_type, get_top_products

@require_GET
def money_last_5min(request):
    user, error = check_token(request)
    if error:
        return error

    total = compute_money_last_5min()
    return JsonResponse({"money_spent_last_5_minutes": total})

@require_GET
def total_per_user_and_type(request):
    user, error = check_token(request)
    if error:
        return error

    result = compute_total_per_user_and_type()
    return JsonResponse(result, safe=False)

@require_GET
def top_products(request):
    user, error = check_token(request)
    if error:
        return error

    try:
        x = int(request.GET.get("x", 5))
    except ValueError:
        return JsonResponse({"error": "Invalid value for parameter x"}, status=400)

    top = get_top_products(x)
    return JsonResponse(dict(top), safe=False)
