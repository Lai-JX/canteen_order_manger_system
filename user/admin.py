from django.contrib import admin

# Register your models here.
from user.models import Address, CustomerInfo, Manager


class ManagerAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['manager_id', 'manager_name', 'manager_phone', 'manager_pwd', 'manager_canteen', 'manager_store', 'manager_label']
class AddressAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['address_id', 'building', 'floor', 'dormitory_num', 'address_describe', 'phone']
class CustomerInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['customer_id', 'customer_name', 'customer_phone', 'customer_pwd', 'customer_sex', 'addresses']


admin.site.register(Address)
admin.site.register(CustomerInfo)
admin.site.register(Manager, ManagerAdmin)