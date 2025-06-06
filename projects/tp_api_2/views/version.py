from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_GET
from ..middleware.token import check_token
import os
import json

base_dir = r"C:\Users\jacqu\Documents\Efrei\M1_2024_2025\data_integration1.5\TP_DataLake_DataWarehouse\datalake\transaction_log"

@require_GET
def get_versioned_data(request):
    user, error = check_token(request)
    if error:
        return error

    date = request.GET.get("date")  # Ex: '2025-04-28'
    if not date:
        return JsonResponse({"error": "Missing date parameter"}, status=400)

    version_dir = os.path.join(base_dir, date)
    if not os.path.exists(version_dir):
        return JsonResponse({"error": "Version not available"}, status=404)

    data = []
    for filename in os.listdir(version_dir):
        if filename.endswith(".json"):
            with open(os.path.join(version_dir, filename), "r", encoding="utf-8") as f:
                try:
                    data.extend(json.load(f))
                except json.JSONDecodeError:
                    continue
    return JsonResponse(data, safe=False)
