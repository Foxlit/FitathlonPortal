from django.views.generic import ListView
from .models import *


class BookingList(ListView):
    model = Booking
    template_name = 'Booking.html'
    context_object_name = 'booking'
