import os
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from tp_api_2.middleware.token import check_token

DATA_LAKE_DIR = r"C:\Users\jacqu\Documents\Efrei\M1_2024_2025\data_integration1.5\TP_DataLake_DataWarehouse\datalake\transaction_log"

@require_GET
def list_data_lake_resources(request):
    user, error = check_token(request)
    if error:
        return error

    try:
        resources = [
            name for name in os.listdir(DATA_LAKE_DIR)
            if os.path.isdir(os.path.join(DATA_LAKE_DIR, name))
        ]
        return JsonResponse({"resources": sorted(resources)}, status=200)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
