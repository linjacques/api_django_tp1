import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ..middleware.token import check_token  # assure-toi que le chemin est correct

@csrf_exempt
def retrieve_all(request):
    user, error = check_token(request)
    if error:
        return error

    page = int(request.GET.get('page', 1))
    page_size = 10
    data_dir = r"C:\Users\jacqu\Documents\Efrei\M1_2024_2025\data_integration1.5\TP_DataLake_DataWarehouse\datalake\transaction_log\2025-04-28"

    all_data = []

    for filename in sorted(os.listdir(data_dir)):
        filepath = os.path.join(data_dir, filename)
        if os.path.isfile(filepath) and filename.endswith(".json"):
            with open(filepath, 'r') as f:
                try:
                    content = json.load(f)
                    if isinstance(content, list):
                        all_data.extend(content)
                    else:
                        all_data.append(content)
                except Exception as e:
                    print(f"Erreur lecture {filename}:", e)

    # Pagination
    start = (page - 1) * page_size
    end = start + page_size
    paginated = all_data[start:end]

    # Projection des champs
    fields = request.GET.get('fields')
    if fields:
        fields = [f.strip() for f in fields.split(',')]
        paginated = [
            {k: item[k] for k in fields if k in item}
            for item in paginated
        ]

    return JsonResponse({
        "page": page,
        "total": len(all_data),
        "results": paginated
    }, safe=False)
