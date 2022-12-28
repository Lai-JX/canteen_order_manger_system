# Generated by Django 4.1.4 on 2022-12-26 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('canteen', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('comment_id', models.AutoField(primary_key=True, serialize=False, verbose_name='评论编号')),
                ('score', models.SmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5, verbose_name='评分')),
                ('content', models.CharField(blank=True, max_length=200, null=True, verbose_name='评价内容')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='评价时间')),
            ],
            options={
                'verbose_name': '评价信息',
                'verbose_name_plural': '评价信息',
                'db_table': 'comment',
                'ordering': ['time'],
            },
        ),
        migrations.CreateModel(
            name='Indent',
            fields=[
                ('indent_id', models.AutoField(primary_key=True, serialize=False, verbose_name='订单编号')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='下单时间')),
                ('indent_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='订单价格')),
                ('indent_notes', models.CharField(blank=True, max_length=100, null=True, verbose_name='订单备注')),
                ('indent_state', models.IntegerField(choices=[(0, '已下单'), (1, '已发货'), (2, '已送达'), (3, '已评价')], default=0, verbose_name='订单状态')),
                ('canteen', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='canteen.canteen', verbose_name='食堂')),
                ('comment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='order.comment', verbose_name='评论')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customerinfo', verbose_name='顾客')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
                'db_table': 'indent',
                'ordering': ['date_time'],
            },
        ),
        migrations.CreateModel(
            name='IndentInventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_num', models.IntegerField(default=1, verbose_name='菜品数量')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='canteen.dish')),
                ('indent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.indent')),
            ],
            options={
                'db_table': 'indent_inventory',
                'ordering': ['indent_id', 'dish_id'],
                'unique_together': {('dish', 'indent')},
            },
        ),
        migrations.AddField(
            model_name='indent',
            name='dishes',
            field=models.ManyToManyField(through='order.IndentInventory', to='canteen.dish'),
        ),
        migrations.AddField(
            model_name='indent',
            name='store',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='canteen.store', verbose_name='商铺'),
        ),
    ]
