from django.contrib import admin
from unfold.admin import ModelAdmin
from customers.models import Customer


@admin.register(Customer)
class CustomerAdmin(ModelAdmin):
    list_display = ['name', 'cpf', 'phone', 'created_at']
    search_fields = ['name', 'cpf', 'phone']
