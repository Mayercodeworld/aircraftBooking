from django.shortcuts import render
from django.db import transaction
from django.utils import timezone
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer, OrderCreateSerializer
from .models import Order
from flights.models import Flight, Seat  


@api_view(['GET'])
def get_user_tickets(request, user_id):
    # 根据 user_id 查找所有匹配的 Order 行
    orders = Order.objects.filter(user_id=user_id)
    # 获取当前时间
    now = timezone.now()
    print(now)
    # 遍历每个订单，更新状态
    for order in orders:
        flight = order.flight
        departure_time = flight.departure_time
        arrival_time = flight.arrival_time
        # print(departure_time)
        # print(arrival_time)
        if now > departure_time and now < arrival_time and order.status == '等待出行':
            order.status = '进行中'
        elif now > arrival_time and order.status == '进行中' or order.status == '等待出行':
            order.status = '已结束'
        # print(order.status)
        order.save()

    # 使用 OrderSerializer 序列化订单数据
    serializer = OrderSerializer(orders, many=True)

    # 检查是否有订单
    if not serializer.data:
        return Response({'code': 1, 'msg': '该用户没有订单'}, status=400)

    # 返回结果
    return Response(serializer.data)

@api_view(['POST'])
def is_order_exist(request):
    request.data['user'] = int(request.data.get('user'))
    request.data['flight'] = int(request.data.get('flight'))
    # print(request.data)
    if existing(request):
        return Response({'code': 401, 'msg': '订单已存在，请勿重复购买'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'code': 0, 'msg': '该用户没有相同的订单'}, status=status.HTTP_200_OK)
    
def existing(request):
    existing_order = Order.objects.filter(
        user=request.data.get('user'), 
        flight=request.data.get('flight'), 
        passportNo=request.data.get('passportNo'), 
        name=request.data.get('name'), 
        status__in=['等待出行', '进行中']
    ).first()
    print(existing_order)
    if existing_order:
        return True
    return False
    
@api_view(['POST'])
def create_order(request):
    # print('request data:', request.data)
    user = int(request.data.get('user'))
    flight = int(request.data.get('flight'))
    # 一定要注意整形数字
    request.data['user'] = user
    request.data['flight'] = flight
    
    flight = Flight.objects.select_related('aircraft').filter(id=flight).first()
    if not flight:
        return Response({'code': 1, 'msg': '航班不存在'}, status=status.HTTP_400_BAD_REQUEST)

    seat_id = request.data.get('seat')
    if not seat_id:
        return Response({'code': 1, 'msg': '未指定座位'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        seat = Seat.objects.get(id=seat_id, flight=flight)
        if seat.status != 'booked':
            return Response({'code': 1, 'msg': '座位未预订，请先完成预订'}, status=status.HTTP_400_BAD_REQUEST)
    except Seat.DoesNotExist:
        return Response({'code': 1, 'msg': '座位不存在或不属于当前航班'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = OrderCreateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'code': 0, 'msg': '订单创建成功'}, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def cancel_order(request, order_id):
    order = Order.objects.filter(order_id=order_id).first()
    if not order:
        return Response({'code': 1, 'msg': '订单不存在'}, status=status.HTTP_400_BAD_REQUEST)
    order.cancel()
    return Response({'code': 0, 'msg': '订单已取消'},status=status.HTTP_200_OK)
 