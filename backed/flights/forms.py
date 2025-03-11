from django import forms
from .models import Flight

# 用于管理员提交的表单
class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_no', 'departure_city', 'arrival_city', 'departure_time', 'arrival_time',  'price', 'aircraft', 'airline']