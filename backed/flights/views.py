from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Flight
from .models import Seat
from .forms import FlightForm
from .serializers import FlightSerializer
from .serializers import SeatSerializer
from datetime import datetime
# Create your views here.

@api_view(['POST'])
def update_flights(request):
    flight_form = FlightForm(request.POST)
    if flight_form.is_valid():
        flight = flight_form.save()
        serializer = FlightSerializer(flight)
        return Response(serializer.data)
@api_view(['GET'])
def get_flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    serializer = FlightSerializer(flight)
    return Response(serializer.data)    

@api_view(['GET'])
def get_seats(request, flight_id):
    flight = get_object_or_404(Flight, id=flight_id)
    seats = flight.seats.all()
    serializer = SeatSerializer(seats, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def book_seat(request, flight_id):   
    data = request.data
    seat_number = data.get('seat_number')

    flight = get_object_or_404(Flight, id=flight_id)

    # 防止超卖
    if flight.remaining_seats <= 0:
        return Response({'error': '该航班已无剩余座位'}, status=status.HTTP_400_BAD_REQUEST)

    seat, created = Seat.objects.get_or_create(
        flight=flight,
        seat_number=seat_number,
        defaults={'status': 'booked'}
    )

    if not created:
        if seat.status == 'booked':
            return Response({'error': '该座位已被预订'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            seat.status = 'booked'
            seat.save()

    serializer = SeatSerializer(seat)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def cancel_seat(request, flight_id):
    data = request.data
    seat_number = data.get('seat_number')

    flight = get_object_or_404(Flight, id=flight_id)

    seat, created = Seat.objects.get_or_create(
        flight=flight,
        seat_number=seat_number,
        defaults={'status': 'booked'}
    )

    if created:
        # 新建的座位无法取消（因为不是预订状态）
        return Response({'error': '该座位未被预订'}, status=status.HTTP_400_BAD_REQUEST)

    if seat.status != 'booked':
        return Response({'error': '该座位未被预订，无法取消'}, status=status.HTTP_400_BAD_REQUEST)

    # 将座位设为可用
    seat.status = 'available'
    seat.save()

    return Response({'message': '座位取消成功'}, status=status.HTTP_200_OK)

@api_view(['GET', 'POST'])    
def get_flights(request):
    if request.method == 'GET':
        flights = Flight.objects.all()
    elif request.method == 'POST':
        query_params = request.data
        flights = Flight.objects.all()
        if 'from' in query_params:
            flights = flights.filter(departure_city=query_params['from'])
        if 'to' in query_params:
            flights = flights.filter(arrival_city=query_params['to'])
        # 可以根据需要添加更多过滤条件
        if 'depart' in query_params:
            try:
                depart_date = datetime.strptime(query_params['depart'], '%Y-%m-%d')
                flights = flights.filter(
                    departure_time__year=depart_date.year,
                    departure_time__month=depart_date.month,
                    departure_time__day=depart_date.day
                )
            except ValueError:
                return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)
        
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)