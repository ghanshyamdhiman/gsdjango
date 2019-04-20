from django.http import HttpResponse
from django.template import loader

from .models import BookingDetails



def index(request):
    latest_booking_list = BookingDetails.objects.order_by('booking_date')[:5]
    template = loader.get_template('bookings/index.html')
    context = {
        'latest_booking_list': latest_booking_list,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
