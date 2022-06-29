from django.shortcuts import render, get_object_or_404
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


def vehicles(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles.html', context={"vehicles": vehicles})


def vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicle.html', context={"vehicle": vehicle})