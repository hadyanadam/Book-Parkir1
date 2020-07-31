# from django.shortcuts import render, get_object_or_404
# from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from .serializers import ParkirSerializer, UserSerializer, SaldoSerializer, ParkirCustomSerializer, BookingTimeParkirSerializer
from django.contrib.auth.models import User

from .models import Parkir, Saldo

# @csrf_exempt
class ParkirList(generics.ListCreateAPIView):
    queryset = Parkir.objects.all()
    serializer_class = ParkirSerializer

# # @csrf_exempt
class ParkirDetail(generics.RetrieveUpdateAPIView):
    lookup_field = 'booking_place'
    queryset = Parkir.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = ParkirSerializer

class ParkirDetailValidation(generics.RetrieveUpdateAPIView):
    lookup_field = 'booking_place'
    queryset = Parkir
    authentication_classes = ()
    permission_classes = ()
    serializer_class= ParkirCustomSerializer

class ParkirDetailValidationList(generics.ListAPIView):
    queryset = Parkir
    authentication_classes = ()
    permission_classes = ()
    serializer_class= ParkirCustomSerializer

class BookingTimeList(generics.ListAPIView):
    queryset = Parkir.objects.all()
    serializer_class = BookingTimeParkirSerializer

class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer

class SaldoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = Saldo.objects.all()
    authentication_classes = ()
    permission_classes = ()
    serializer_class = SaldoSerializer
class LoginView(APIView):
    permission_classes = ()

    def post(self, request,):
        print(request.headers)
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)

