from django.contrib import admin

# Register your models here.
from canteen.models import Canteen,Store,Dish,Manager

class CanteenAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['canteen_name']
    list_display = ['canteen_id', 'canteen_name', 'canteen_image', 'canteen_state']

class StoreAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['store_id', 'store_name', 'canteen_id', 'store_describe', 'store_image', 'store_state']

class DishAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['dish_id', 'dish_name', 'dish_price', 'dish_image', 'dish_describe', 'dish_state']

class ManagerAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['manager_id', 'manager_name', 'manager_phone', 'manager_pwd', 'manager_canteen', 'manager_store', 'manager_label']

admin.site.register(Canteen, CanteenAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Dish, DishAdmin)
admin.site.register(Manager, ManagerAdmin)
