from django.urls import path
from .views import show_canteen, show_store, show_dish

urlpatterns = [
    path('', show_canteen, name='canteen'),
    path('store/', show_store, name='store'),
    path('dish/', show_dish),
]