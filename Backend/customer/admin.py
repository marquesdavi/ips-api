from django.contrib import admin
from customer.models import Customer

# Register your models here.
"""class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','cpf', 'rg', 'phone_number')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'cpf', 'rg', 'email')
    list_per_page = 25
    ordering = ('name',)"""


admin.site.register(Customer)