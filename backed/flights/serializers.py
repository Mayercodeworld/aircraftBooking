from rest_framework import serializers
from .models import Flight

def get_time_field(field_name):
    def method(self, obj):
        return getattr(obj.departure_time, field_name)
    return method

def get_weekday_name(self, obj):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[obj.departure_time.weekday()]

def get_arrival_time_field(field_name):
    def method(self, obj):
        return getattr(obj.arrival_time, field_name)
    return method

def get_arrival_weekday_name(self, obj):
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[obj.arrival_time.weekday()]

# 序列化数据，根据请求返回数据
class FlightSerializer(serializers.ModelSerializer):
    departure_year = serializers.SerializerMethodField()
    departure_month = serializers.SerializerMethodField()
    departure_day = serializers.SerializerMethodField()
    departure_hour = serializers.SerializerMethodField()
    departure_minute = serializers.SerializerMethodField()
    departure_weekday = serializers.SerializerMethodField()
    departure_weekday_name = serializers.SerializerMethodField()
    
    arrival_year = serializers.SerializerMethodField()
    arrival_month = serializers.SerializerMethodField()
    arrival_day = serializers.SerializerMethodField()
    arrival_hour = serializers.SerializerMethodField()
    arrival_minute = serializers.SerializerMethodField()
    arrival_weekday = serializers.SerializerMethodField()
    arrival_weekday_name = serializers.SerializerMethodField()

    class Meta:
        model = Flight
        fields = '__all__'

    # Departure time fields
    get_departure_year = get_time_field('year')
    get_departure_month = get_time_field('month')
    get_departure_day = get_time_field('day')
    get_departure_hour = get_time_field('hour')
    get_departure_minute = get_time_field('minute')
    get_departure_weekday = get_time_field('weekday')
    get_departure_weekday_name = get_weekday_name

    # Arrival time fields
    get_arrival_year = get_arrival_time_field('year')
    get_arrival_month = get_arrival_time_field('month')
    get_arrival_day = get_arrival_time_field('day')
    get_arrival_hour = get_arrival_time_field('hour')
    get_arrival_minute = get_arrival_time_field('minute')
    get_arrival_weekday = get_arrival_time_field('weekday')
    get_arrival_weekday_name = get_arrival_weekday_name