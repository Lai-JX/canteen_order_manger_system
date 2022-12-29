# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse


class Canteen(models.Model):
    canteen_id = models.AutoField(primary_key=True, verbose_name='食堂编号')
    # manager = models.ForeignKey('Manager', models.SET_NULL, blank=True, null=True, verbose_name='食堂管理员')
    canteen_name = models.CharField(max_length=20, verbose_name='食堂名称')
    canteen_image = models.ImageField(upload_to='images/canteen',blank=True, null=True, verbose_name='食堂照片')
    canteen_state = models.CharField(max_length=20, choices=[("营业中", "营业中"), ("休息中","休息中")], verbose_name='食堂状态')

    class Meta:
        ordering = ['canteen_id']
        db_table = 'canteen'
        verbose_name = '食堂信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.canteen_name


class Store(models.Model):
    store_id = models.AutoField(primary_key=True, verbose_name = '商铺编号')
    canteen_id = models.ForeignKey(Canteen, models.CASCADE, '食堂编号')
    # manager = models.ForeignKey('Manager', models.SET_NULL, blank=True, null=True, verbose_name='商家')
    store_name = models.CharField(max_length=20, verbose_name='商铺名称')
    store_describe = models.CharField(max_length=200, blank=True, null=True, verbose_name='商铺描述')
    store_image = models.ImageField(upload_to='images/store', blank=True, null=True, verbose_name='商铺照片')
    store_state = models.IntegerField(choices=[(1, "营业中"), (0,"休息中")], verbose_name='商铺状态')
    # dishes = models.ManyToManyField('Dish', db_table='store_dish', )       # 多对多关系

    class Meta:
        ordering = ['store_id']
        db_table = 'store'
        verbose_name = '商铺信息'
        verbose_name_plural = verbose_name

    def __str__(self):          # 决定了外键的值
        return self.canteen_id.canteen_name+self.store_name
    def update_store_url(self): # 更新需要跳转到新的页面，但是需要知道更新的是哪一个
        # print('update_store')
        return reverse("update_store",kwargs={'store_id': self.store_id})
    def del_store_url(self): # 更新需要跳转到新的页面，但是需要知道更新的是哪一个
        # print('del_store')
        return reverse("del_store",kwargs={'store_id': self.store_id})


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True, verbose_name = '菜品编号')
    store_id = models.ForeignKey(Store, models.CASCADE, '商铺编号')
    dish_name = models.CharField(unique=True, max_length=20, verbose_name='菜品名称')
    dish_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='菜品价格')
    dish_image = models.ImageField(upload_to='images/dish',blank=True, null=True, verbose_name='菜品照片')
    dish_describe = models.CharField(max_length=200, blank=True, null=True, verbose_name='菜品描述')
    dish_state = models.IntegerField(choices=[(1,"销售中"),(2,"售罄")], verbose_name='菜品状态')
    # dish_order_num = models.IntegerField(default=0,verbose_name='下单数量')

    class Meta:
        ordering = ['dish_id']
        db_table = 'dish'
        verbose_name = '菜品信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.dish_name

    # 将菜品编号传递给订单
    def get_order_url_add(self):
        return reverse("order:get_order_add", kwargs={'dish_id': self.dish_id})
        # get_order是urlpatterns中
        # path('get_order/<slug:dish_id>', get_order, name='get_order') 里面的name；
        # kwargs为要传入path的参数
        # 注：reverse的精妙之处在于绑定了动态路由和视图（将相应参数传递给视图），并返回url
        # 将菜品编号传递给订单
    # 菜品数增加
    def get_order_url_sub(self):
        return reverse("order:get_order_sub", kwargs={'dish_id': self.dish_id})


class Manager(models.Model):
    manager_id = models.AutoField(primary_key=True, verbose_name = '管理员编号')
    manager_name = models.CharField(max_length=20, verbose_name='管理员昵称', unique=True)
    manager_phone = models.CharField(max_length=20,verbose_name='管理员联系方式')
    manager_pwd = models.CharField(max_length=100,verbose_name='管理员密码')
    manager_canteen = models.ForeignKey(Canteen, models.SET_NULL, blank=True, null=True, verbose_name='管理的食堂')
    manager_store = models.ForeignKey(Store, models.SET_NULL, blank=True, null=True, verbose_name='管理的商铺')
    manager_label = models.IntegerField(choices=[(0, "商家"), (1,"食堂管理员")], verbose_name='管理员类型')

    class Meta:
        ordering = ['manager_id']
        db_table = 'manager'
        verbose_name = '管理员信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.manager_name
