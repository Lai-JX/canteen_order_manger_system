from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect

from canteen.views import show_cur_order
from user.models import CustomerInfo
from .models import Indent, IndentInventory
from canteen.models import Dish, Store


# Create your views here.

# def show_dish(request):
#     # template_name = 'dish/dish_list.html'
#     # context = {
#     #     'shop_with_dish_list': Shop.objects.all(),
#     #     'dish_list': Dish.objects.all(),
#     # }
#
#     return render(request, 'canteen/dish_list.html', locals())


def show_order(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/user/login/')

    user_id = request.session['user_id']
    order_list = Indent.objects.filter(customer_id=user_id)
    # 整理数据，方便输出
    order_list_ = []
    order = {}
    dish = {}
    for i in order_list:
        order = {}
        order['id'] = i.indent_id
        order['time'] = i.date_time
        order['canteen_name'] = i.canteen.canteen_name
        order['store_name'] = i.store.store_name
        order['phone'] = i.customer.customer_phone
        order['addr'] = i.indent_address
        order['state'] = i.indent_state
        order['price'] = i.indent_price
        order['comment'] = '未评价' if i.comment is None else i.comment
        dishes = []
        for j in i.dishes.all():
            dish = {}
            dish['name'] = j.dish_name
            dish['price'] = j.dish_price
            dish['num'] = IndentInventory.objects.get(indent=i.indent_id,dish=j.dish_id).dish_num
            dishes.append(dish)
        order['dishes'] = dishes
        order_list_.append(order)


    return render(request, 'order/my_order.html', {'order_list':order_list_})


def get_order_add(request, dish_id):
    print('get_order_add: dish_id',dish_id)
    if not request.session.get('is_login', None) or request.session.get('label') != 0:
        messages.warning(request, "若要下单，请先登录顾客账户~")
        return redirect('/user/login/')
    user_id = request.session['user_id']
    customer = CustomerInfo.objects.get(customer_id=user_id)
    # 获取要下单的菜品
    dish = get_object_or_404(Dish, dish_id=dish_id)
    # dish.dish_order_num = dish.dish_order_num+1     # 下单数加1
    # dish.save()
    # 商铺
    store = Store.objects.get(store_id = dish.store_id.store_id)

    # 添加菜品到订单（订单不存在则创建）
    try:
        order_id = request.session['order_id']
        order = Indent.objects.get(indent_id=order_id)
        if dish.store_id.store_id != order.store.store_id or dish.store_id.canteen_id.canteen_id != order.canteen.canteen_id:
            messages.warning(request, "请在同一商家下单~")
            return redirect("/dish/#" + dish_id)
        order.dishes.add(dish)

    except:
        # 将下单数量均改为0，在下单完毕时该比较合适
        # for dish1 in Dish.objects.all():
        #     dish1.dish_order_num = 0
        #     dish1.save()
        # dish.dish_order_num = 1
        # dish.save()
        
        order = Indent(customer = customer, store=dish.store_id, canteen=store.canteen_id, indent_state='未下单')
        order.indent_address = customer.addresses.first()
        order.save()
        order.dishes.add(dish)
        request.session['order_id'] = order.indent_id
    dish_ = IndentInventory.objects.get(indent=request.session['order_id'], dish=dish_id)
    dish_.dish_num = dish_.dish_num + 1
    dish_.save()
    # 总价
    order.indent_price = order.indent_price + dish.dish_price
    order.save()
    return redirect("/dish/#"+dish_id)



    # user_id = request.session['user_id']   # 可能需要先把登录做了

    # try:
    #     user = CustomerInfo.objects.filter(customer_id=user_id).first()
    #     order = Indent.objects.create(customer=user)
    #     order.indent_price = order.dish.dish_price
    #     order.indent_status = 0
    #     order.save()
    #     messages.success(request, '下单成功，订单号为 (Order ID-{}). 请支付 {} 元'.format(order.order_id, order.order_price))
    #     return redirect("order:show_order")
    #
    # except ObjectDoesNotExist:
    #     messages.warning(request, "你还没有订单哦~")
    #     return redirect("order:show_order")

def get_order_sub(request, dish_id):

    print('get_order_sub: dish_id:', dish_id)
    order_id = request.session['order_id']
    if not request.session.get('is_login', None) or request.session.get('label') != 0:
        messages.warning(request, "若要下单，请先登录顾客账户~")
        return redirect('/user/login/')

    # 获取要减去的菜品 及对应订单项
    dish = get_object_or_404(Dish, dish_id=dish_id)
    try:
        dish_ = IndentInventory.objects.get(dish=dish_id, indent=order_id)
    except:
        messages.warning(request, "该菜品未下单~")
        return redirect("/dish/#" + dish_id)
    dish_.dish_num = dish_.dish_num - 1  # 下单数加1
    dish_.save()

    # 修改订单
    try:
        order = Indent.objects.get(indent_id=order_id)
        if dish_.dish_num == 0:
            order.dishes.remove(dish)

    except:
        messages.warning(request, "没有订单~")
        return redirect("/dish/#" + dish_id)

    # 总价
    order.indent_price = order.indent_price - dish.dish_price
    order.save()

    return redirect("/dish/#"+dish_id)

def del_order(request, order_id):
    print('delete order')
    try:
        order = Indent.objects.get(indent_id=order_id)
        dish_list = IndentInventory.objects.filter(indent=order.indent_id)
        # for i in order.dishes.all():
        #     i.dish_order_num = 0;
        #     i.save()
        for i in dish_list:
            i.dish_num = 0;
            i.save()
        order.delete()
        del request.session['order_id']
    except:
        messages.warning(request, "订单删除失败~")
    return redirect("/dish/")