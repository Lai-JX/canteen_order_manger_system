from django.urls import path
from .views import show_canteen, show_store, show_dish, update_store, del_store, add_store, add_dish, update_dish, \
    del_dish

urlpatterns = [
    path('', show_canteen, name='canteen'),
    path('store/', show_store, name='store'),
    path('dish/', show_dish),
    path('update_store/<slug:store_id>', update_store, name = 'update_store'),
    path('del_store/<slug:store_id>', del_store, name = 'del_store'),
    path('add_store/', add_store, name = 'add_store'),

    path('update_dish/<slug:dish_id>', update_dish, name = 'update_dish'),
    path('del_dish/<slug:dish_id>', del_dish, name = 'del_dish'),
    path('add_dish/<slug:store_id>', add_dish, name = 'add_dish'),
]