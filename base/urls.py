from django.urls import path
from .views import getProducts, getProduct, getRoutes


urlpatterns = [
    path('', getRoutes, name="routes"),
    path('products', getProducts, name="routes"),
    path('products/<str:pk>', getProduct, name="routes"),
]


