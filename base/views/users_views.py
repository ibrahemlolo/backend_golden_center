from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from base.serializers import UserSerializerWithToken, UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs: dict[str]) -> dict[str, str]:
        data = super().validate(attrs)

        # Add custom claims
        serializer = UserSerializerWithToken(self.user).data
        for k, v in serializer.items():
            data[k] = v
        # ...

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer




# ---CREATE_USER
@api_view(['POST'])
def regesterUser(request):
    data = request.data
    try:
        user = User.objects.create(
            first_name=data['name'],
            username=data['email'],
            email=data['email'],
            password=make_password(data['password'])
        )
        serializer = UserSerializerWithToken(user, many=False)
        return Response(serializer.data)
    except:
        message = {'detail': 'User with this email already exists try to login'}
        return Response(message, status=400)


# ---USER_PROFILE
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getUserProfile(request):
    user = request.user
    serilizer = UserSerializer(user, many=False)
    return Response(serilizer.data)


# ---USER
@api_view(['GET'])
@permission_classes([IsAdminUser])
def getUsers(request):
    users = User.objects.all()
    serilizer = UserSerializer(users, many=True)
    return Response(serilizer.data)




