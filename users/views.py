from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . serializers import UserModelSerializer
from rest_framework.response import Response
from rest_framework import status


class ListCreateUserView(ListCreateAPIView):
    model = User
    serializer_class = UserModelSerializer

    
    def get_queryset(self):
        return User.objects.all()


class RetriveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    model = User
    serializer_class = UserModelSerializer

    def get_queryset(self):
        return User.objects.all()


class LoginUserView(APIView):
    
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login bem-sucedido!'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Credenciais inválidas.'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutUserView(APIView):
    
    
    def get(self, request):
        logout(request)
        return Response({'message': 'Logout bem-sucedido!'}, status=status.HTTP_200_OK)



class CheckAuthentication(APIView):
    
    
    def post(self, request):
        return Response({'is_authenticated': True}, status=status.HTTP_200_OK)
