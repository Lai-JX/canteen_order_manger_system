# Generated by Django 4.1.4 on 2022-12-26 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0006_rename_canteen_store_canteen_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='store',
            old_name='store_decribe',
            new_name='store_describe',
        ),
    ]
