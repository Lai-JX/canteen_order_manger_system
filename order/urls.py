from django.urls import path
from .views import show_order, get_order_sub, get_order_add,del_order


app_name = 'order'
urlpatterns = [
    # path('dish/', show_dish),
    path('order/', show_order, name='show_order'),
    path('get_order_add/<slug:dish_id>', get_order_add, name='get_order_add'),
    path('get_order_sub/<slug:dish_id>', get_order_sub, name='get_order_sub'),
    path('del_order/<slug:order_id>', del_order, name='del_order'),
]