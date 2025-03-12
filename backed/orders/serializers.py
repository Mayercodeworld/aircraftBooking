from rest_framework import serializers
from .models import Order
from flights.models import Flight, Seat
from flights.serializers import FlightSerializer, SeatSerializer

class OrderSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)  # 嵌套 FlightSerializer
    seat = SeatSerializer(read_only=True)  # 嵌套 SeatSerializer

    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateSerializer(serializers.ModelSerializer):
    flight = serializers.PrimaryKeyRelatedField(queryset=Flight.objects.all())
    seat = serializers.PrimaryKeyRelatedField(queryset=Seat.objects.all())

    class Meta:
        model = Order
        fields = '__all__'