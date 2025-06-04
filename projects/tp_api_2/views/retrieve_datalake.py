import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def retrieve_all(request):
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

    start = (page - 1) * page_size
    end = start + page_size
    paginated = all_data[start:end]
    print("Contenu du dossier :", os.listdir(data_dir))
    print("Nombre de fichiers JSON lus :", len(all_data))

    return JsonResponse({
        "page": page,
        "total": len(all_data),
        "results": paginated
    }, safe=False)
