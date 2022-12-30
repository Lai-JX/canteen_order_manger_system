import os

import requests
from django.contrib import messages
from django.shortcuts import render, redirect

from order.models import Indent, IndentInventory
from user.models import Address
from .forms import storeForm, dishForm
from .models import Canteen, Store, Dish
from user.models import Manager


# Create your views here.

# 新增商铺
# def is_add_store(request):
#     if request.POST.get('add_store') is not None:
#         print('add_store')
#         return True
#     return False
# 整理菜品列表并输出
def get_order_dish_list(order_id):
    dish_list_ = None
    # 获取订单明细
    if order_id is not None:
        order = Indent.objects.get(indent_id=order_id)
        dish_list_ = IndentInventory.objects.filter(indent=order.indent_id)
        # 整理数据，方便输出
        dish_list = []
        for i in dish_list_:
            dish = {}
            dish['dish_price'] = i.dish.dish_price
            dish['dish_name'] = i.dish.dish_name
            dish['dish_num'] = i.dish_num
            dish_list.append(dish)
        return dish_list
    return None

# 整理菜品列表并输出
def get_dish_list(order_id):
    dish_list_ =None
    # 获取订单明细
    if order_id is not None:
        order = Indent.objects.get(indent_id=order_id)
        dish_list_ = IndentInventory.objects.filter(indent=order.indent_id)
    # 整理数据，方便输出
    dish_list = []
    for i in Dish.objects.all():
        dish = {}
        dish['dish_price'] = i.dish_price
        dish['dish_describe'] = i.dish_describe
        dish['dish_id'] = i.dish_id
        dish['store_id'] = i.store_id.store_id
        dish['dish_name'] = i.dish_name
        dish['dish_image'] = i.dish_image
        dish['get_order_url_add'] = i.get_order_url_add()
        dish['get_order_url_sub'] = i.get_order_url_sub()
        dish['dish_num'] = 0
        if dish_list_ is not None:
            try:
                cur_dish = dish_list_.get(dish_id=i.dish_id)
                dish['dish_num'] = cur_dish.dish_num
            except:
                dish['dish_num'] = 0
        dish_list.append(dish)
    return dish_list


def show_canteen(request):
    # 是否更改状态（只有食堂管理员能更改）
    canteen_id = request.POST.get('canteen_id')     # 选中的食堂
    # 是否更改状态
    if canteen_id is not None:
        user = Manager.objects.get(manager_label=1, manager_id=request.session.get('user_id'))
        # 用户管理的食堂
        canteen = user.manager_canteen
        # 用户只能修改自己管理的食堂
        if int(canteen_id) == canteen.canteen_id:
            pre_state = canteen.canteen_state   # 之前状态
            canteen.canteen_state = '营业中' if pre_state == '休息中' else '休息中'
            canteen.save()
        else:
            messages.warning(request,'管理员只能修改自己管理的食堂！')

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
    order_show, order = show_cur_order(request)
    # if is_add_store(request):
    #     print('is add')
    #     return redirect('/add_store/')
    context = {
        'canteen_list': Canteen.objects.all(),
        'store_list': Store.objects.all(),
        'order_show':order_show,
        'order':order,
        'order_state':['未下单','已下单','已发货','已送达','已评价'],
        'dish_list_':get_order_dish_list(request.session.get('order_id'))
    }
    # print(Canteen.objects.all()[0].canteen_id)
    # print(Store.objects.all()[0].canteen_id)
    # print(type(Canteen.objects.all()[0].canteen_id))
    # print(type(Store.objects.all()[0].canteen_id.canteen_id))
    # print(Canteen.objects.all()[0].canteen_id==Store.objects.all()[0].canteen_id)
    # print(Store.objects.all()[0].store_image)
    return render(request, 'canteen/store_list.html', context)

def show_dish(request):
    # dish_list = Dish.objects.all()
    # dishes = []
    # for item in dish_list:
    #     dishes.append()
    order_show, order = show_cur_order(request)
    context = {
        'store_list': Store.objects.all(),
        'dish_list': get_dish_list(request.session.get('order_id')),
        'order_show':order_show,
        'order':order,
        'order_state':['未下单','已下单','已发货','已送达','已评价'],
        'dish_list_':get_order_dish_list(request.session.get('order_id')),
    }

    # print(Dish.objects.all()[0].dish_id)
    # print(Store.objects.all()[0].dish_id)
    # print(dish_list_[0]['dish_id'])
    return render(request,'canteen/dish_list.html', context)

def show_cur_order(request):
    order_show = False
    order = None
    order_id = request.session.get('order_id')
    # dish_list = None
    # 每个菜品数量
    # if order_id is not None:
    #     order = Indent.objects.get(indent_id=order_id)
    #     dish_list = IndentInventory.objects.filter(indent=order.indent_id)

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
        # for i in dish_list:
        #     i.dish_num = 0
        #     i.save()
        order.indent_state='已下单'
        order.save()
        del request.session['order_id']
        messages.success(request,'下单成功！')
        return False, None

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
            return False, None
        if not request.session.get('order_id', None):
            messages.warning(request, "暂无订单~")
            return False, None
        order_id = request.session['order_id']
        order = Indent.objects.get(indent_id=order_id)
    return order_show, order

def del_store(request, store_id):
    print('del store:store_id:',store_id)
    Store.objects.get(store_id=store_id).delete()
    return redirect('/store/')

def update_store(request, store_id):
    print('update store:store_id:', store_id)
    print('user_id:',(request.session['user_id']))
    # 如果是商家，则只能修改自己的
    if request.session['label'] == 1:
        try:
            user = Manager.objects.get(manager_label=0,manager_id=request.session['user_id'])
            # print(type(user.manager_store.store_id))
            if user.manager_store.store_id != int(store_id):
                messages.warning(request, '商铺只允许被所属商家或食堂管理员修改！')
                return redirect('/store/')
        except:
            messages.warning(request, '商铺只允许被所属商家或食堂管理员修改！')
            return redirect('/store/')
    request.session['update_store_id'] = store_id
    return redirect('/add_store/')

def add_store(request):
    print('add_store')
    print(request.method)
    update_store_id = request.session.get('update_store_id')

    print('update_store_id:',update_store_id)
    # 判断是更新还是新增
    if update_store_id is not None:
        store = Store.objects.get(store_id=update_store_id)
        store_form = storeForm({
            'store_name':store.store_name,
            'store_des' :store.store_describe,
            'store_state' :store.store_state,
            'store_image' : store.store_image,
            # 'manager_name' = None,
        })
    else:
        store_form = storeForm()
    if request.method == "POST":
        store_form = storeForm(request.POST, request.FILES)    # 将表单用一个类封装起来 # request.POST返回一个字典，get是字典的内置方法
        message = '请检查填写内容！'
        print('store_form valid',store_form.is_valid())
        if store_form.is_valid():
            try:
                # 设置管理商铺的商家

                business = Manager.objects.get(manager_label=0,manager_name=store_form.cleaned_data.get('manager_name'))

            except:
                messages.warning(request,"商家不存在！")
                return render(request, 'canteen/add_store.html', locals())
            # 商铺属性
            name = store_form.cleaned_data.get('store_name')
            des = store_form.cleaned_data.get('store_des')
            image = store_form.cleaned_data.get('store_image')
            state = store_form.cleaned_data.get('store_state')
            # 创建商铺
            print(request.session['user_id'])
            # 是否为新建商铺
            if update_store_id is None:
                store = Store(canteen_id=Manager.objects.get(manager_label=1, manager_id=request.session['user_id']).manager_canteen,)

            store.store_name=name
            store.store_image=image
            store.store_state=state
            store.store_describe=des
            store.save()
            # 商铺与商家绑定
            if update_store_id is None:
                business.manager_store = store
                business.save()
            else:
                del request.session['update_store_id']

            return redirect('/store/')
    return render(request,'canteen/add_store.html',locals())

# 添加或修改菜品，store为要菜品对应的商铺
def add_dish(request, store_id):
    print('add_dish')
    print(request.method)
    update_dish_id = request.session.get('update_dish_id')

    print('update_dish_id:',update_dish_id)
    # 判断是更新还是新增
    if update_dish_id is not None:
        dish = Dish.objects.get(dish_id=update_dish_id)
        dish_form = dishForm({
            'dish_name':dish.dish_name,
            'dish_des' :dish.dish_describe,
            'dish_state' :dish.dish_state,
            'dish_image' : dish.dish_image,
            'dish_price' : dish.dish_price,
        })
    else:
        dish_form = dishForm()
    if request.method == "POST":
        dish_form = dishForm(request.POST, request.FILES)    # 将表单用一个类封装起来 # request.POST返回一个字典，get是字典的内置方法
        message = '请检查填写内容！'
        print('dish_form valid',dish_form.is_valid())
        if dish_form.is_valid():
            # 对应商铺
            print('store_id:',store_id)
            store = Store.objects.get(store_id=store_id)

            # 菜品属性
            name = dish_form.cleaned_data.get('dish_name')
            des = dish_form.cleaned_data.get('dish_des')
            image = dish_form.cleaned_data.get('dish_image')
            state = dish_form.cleaned_data.get('dish_state')
            price = dish_form.cleaned_data.get('dish_price')
            # 创建商铺
            print(request.session['user_id'])
            print('update_dish_id:',update_dish_id)
            # 是否为新建商铺
            if update_dish_id is None:
                dish = Dish(store_id=Store.objects.get(store_id=store_id))

            dish.dish_name=name
            dish.dish_image=image
            dish.dish_state=state
            dish.dish_describe=des
            dish.dish_price = price
            dish.save()
            if update_dish_id is not None:
                del request.session['update_dish_id']

            return redirect('/dish/')

    return render(request,'canteen/add_dish.html',locals())

def del_dish(request, dish_id):
    print('del dish:dish_id:',dish_id)
    dish = Dish.objects.get(dish_id=dish_id)
    # 如果是商家，则只能删除自己的
    if request.session['label'] == 1:
        try:
            user = Manager.objects.get(manager_label=0, manager_id=request.session['user_id'])
            if user.manager_store.store_id != dish.store_id.store_id:
                messages.warning(request, '菜品只允许被所属商家或食堂管理员删除！')
                return redirect('/dish/')
        except:
            messages.warning(request, '商铺只允许被所属商家或食堂管理员删除！')
            return redirect('/dish/')
    dish.delete()
    return redirect('/dish/')

def update_dish(request, dish_id):
    print('update dish:dish_id:', dish_id)
    print('user_id:',(request.session['user_id']))
    dish = Dish.objects.get(dish_id=dish_id)
    # 如果是商家，则只能修改自己的
    if request.session['label'] == 1:
        try:
            user = Manager.objects.get(manager_label=0,manager_id=request.session['user_id'])
            if user.manager_store.store_id != dish.store_id.store_id:
                messages.warning(request, '菜品只允许被所属商家或食堂管理员修改！')
                return redirect('/dish/')
        except:
            messages.warning(request, '菜品只允许被所属商家或食堂管理员修改！')
            return redirect('/dish/')
    request.session['update_dish_id'] = dish_id
    return redirect('/add_dish/{}'.format(dish.store_id.store_id))