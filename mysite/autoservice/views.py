from django.shortcuts import render, get_object_or_404
from .models import (Service,
                     Order,
                     Vehicle)
from django.views import generic
from django.core.paginator import Paginator

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
    paginator = Paginator(Vehicle.objects.all(), 2)
    page_number = request.GET.get('page')
    vehicles = paginator.get_page(page_number)
    return render(request, 'vehicles.html', context={"vehicles": vehicles})


def vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'vehicle.html', context={"vehicle": vehicle})


class OrderListView(generic.ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'orders.html'
    paginate_by = 2

class OrderDetailView(generic.DetailView):
    model = Order
    context_object_name = 'order'
    template_name = 'order.html'
