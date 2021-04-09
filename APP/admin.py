from django.contrib import admin

# Register your models here.

from .models import Customer, Map

admin.site.register(Customer)
admin.site.register(Map)
