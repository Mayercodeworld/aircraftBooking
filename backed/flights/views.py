from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Flight
from .forms import FlightForm
from .serializers import FlightSerializer
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
        # if 'depart' in query_params:
        #     flights = flights.filter(departure_time=query_params['depart'])
        
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)