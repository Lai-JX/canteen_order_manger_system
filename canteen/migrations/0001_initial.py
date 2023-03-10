# Generated by Django 4.1.4 on 2022-12-26 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canteen',
            fields=[
                ('canteen_id', models.AutoField(primary_key=True, serialize=False, verbose_name='食堂编号')),
                ('canteen_name', models.CharField(max_length=20, verbose_name='食堂名称')),
                ('canteen_image', models.ImageField(blank=True, null=True, upload_to='images/canteen', verbose_name='食堂照片')),
                ('canteen_state', models.IntegerField(choices=[(1, '营业中'), (0, '休息中')], max_length=10, verbose_name='食堂状态')),
            ],
            options={
                'verbose_name': '食堂',
                'verbose_name_plural': '食堂',
                'db_table': 'canteen',
                'ordering': ['canteen_id'],
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('dish_id', models.AutoField(primary_key=True, serialize=False, verbose_name='菜品编号')),
                ('dish_name', models.CharField(max_length=20, unique=True, verbose_name='菜品名称')),
                ('dish_price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='菜品价格')),
                ('dish_image', models.ImageField(blank=True, null=True, upload_to='images/dish', verbose_name='菜品照片')),
                ('dish_decribe', models.CharField(blank=True, max_length=200, null=True, verbose_name='菜品描述')),
                ('dish_state', models.IntegerField(choices=[(1, '销售中'), (2, '售罄')], max_length=10, verbose_name='菜品状态')),
            ],
            options={
                'verbose_name': '菜品信息',
                'verbose_name_plural': '菜品信息',
                'db_table': 'dish',
                'ordering': ['dish_id'],
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('manager_id', models.AutoField(primary_key=True, serialize=False, verbose_name='管理员编号')),
                ('manager_name', models.CharField(max_length=20, verbose_name='管理员昵称')),
                ('manager_phone', models.CharField(max_length=20, verbose_name='管理员联系方式')),
                ('manager_pwd', models.CharField(max_length=100, verbose_name='管理员密码')),
                ('manager_label', models.IntegerField(choices=[(0, '商家'), (1, '食堂管理员')], max_length=10, verbose_name='管理员类型')),
            ],
            options={
                'verbose_name': '管理员信息',
                'verbose_name_plural': '管理员信息',
                'db_table': 'manager',
                'ordering': ['manager_id'],
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(primary_key=True, serialize=False, verbose_name='商铺编号')),
                ('store_name', models.CharField(max_length=20, verbose_name='商铺名称')),
                ('store_decribe', models.CharField(blank=True, max_length=200, null=True, verbose_name='商铺描述')),
                ('store_image', models.ImageField(blank=True, null=True, upload_to='images/store', verbose_name='商铺照片')),
                ('store_state', models.IntegerField(choices=[(1, '营业中'), (0, '休息中')], max_length=10, verbose_name='商铺状态')),
                ('canteen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='食堂编号', to='canteen.canteen')),
                ('dishes', models.ManyToManyField(db_table='store_dish', to='canteen.dish')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='canteen.manager', verbose_name='商家')),
            ],
            options={
                'verbose_name': '商铺信息',
                'verbose_name_plural': '商铺信息',
                'db_table': 'store',
                'ordering': ['store_id'],
            },
        ),
        migrations.AddField(
            model_name='canteen',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='canteen.manager', verbose_name='食堂管理员'),
        ),
    ]
