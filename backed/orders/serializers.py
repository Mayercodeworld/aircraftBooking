from rest_framework import serializers
from .models import Order
from flights.serializers import FlightSerializer

class OrderSerializer(serializers.ModelSerializer):
    flight = FlightSerializer(read_only=True)  # 嵌套 FlightSerializer

    class Meta:
        model = Order
        fields = '__all__'