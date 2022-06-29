from django.db import models


# Create your models here.

class VehicleModel(models.Model):
    make = models.CharField(verbose_name='Make', max_length=200)
    model = models.CharField(verbose_name='Model', max_length=200)

    def __str__(self):
        return f"{self.make} {self.model}"

    class Meta:
        verbose_name = 'Vehicle model'
        verbose_name_plural = 'Vehicles model'


class Vehicle(models.Model):
    year = models.IntegerField(verbose_name='Year', null=True)
    owner_name = models.CharField(verbose_name='Owner', max_length=200)
    vehicle_model = models.ForeignKey(to='VehicleModel', verbose_name="Vehicle Model", on_delete=models.SET_NULL,
                                      null=True)
    license_plate = models.CharField(verbose_name='License Plate', max_length=200)
    vin_code = models.CharField(verbose_name='VIN code', max_length=20)
    engine = models.CharField(verbose_name='Engine', max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.owner_name}: {self.vehicle_model}, {self.year}, {self.engine}, {self.license_plate}, {self.vin_code}"

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

class Service(models.Model):
    name = models.CharField(verbose_name="Name", max_length=200)
    price = models.FloatField(verbose_name="Price")

    def __str__(self):
        return f"{self.name}: {self.price}"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class Order(models.Model):
    vehicle = models.ForeignKey(to='Vehicle', verbose_name="Vehicle", on_delete=models.SET_NULL, null=True)
    due_date = models.DateTimeField(verbose_name="Due Date", null=True, blank=True)
    tsum = models.FloatField(verbose_name="TOTAL")

    ORDER_STATUS = (
        ('a', 'Accepted'),
        ('i', 'In Progress'),
        ('d', 'Done'),
        ('c', 'Cancelled'),
    )

    status = models.CharField(
        max_length=1,
        choices=ORDER_STATUS,
        blank=True,
        default='a',
        help_text='Status',
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE, null=True, related_name='lines')
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True)
    qty = models.IntegerField(verbose_name="Quantity")

    class Meta:
        verbose_name = 'Order line'
        verbose_name_plural = 'Order lines'
