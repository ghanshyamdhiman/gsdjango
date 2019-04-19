from django.db import models


class BookingDetails(models.Model):
    booking_venue = models.CharField(max_length=200)
    booking_date = models.DateTimeField('Booking Date')
    
    def __str__(self):
        return self.booking_venue

class ClientDetails(models.Model):
    client_name = models.CharField(max_length=200)
    advance_paid = models.IntegerField(default=0)
    
    def __str__(self):
        return self.client_name
# Create your models here.
