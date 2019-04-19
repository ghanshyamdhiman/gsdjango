from django.db import models


class BookingDetails(models.Model):
    booking_venue = models.CharField(max_length=200)
    booking_date = models.DateTimeField('Booking Date')


class ClientDetails(models.Model):
    client_name = models.CharField(max_length=200)
    advance_paid = models.IntegerField(default=0)
# Create your models here.
