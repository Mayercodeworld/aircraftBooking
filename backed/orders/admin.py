# orders/admin.py
from django.contrib import admin
from .models import Order, TicketNotification, Invoice


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'name', 'passportNo','date', 'flight', 'seat')
    list_filter = ('passportNo', 'name', 'flight')
    search_fields = ('passportNo', 'date', 'flight')

admin.site.register(TicketNotification)
admin.site.register(Invoice)
