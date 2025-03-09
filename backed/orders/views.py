from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
