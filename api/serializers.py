from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Parkir, Saldo, DeadlineParkir

class ParkirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkir
        fields = ('user','booking_place','book_status')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

class SaldoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Saldo
        fields = '__all__'

class DeadlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeadlineParkir
        field = '__all__'