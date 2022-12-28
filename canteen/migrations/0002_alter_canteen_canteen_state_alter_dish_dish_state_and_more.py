# Generated by Django 4.1.4 on 2022-12-26 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canteen',
            name='canteen_state',
            field=models.IntegerField(choices=[(1, '营业中'), (0, '休息中')], verbose_name='食堂状态'),
        ),
        migrations.AlterField(
            model_name='dish',
            name='dish_state',
            field=models.IntegerField(choices=[(1, '销售中'), (2, '售罄')], verbose_name='菜品状态'),
        ),
        migrations.AlterField(
            model_name='manager',
            name='manager_label',
            field=models.IntegerField(choices=[(0, '商家'), (1, '食堂管理员')], verbose_name='管理员类型'),
        ),
        migrations.AlterField(
            model_name='store',
            name='store_state',
            field=models.IntegerField(choices=[(1, '营业中'), (0, '休息中')], verbose_name='商铺状态'),
        ),
    ]