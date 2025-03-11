# orders/admin.py
from django.contrib import admin
from .models import Order, TicketNotification, Invoice

admin.site.register(Order)
admin.site.register(TicketNotification)
admin.site.register(Invoice)
