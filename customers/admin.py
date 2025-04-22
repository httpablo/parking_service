from django.contrib import admin
from customers.models import Customers


@admin.register(Customers)
class CustomersAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'phone', 'created_at']
    search_fields = ['name', 'cpf', 'phone']
