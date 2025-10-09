from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

# Create your views here.

# def getRoutes(request):
#      return JsonResponse('API is running...', safe=False)

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
        '/api/products/create/',
        '/api/products/upload/',
        '/api/products/<id>/reviews/',
        '/api/products/top/',
        '/api/products/<id>/',
        '/api/products/delete/<id>/',
        '/api/products/update/<id>/',

        '/api/users/login/',
        '/api/users/logout/',
        '/api/users/register/',
        '/api/users/profile/',
        '/api/users/profile/update/',

        '/api/orders/',
        '/api/orders/add/',
        '/api/orders/myorders/',
        '/api/orders/<id>/',
        '/api/orders/<id>/pay/',
        '/api/orders/<id>/deliver/',

    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    return Response(products)


@api_view(['GET'])
def getProduct(request,pk):
     product=None
     for i in products:
          if i['_id']==pk:
               product=i
               break
     
     return Response(product)
