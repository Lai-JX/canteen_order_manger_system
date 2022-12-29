from django.urls import path
from .views import show_canteen, show_store, show_dish, update_store, del_store, add_store

urlpatterns = [
    path('', show_canteen, name='canteen'),
    path('store/', show_store, name='store'),
    path('dish/', show_dish),
    path('update_store/<slug:store_id>', update_store, name = 'update_store'),
    path('del_store/<slug:store_id>', del_store, name = 'del_store'),
    path('add_store/', add_store, name = 'add_store'),
]