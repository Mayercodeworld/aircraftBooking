from rest_framework import serializers
from .models import Flight, Seat

# 序列化数据，根据请求返回数据
class FlightSerializer(serializers.ModelSerializer):
    remaining_seats = serializers.IntegerField(source='get_available_seats', read_only=True)
    class Meta:
        model = Flight
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'