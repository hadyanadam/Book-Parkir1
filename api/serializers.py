from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from .models import Parkir, Saldo, DeadlineParkir
from datetime import datetime
import pytz

class ParkirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parkir
        fields = ('user','booking_place','book_status')

class ParkirCustomSerializer(serializers.ModelSerializer):
    book_status = serializers.SerializerMethodField()
    class Meta:
        model = Parkir
        fields = ('user','booking_place','book_status')

    def get_book_status(self, obj):
        book_status = obj.book_status
        waktu_booking = obj.waktu_booking.waktu_booking
        if book_status and waktu_booking < datetime.now(pytz.utc):
            return True
        else:
            return False
class BookingTimeParkirSerializer(serializers.ModelSerializer):
    waktu_booking = serializers.SerializerMethodField()
    class Meta:
        model = Parkir
        fields = ('user','booking_place','book_status', 'waktu_booking')

    def get_waktu_booking(self,obj):
        waktu_booking = obj.waktu_booking.waktu_booking
        localtime = waktu_booking.astimezone(pytz.timezone('Asia/Jakarta'))
        return localtime.strftime("%Y-%m-%d %H:%M:%S%z")

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