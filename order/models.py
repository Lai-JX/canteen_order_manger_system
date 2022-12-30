# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.urls import reverse

from user.models import CustomerInfo, Address
from canteen.models import Canteen, Store, Dish


class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True, verbose_name = '评论编号')
    score = models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, verbose_name='评分')
    content = models.CharField(max_length=200, blank=True, null=True, verbose_name='评价内容')
    time = models.DateTimeField(auto_now_add=True, verbose_name='评价时间')

    class Meta:
        ordering = ['time']
        db_table = 'comment'
        verbose_name = '评价信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return str(self.comment_id)


class Indent(models.Model):
    indent_id = models.AutoField(primary_key=True, verbose_name = '订单编号')
    customer = models.ForeignKey(CustomerInfo, models.CASCADE, verbose_name='顾客')
    store = models.ForeignKey(Store, models.SET_NULL,blank=True, null=True, verbose_name='商铺')
    canteen = models.ForeignKey(Canteen, models.DO_NOTHING, verbose_name='食堂')
    comment = models.ForeignKey(Comment, models.SET_NULL, blank=True, null=True, verbose_name='评论')
    date_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')
    indent_price = models.DecimalField(max_digits=5, decimal_places=2, default=0,verbose_name='订单价格')
    indent_notes = models.CharField(max_length=100, blank=True, null=True, verbose_name='订单备注')
    indent_state = models.CharField(max_length=10, default='未下单', choices=[('未下单','未下单'),('已下单', '已下单'), ('已发货', '已发货'), ('已送达', '已送达'), ('已评价', '已评价')], verbose_name='订单状态')
    dishes = models.ManyToManyField(Dish, through='IndentInventory', through_fields=('indent', 'dish'))
    indent_address = models.ForeignKey(Address, models.SET_NULL, blank=True, null=True,verbose_name='订单地址')

    class Meta:
        ordering = ['-date_time']
        db_table = 'indent'
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name

    # 删除订单
    def del_order_url(self):
        print('del_order_url')
        return reverse("order:del_order", kwargs={'order_id': self.indent_id})
    def __str__(self):
        return str(self.indent_id)


class IndentInventory(models.Model):
    indent = models.ForeignKey(Indent, models.CASCADE)
    dish = models.ForeignKey(Dish, models.CASCADE)
    dish_num = models.IntegerField(default=0, verbose_name='菜品数量')

    class Meta:
        ordering = ['indent_id','dish_id']
        db_table = 'indent_inventory'
        unique_together = (('dish', 'indent'),)
    def __str__(self):
        return '订单明细'




# class StoreDish(models.Model):
#     dish = models.OneToOneField(Dish, models.CASCADE, primary_key=True, verbose_name='菜品')
#     store = models.ForeignKey('Store', models.CASCADE, verbose_name='商铺')
#
#     class Meta:
#         ordering = ['store_id','dish_id']
#         db_table = 'store_dish'
#         unique_together = (('dish', 'store'),)
#         verbose_name = '商铺-菜品'
#         verbose_name_plural = verbose_name
