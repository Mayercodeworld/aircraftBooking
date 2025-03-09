from django import forms
from .models import Order

# 用于管理员提交的表单
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'flight', 'name', 'passportNo', 'gender', 'country', 'price', 'status']