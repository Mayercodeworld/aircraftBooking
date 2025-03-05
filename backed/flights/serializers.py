from rest_framework import serializers
from .models import Flight

# 序列化数据，根据请求返回数据
class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'