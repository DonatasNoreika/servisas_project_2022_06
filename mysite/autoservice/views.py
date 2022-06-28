from django.shortcuts import render
from .models import (Service,
                     Order,
                     Vehicle)


# Create your views here.
def index(request):
    services = Service.objects.count()
    orders_done = Order.objects.filter(status__exact='d').count()
    vehicles = Vehicle.objects.count()

    my_context = {
        "my_services": services,
        "my_orders_done": orders_done,
        "my_vehicles": vehicles,
    }

    return render(request, 'index.html', context=my_context)
