import os

from django.contrib import messages
from django.shortcuts import render, redirect

from order.models import Indent, IndentInventory
from user.models import Address
from .models import Canteen, Store, Dish

# Create your views here.
def show_canteen(request):
    context = {
            'canteen_list': Canteen.objects.all(),
    }
    return render(request, 'canteen/canteen_list.html', context)

def show_store(request):
    # same_name_store = Store.objects.filter(store_name='猪肚鸡')
    # if len(same_name_store)==0:
    #     store = Store(canteen_id=Canteen.objects.get(canteen_id=9), store_name='猪肚鸡',
    #                   store_describe='猪肚包鸡，是一道广东省传统的地方名菜，属于客家菜系，又名猪肚煲鸡、凤凰投胎，流行于广东的深圳、惠州、河源、梅州等粤东一带，是广东客家地区酒席必备的餐前用汤，汤里浓中带清，有浓郁的药材味和胡椒香气。最早是客家女人坐月子时吃的一道菜肴。',
    #                   store_image='D:\hgs-3-1\DB\lab\DB4\img\猪肚鸡店铺.webp', store_state=1)
    #     store.save()
    #     dish = Dish(dish_name='柠檬猪肚鸡', dish_price=16, dish_image='../../../img/柠檬猪肚鸡.webp', dish_describe='经济实惠',
    #          dish_state=1)
    #     dish.save()
    #     store.dishes.add(dish)
    #     store.save()
    order_show, order, dish_list_ = show_cur_order(request)

    context = {
        'canteen_list': Canteen.objects.all(),
        'store_list': Store.objects.all(),
        'order_show':order_show,
        'order':order,
        'order_state':['未下单','已下单','已发货','已送达','已评价'],
        'dish_list_': dish_list_,
    }
    # print(Canteen.objects.all()[0].canteen_id)
    # print(Store.objects.all()[0].canteen_id)
    # print(type(Canteen.objects.all()[0].canteen_id))
    # print(type(Store.objects.all()[0].canteen_id.canteen_id))
    # print(Canteen.objects.all()[0].canteen_id==Store.objects.all()[0].canteen_id)
    print(Store.objects.all()[0].store_image)
    return render(request, 'canteen/store_list.html', context)

def show_dish(request):
    # dish_list = Dish.objects.all()
    # dishes = []
    # for item in dish_list:
    #     dishes.append()
    order_show, order, dish_list_ = show_cur_order(request)
    if not dish_list_:
        dish_list_ = []
        for i in Dish.objects.all():
            dish_list_.append({'dish':{'dish_id':i.dish_id}, 'dish_num':0})

    context = {
        'store_list': Store.objects.all(),
        'dish_list': Dish.objects.all(),
        'order_show':order_show,
        'order':order,
        'order_state':['未下单','已下单','已发货','已送达','已评价'],
        'dish_list_':dish_list_,
    }

    print(Dish.objects.all()[0].dish_id)
    # print(Store.objects.all()[0].dish_id)
    # print(dish_list_[0]['dish_id'])
    return render(request,'canteen/dish_list.html', context)

def show_cur_order(request):
    order_show = False
    order = None
    order_id = request.session.get('order_id')
    dish_list = None
    # 每个菜品数量
    if order_id is not None:
        order = Indent.objects.get(indent_id=order_id)
        dish_list = IndentInventory.objects.filter(indent=order.indent_id)

    # 能否获取到地址，能获取到则为下单
    order_address = request.POST.get('select_address')
    if order_address is not None:
        print('selected order_address:', order_address)
        order = Indent.objects.get(indent_id=order_id)
        order.indent_address = Address.objects.get(address_id=int(order_address))
        order.save()
        # 每道菜的数量设未0
        # for i in order.dishes.all():
        #     i.dish_order_num = 0
        #     i.save()
        for i in dish_list:
            i.dish_num = 0
            i.save()
        order.indent_state='已下单'
        order.save()
        del request.session['order_id']
        return False, None, dish_list

    show = request.POST.get('show')
    # 是否展示订单
    if show is not None:
        order_show = True
    else:
        if request.POST.get('close'):
            order_show = False
    if order_show:
        if not request.session.get('is_login', None) or request.session.get('label') != 0:
            messages.warning(request, "请先登录顾客账户~")
            return False, None,dish_list
        if not request.session.get('order_id', None):
            messages.warning(request, "暂无订单~")
            return False, None,dish_list
        order_id = request.session['order_id']
        order = Indent.objects.get(indent_id=order_id)



    return order_show, order,dish_list