# Generated by Django 4.1.4 on 2022-12-30 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0008_alter_indent_store'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='indent',
            options={'ordering': ['-date_time'], 'verbose_name': '订单信息', 'verbose_name_plural': '订单信息'},
        ),
    ]
