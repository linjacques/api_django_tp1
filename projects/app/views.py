from django.shortcuts import render 
import json 
from django.http import JsonResponse 
from django.views.decorators.csrf import csrf_exempt 
from .models import Product

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

def get_all_products(request):
        produits = Product.objects.all().values()
        return JsonResponse(list(produits), safe=False)

def get_most_expensive_product(request):
    produit = Product.objects.order_by('-price').first()
    data = {
            "id": produit.id,
            "name": produit.name,
            "price": produit.price,
            "description": produit.description,
        }
    return JsonResponse(data)

@csrf_exempt
def add_product(request):
    data = json.loads(request.body)
    name = data.get("name")
    price = data.get("price")
    description = data.get("description", "")
    product = Product.objects.create(
        name=name,
        price=price,
        description=description
    )

    return JsonResponse({
        "id": product.id,
        "name": product.name,
        "price": str(product.price),
        "description": product.description,
        "created_at": product.created_at.isoformat(),
        "updated_at": product.updated_at.isoformat()
    }, status=201)

@csrf_exempt
def update_product(request, product_id):
    data = json.loads(request.body)
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Produit non trouvé."}, status=404)

    name = data.get("name")
    price = data.get("price")
    description = data.get("description")

    if name:
        product.name = name
    if price:
        product.price = price
    if description is not None:
        product.description = description

    product.save()

    return JsonResponse({
        "id": product.id,
        "name": product.name,
        "price": str(product.price),
        "description": product.description,
        "created_at": product.created_at.isoformat(),
        "updated_at": product.updated_at.isoformat()
    })