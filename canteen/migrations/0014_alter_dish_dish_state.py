# Generated by Django 4.1.4 on 2022-12-29 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0013_alter_manager_manager_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='dish_state',
            field=models.IntegerField(choices=[(1, '销售中'), (0, '售罄')], verbose_name='菜品状态'),
        ),
    ]
