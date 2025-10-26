from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from base.serializers import ProductSerializer
from base.models import Product




# ---ALL_PRODUCTS
@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serilizer = ProductSerializer(products, many=True)
    return Response(serilizer.data)


# ---ONE_PRODUCT
@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)


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
