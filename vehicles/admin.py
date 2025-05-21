from django.contrib import admin
from unfold.admin import ModelAdmin
from vehicles.models import VehicleType, Vehicle


@admin.register(VehicleType)
class VehicleTypeAdmin(ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(Vehicle)
class VehicleAdmin(ModelAdmin):
    list_display = ['license_plate', 'brand', 'model', 'color']
    search_fields = ['license_plate', 'model']
    list_filter = ['vehicle_type']
