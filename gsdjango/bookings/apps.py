from django.apps import AppConfig
from django.contrib import admin
from .models import BookingDetails

admin.site.register(BookingDetails)

class BookingsConfig(AppConfig):
    name = 'bookings'

    


