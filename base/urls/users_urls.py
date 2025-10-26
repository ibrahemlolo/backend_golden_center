from django.urls import path
from base.views import users_views as views


urlpatterns = [
    path('/login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('/regester', views.regesterUser, name="regester"),


    path('/', views.getUsers, name="users"),
    path('/profile/', views.getUserProfile, name="users-profile"),

]
