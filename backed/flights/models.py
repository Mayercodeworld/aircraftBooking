from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_no = models.CharField(max_length=10, unique=True)
    departure_city = models.CharField(max_length=100)
    arrival_city = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    remaining_tickets = models.IntegerField()
    airline = models.CharField(max_length=100, default='UnKnown') 

    def __str__(self):
        return f'航班 {self.flight_no}:  {self.departure_city} 到 {self.arrival_city}'

    class Meta:
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'