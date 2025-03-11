from django.contrib import admin
from .models import Aircraft, Flight, Seat
# Register your models here.
admin.site.register(Aircraft)
admin.site.register(Flight)
# admin.site.register(Seat)