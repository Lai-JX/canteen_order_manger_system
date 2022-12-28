from django.contrib import admin

# Register your models here.
from user.models import Address, CustomerInfo

admin.site.register(Address)
admin.site.register(CustomerInfo)