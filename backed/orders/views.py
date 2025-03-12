from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import OrderSerializer
from .models import Order,UserInfo
from flights.models import Flight, Seat  

@api_view(['GET'])
# 获得用户表单
def get_user_tickets(request, user_id):
    # 根据 user_id 查找所有匹配的 Order 行
    orders = Order.objects.filter(user_id=user_id)

    # 使用 OrderSerializer 序列化订单数据
    serializer = OrderSerializer(orders, many=True)

    # 检查是否有订单
    if not serializer.data:
        return Response({'code': 1, 'msg': '该用户没有订单'}, status=400)

    # 返回结果
    return Response(serializer.data)

@api_view(['POST'])
#创建订单
def create_order(request):
    user_id = request.data.get('user')
    flight_id = request.data.get('flight')
    passport_id = request.data.get('passportNo')
    seat_letter = request.data.get('seat_letter')  # 获取用户选择的座位字母

    # 检查是否存在具有相同 user_id, flight_id, passport_id 的订单
    existing_order = Order.objects.filter(user=user_id, flight=flight_id, passportNo=passport_id).first()
    if existing_order:
        return Response({'code': 1, 'msg': '该用户已经存在相同的订单'}, status=status.HTTP_400_BAD_REQUEST)

    # 获取航班和可用座位
    flight = Flight.objects.filter(id=flight_id).first()
    if not flight:
        return Response({'code': 1, 'msg': '航班不存在'}, status=status.HTTP_400_BAD_REQUEST)

    available_seats = flight.seats.filter(status='available')

    if not available_seats.exists():
        return Response({'code': 1, 'msg': '没有可用的座位'}, status=status.HTTP_400_BAD_REQUEST)

    # 选择座位
    if seat_letter:
        seat = Seat.get_sequential_seat(flight, seat_letter)
        if not seat:
            return Response({'code': 1, 'msg': '选择的座位不可用'}, status=status.HTTP_400_BAD_REQUEST)
    else:
        # 如果没有提供座位字母，按顺序分配第一个可用座位
        seat = available_seats.order_by('seat_number').first()
        if not seat:
            return Response({'code': 1, 'msg': '没有可用的座位'}, status=status.HTTP_400_BAD_REQUEST)
        seat.status = 'booked'
        seat.save()

    # 更新座位状态
    seat.status = 'booked'
    seat.save()

    # 创建订单
    request.data['seat'] = seat.id  # 将座位ID添加到请求数据中
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # print('Validation errors:', serializer.errors)  # 打印验证错误信息
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 # @api_view(['POST'])
 # # 取票通知
 # def notice_ticket(request, user_id):
 #     try:
 #         user = UserInfo.objects.get(id=user_id)
 #     except UserInfo.DoesNotExist:
 #         return Response({'code': 1, 'msg': '用户不存在'}, status=status.HTTP_400_BAD_REQUEST)
