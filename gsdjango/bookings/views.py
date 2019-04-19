from django.http import HttpResponse
from .models import BookingDetails


def index(request):
    latest_booking_list = BookingDetails.objects.order_by('booking_date')[:5]
    output = ', '.join([q.booking_venue for q in latest_booking_list])
    return HttpResponse(output)

def booking(request, booking_venue):
    return HttpResponse("You're looking at booking venue %s." % booking_venue)


# Create your views here.
