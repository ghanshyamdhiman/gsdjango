from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the bookings index.")

def booking(request, booking_venue):
    return HttpResponse("You're looking at booking venue %s." % booking_venue)


# Create your views here.
