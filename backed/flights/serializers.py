from rest_framework import serializers
from .models import Flight, Seat

# 序列化数据，根据请求返回数据
class FlightSerializer(serializers.ModelSerializer):
    remaining_seats = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Flight
        fields = '__all__'  # 或者显式列出所有字段 + 'remaining_seats'

    def get_remaining_seats(self, obj):
        return obj.remaining_seats

class SeatSerializer(serializers.ModelSerializer):
    is_booked = serializers.SerializerMethodField()

    class Meta:
        model = Seat
        fields = ['id', 'seat_number', 'status', 'is_booked']
    def get_is_booked(self, obj):
        return obj.status == 'booked'

    