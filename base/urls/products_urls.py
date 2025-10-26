from django.urls import path
from base.views import products_views as views


urlpatterns = [
    path('/routs', views.getRoutes, name="routes"),
    path('/', views.getProducts, name="routes"),
    path('/<str:pk>', views.getProduct, name="routes"),
]
