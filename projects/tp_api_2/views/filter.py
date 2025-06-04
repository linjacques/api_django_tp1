import os
import json
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from ..middleware.token import check_token

data_dir = r"C:\Users\jacqu\Documents\Efrei\M1_2024_2025\data_integration1.5\TP_DataLake_DataWarehouse\datalake\transaction_log\2025-04-28"

filters_eq = ['payment_method', 'country', 'product_category', 'status']

filters_num = {
    'amount': float,
    'customer_rating': float
}

def passes_filters(item, request):
    
    for key in filters_eq:
        val = request.GET.get(key)
        if val:
            if key == "country":
                nested_val = item.get("location", {}).get("country", "")
                if val.lower() != str(nested_val).lower():
                    return False
            else:
                if val.lower() != str(item.get(key, "")).lower():
                    return False

    for key, caster in filters_num.items():
        for suffix, op in [('gt', lambda a, b: a > b),
                           ('lt', lambda a, b: a < b),
                           ('eq', lambda a, b: a == b)]:
            param = f"{key}__{suffix}"
            val = request.GET.get(param)
            if val is not None:
                try:
                    item_val = caster(item.get(key, 0))
                    filter_val = caster(val)
                    if not op(item_val, filter_val):
                        return False
                except:
                    return False
    return True

@require_GET
def filtered_transactions(request):
    user, error = check_token(request)
    if error:
        return error

    results = []

    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            path = os.path.join(data_dir, filename)
            with open(path, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    for item in data:
                        if passes_filters(item, request):
                            results.append(item)
                except json.JSONDecodeError:
                    continue 

    return JsonResponse(results, safe=False)
