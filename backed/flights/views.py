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
        # if 'depart' in query_params:
        #     flights = flights.filter(departure_time=query_params['depart'])
        # 可以根据需要添加更多过滤条件
    
    serializer = FlightSerializer(flights, many=True)
    return Response(serializer.data)