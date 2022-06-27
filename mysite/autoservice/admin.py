import site

from django.contrib import admin

# Register your models here.
from .models import (Vehicle,
                     VehicleModel,
                     Service,
                     Order,
                     OrderLine)


class OrderLinesInline(admin.TabularInline):
    model = OrderLine
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['vehicle', 'due_date', 'tsum']
    inlines = [OrderLinesInline]


class VehicleAdmin(admin.ModelAdmin):
    list_display = ['year', 'owner_name', 'vehicle_model', 'license_plate', 'vin_code', 'engine']
    list_filter = ('owner_name', 'vehicle_model')
    search_fields = ['license_plate', 'vin_code', 'vehicle_model__make', 'vehicle_model__model']

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


admin.site.register(Vehicle, VehicleAdmin)
admin.site.register(VehicleModel)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderLine)
