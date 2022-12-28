# Generated by Django 4.1.4 on 2022-12-28 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_indent_indent_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indent',
            name='indent_state',
            field=models.CharField(choices=[('未下单', '未下单'), ('已下单', '已下单'), ('已发货', '已发货'), ('已送达', '已送达'), ('已评价', '已评价')], default='未下单', max_length=10, verbose_name='订单状态'),
        ),
    ]