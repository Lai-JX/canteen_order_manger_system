# Generated by Django 4.1.4 on 2022-12-28 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0005_indent_indent_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='indentinventory',
            name='dish_num',
            field=models.IntegerField(default=0, verbose_name='菜品数量'),
        ),
    ]
