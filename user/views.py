import hashlib

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import redirect

from canteen.models import Manager
from . import models
from . import forms

# Create your views here.
# Create your views here.

# 对密码进行加密
from .forms import AddressForm
from .models import CustomerInfo, Address

def getAddress(building,floor,dormitory,address_des):
    try:
        addr = Address.objects.get(building=building,floor=floor,
                                    dormitory_num=dormitory, address_describe=address_des)
        return addr
    except:
        addr = Address(building=building,floor=floor,
                       dormitory_num=dormitory, address_describe=address_des)
        addr.save()
        return addr

def hash_code(s, salt='mysite'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()
# def create_admin_user():
#     from django.contrib.auth.models import User, Group
#     user = User.objects.create_user(username='John', password='123456')
#     user.save()
#     group = Group.objects.get(name='manager')
#     group.user_set.add(user)


def index(request):
    # create_admin_user()
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'user/index.html')


def login(request):
    if request.session.get('is_login', None):  # 不允许重复登录
        messages.warning(request,'若要重新登录，请先退出当前账号！')
        return redirect('/user/index/')
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)    # 将表单用一个类封装起来 # request.POST返回一个字典，get是字典的内置方法
        message = '请检查填写内容！'
        print('login form valid',login_form.is_valid())
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            label = login_form.cleaned_data.get('label')
            label = int(label)
            print('Login:',username, password,label)
            # print(CustomerInfo.objects.all()[0])
            if username.strip() and password:  # 确保用户名和密码都不为空
                # 用户名字符合法性验证
                # 密码长度验证
                # 更多的其它验证.....

                try:
                    # 顾客
                    if label == 0:
                        user = CustomerInfo.objects.get(customer_name=username)
                        user_id = user.customer_id
                        pwd = user.customer_pwd
                    # 商家/食堂管理员
                    else:
                        user = Manager.objects.get(manager_name=username,manager_label=label-1)
                        user_id = user.manager_id
                        pwd = user.manager_pwd
                except:
                    message = '用户不存在！'
                    return render(request, 'user/login.html', locals()) # locals() 以字典形式返回当前所有的本地变量


                if pwd == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user_id
                    # request.session['user_phone'] = user.customer_phone
                    request.session['label'] = label
                    if label==0:
                        # messages.success(request, '顾客: {}登录成功！'.format(user.customer_name))
                        request.session['user_name'] = user.customer_name
                    elif label==1:
                        messages.success(request, '{}商家: {}登录成功！'.format(user.manager_store,user.manager_name))
                        request.session['user_name'] = user.manager_name
                    elif label==2:
                        messages.success(request, '{}管理员: {}登录成功！'.format(user.manager_canteen,user.manager_name))
                        request.session['user_name'] = user.manager_name
                    return redirect('/user/index/')
                else:
                    message = '密码不正确！'
                    return render(request, 'user/login.html', locals())
        else:
            return render(request, 'user/login.html',locals())
    else:
        login_form = forms.LoginForm()    # 空表单
        return render(request, 'user/login.html',locals())

def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    print('register',request.method)
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        # address_form = forms.AddressForm(request.POST)
        message = "请检查填写的内容！"
        print('register form valid', register_form.is_valid())
        if register_form.is_valid():
            username = register_form.cleaned_data.get('username')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')


            if password1 != password2:
                message = '两次输入的密码不同！'
                return render(request, 'user/register.html', locals())
            else:
                same_name_user = CustomerInfo.objects.filter(customer_name=username)
                if same_name_user:
                    message = '用户名已经存在'
                    return render(request, 'user/register.html', locals())
                # same_email_user = models.User.objects.filter(email=email)
                # if same_email_user:
                #     message = '该邮箱已经被注册了！'
                #     return render(request, 'user/register.html', locals())
                phone = register_form.cleaned_data.get('phone')
                sex = register_form.cleaned_data.get('sex')
                address_p1 = register_form.cleaned_data.get('building')
                address_p2 = register_form.cleaned_data.get('floor')
                address_p3 = register_form.cleaned_data.get('dormitory_num')
                address_des = register_form.cleaned_data.get('address_describe')

                customer = CustomerInfo(customer_sex = sex, customer_name = username,
                                        customer_pwd = hash_code(password1), customer_phone = phone)
                customer.save()
                addr = getAddress(address_p1, address_p2, address_p3, address_des)
                # addr = Address(building=address_p1, floor=address_p2, dormitory_num=address_p3,address_describe=address_des)
                # addr.save()
                customer.addresses.add(addr)
                # customer.addresses.first()
                customer.save()
                return redirect('/user/login/')
        else:
            return render(request, 'user/register.html', locals())
    else:
        register_form = forms.RegisterForm()
        # address_form = forms.AddressForm()
        return render(request, 'user/register.html',locals())

# 退出登录时返回登录界面
def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就未登录，也就没有登出一说
        return redirect("/login/")
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']
    return redirect("/user/login/")

def information(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/user/login/')

    address_form = AddressForm()
    user_id = request.session['user_id']
    customer = CustomerInfo.objects.filter(customer_id=user_id).first()

    # if customer.address:
    #     # print("已经填过地址")
    #     return redirect("customer:show_info")
    address_form = AddressForm()
    if request.method == "POST":
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            # 各地址属性
            building = address_form.cleaned_data['building']
            floor = address_form.cleaned_data['floor']
            dormitory_num = address_form.cleaned_data['dormitory_num']
            address_des = address_form.cleaned_data['address_describe']
            # 获取地址记录
            addr = getAddress(building,floor,dormitory_num,address_des)
            # 添加地址
            customer.addresses.add(addr)
            customer.save()
            messages.success(request, '个人地址添加成功！')
            return render(request, 'user/show_info.html', locals())
            # try:
            #     # 匹配当前用户号
            #     # cus_info = Address.objects.create(district=new_district, building=new_building, room=new_room)
            #     # cus_info.save()
            #     # customer = CustomerInfo.objects.filter(customer_id=user_id).first()
            #     customer.addresses.get(address_id=addr.address_id)
            #     print('地址已存在，直接添加')
            #     customer.addresses.add(addr)
            #     customer.save()
            #     return render(request, 'user/show_info.html', locals())
            #
            # except:
            #     customer.addresses.add(addr)
            #     customer.save()
            #     # request.session['district'] = new_district
            #     # request.session['building'] = new_building
            #     # request.session['room'] = new_room
            #     messages.success(request, '个人地址添加成功！')
            #     return render(request, 'user/show_info.html', locals())
    return render(request, 'user/information.html', locals())

def show_info(request):
    return render(request, 'user/show_info.html', locals())
