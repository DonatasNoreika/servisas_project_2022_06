import site

from django.contrib import admin

# Register your models here.
from .models import (Vehicle,
                     VehicleModel,
                     Service,
                     Order,
                     OrderLine)

admin.site.register(Vehicle)
admin.site.register(VehicleModel)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(OrderLine)
