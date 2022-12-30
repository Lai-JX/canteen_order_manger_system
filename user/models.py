# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from canteen.models import Canteen, Store


class Address(models.Model):
    address_id = models.AutoField(primary_key=True, verbose_name='地址编号')
    building = models.CharField(max_length=10, verbose_name='楼栋编号')
    floor = models.CharField(max_length=10, verbose_name='楼层编号')
    dormitory_num = models.CharField(max_length=10,verbose_name='门牌号')
    address_describe = models.CharField(max_length=100, blank=True, null=True, verbose_name='地址描述')

    class Meta:
        ordering = ['address_id']
        db_table = 'address'
        verbose_name = '地址信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return f'{self.building}栋 {self.floor}层 {self.dormitory_num}; 地址描述:{self.address_describe}'
    def toStr(self):
        return f'{self.building}栋 {self.floor}层 {self.dormitory_num}; 地址描述:{self.address_describe}'

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
# class CustomerAddress(models.Model):
#     customer = models.OneToOneField('CustomerInfo', models.CASCADE, primary_key=True)
#     address = models.ForeignKey(Address, models.CASCADE)
#
#     class Meta:
#         ordering = ['customer_id','address_id']
#         db_table = 'customer_address'
#         unique_together = (('customer', 'address'),)
#         verbose_name = '顾客-地址'
#         verbose_name_plural = verbose_name


class CustomerInfo(models.Model):
    customer_id = models.AutoField(primary_key=True, verbose_name='顾客编号')
    customer_name = models.CharField(max_length=20, verbose_name='顾客昵称')
    customer_sex = models.IntegerField(choices=[(1,'男'),(0,'女')], verbose_name='性别')
    customer_phone = models.CharField(max_length=20, verbose_name='顾客联系方式')
    customer_pwd = models.CharField(max_length=100, verbose_name='顾客密码')
    addresses = models.ManyToManyField(Address, db_table='customer_address')     # 多对多关系

    class Meta:
        ordering = ['customer_id']
        db_table = 'customer_info'
        verbose_name = '顾客信息'
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.customer_name
