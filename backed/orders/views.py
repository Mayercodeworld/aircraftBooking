from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .models import Order


@api_view(['GET'])
def get_user_tickets(request, user_id):
    # 根据 user_id 查找所有匹配的 Order 行
    orders = Order.objects.filter(user_id=user_id)

    # 将查询结果转换为列表
    order_list = [
        {
            'order_id': order.order_id,
            'date': order.date,
            'price': order.price,
            'status': order.status
        }
        for order in orders
    ]
    print(order_list)
    #监测这个用户有没有订单，没有返回
    if len(order_list) == 0:
        return Response({'code': 1, 'msg': '该用户没有订单'}, status=400)

    # 返回结果
    return Response(order_list)

@api_view(['POST'])
def create_order(request):
    user_id = request.data.get('user')
    flight_id = request.data.get('flight')
    passport_id = request.data.get('passportNo')

    # 检查是否存在具有相同 user_id, flight_id, passport_id 的订单
    existing_order = Order.objects.filter(user=user_id, flight=flight_id, passportNo=passport_id).first()
    if existing_order:
        return Response({'code': 1, 'msg': '该用户已经存在相同的订单'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # print('Validation errors:', serializer.errors)  # 打印验证错误信息
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 